from datetime import datetime


# zadanie 1 
# zadanie 2
class Incident:
    __max_id = 0

    def __init__(self, description, priority, time, location, name, lastname):
        Incident.__max_id += 1
        self.id = Incident.__max_id
        self.description = description
        self.priority = priority
        self.time = datetime.strptime(time, "%H:%M").time()
        self.location = location
        self.name = name
        self.lastname = lastname
       


    def __str__(self):
        return f"Incident {self.id}: {self.description}, priority: {self.priority}, time: {self.time}"