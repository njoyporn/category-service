import datetime, json
from backend_shared.types import Timestamp

class DBUtils:
    def __init__(self):
        pass

    def split(self, item, type=None):
        try:
            if not item: return []
            if type == "number":
                res = []
                if "," in item: 
                    for i in item.split(","):
                        res.append(int(i.strip()))
                    return res
                return [int(item)]
            if "," in item: return item.split(",")
            return [item]
        except: return []

    def category_to_json(self, entry):
        category_json = {}
        try:
            category_json = {
                "id": entry[0],
                "name": entry[1],
                "info": entry[2],
                "thumbnails": self.split(entry[3], "number")
            }
            return category_json
        except Exception as e:
            return category_json  
        
    def get_date_string(self):
        return datetime.datetime.now().strftime('%Y-%m-%d')
    
    def get_one_month_ago(self):
        return (datetime.datetime.now() - datetime.timedelta(days=30)).strftime('%Y-%m-%d')
    
    def ist_older_than_18(self, geburtsdatum):
        values = str(geburtsdatum).split("-")
        today = datetime.datetime.now()
        eighteenyears = datetime.timedelta(days=18*365+5)
        date_of_birth = datetime.datetime(int(values[0]), int(values[1]), int(values[2]))
        return today - eighteenyears > date_of_birth