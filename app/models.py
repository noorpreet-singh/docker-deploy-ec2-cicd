# In-memory storage
todos = [
    {"id": 1, "task": "Learn Docker"},
    {"id": 2, "task": "Deploy EC2"}
]
next_id = 3

home = {"message" : "welcome back 4::"} 
health = {"status" : "healthy"}

class Todo:

    @staticmethod
    def get_home():
        return home

    @staticmethod
    def get_health():
        return health


    @staticmethod
    def get_all():
        return todos
    
    @staticmethod
    def create(task):
        global next_id
        new_todo = {"id": next_id, "task": task}
        todos.append(new_todo)
        next_id += 1
        return new_todo
