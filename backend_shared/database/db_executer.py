import datetime, re

class Executer:
    def __init__(self, connection, config):
        self.connection = connection
        self.config = config
    
    def get_category_by_id(self, id):
        rc, result = self.connection.execute(f"select * from {self.config['database']['name']}.{self.config['database']['tables'][0]['name']} where id = {id}")
        return result
    
    def get_categories(self):
        rc, result = self.connection.execute(f"select * from {self.config['database']['name']}.{self.config['database']['tables'][0]['name']}")
        return result
    
    def create_category(self, id, name):
        rc, result = self.connection.execute(f'''insert into {self.config["database"]["name"]}.{self.config["database"]["tables"][0]["name"]} (
                                id,
                                name                                  
                                created_at,
                                updated_at) 
                                values (
                                '{id}',
                                '{name}',
                                '{datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}',
                                '{datetime.datetime.now().strftime('%Y-%m-%dT%H:%M:%S')}')''')