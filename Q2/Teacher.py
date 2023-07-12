class Teacher:
    def __init__(self, name="", salary=-1):
        self.Name = name
        self.Salary = salary
    def __repr__(self):
        return f"({self.Name}, {self.Salary})"    
