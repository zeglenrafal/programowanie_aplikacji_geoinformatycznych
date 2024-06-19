#zadanie 3
class Station:
    __max_id = 0

    def __init__(self, location, ambulance, driver, employee):
        Station.__max_id += 1
        self.id = Station.__max_id
        self.location = location 
        self.ambulance = ambulance
        self.driver = driver
        self.employee = employee

    def stationinfo(self):
        print("Station ID: " + str(self.id) + ", Location: " + str(self.location))
        print("Employee" +self.employee.first_name + self.employee.last_name)
        print(self.ambulance.__str__())
        print("Driver" + self.driver.first_name + self.driver.last_name + self.driver.license_number)
        

    def is_ambulance_here(self):
        if self.location == self.ambulance.location:
            print('Na stacji jest dostepna karetka')
            return True
        return False