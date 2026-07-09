from app.models import Todo

class TodoService:



    @staticmethod
    def get_home():
        return Todo.get_home()

    @staticmethod
    def get_health():
        return Todo.get_health()


    @staticmethod
    def get_all_todos():
        return Todo.get_all()
    
    @staticmethod
    def create_todo(task):
        return Todo.create(task)
