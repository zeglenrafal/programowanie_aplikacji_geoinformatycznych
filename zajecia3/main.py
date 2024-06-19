from fleet.ambulance import Ambulance
from fleet.station import Station
from operations import *
from personnel import *


def run_application():
    # zdefiniowanie naszych zasobów
    ambulance1 = Ambulance("Type B", "available", (50.095340, 19.920282), ["Stretcher", "First Aid Kit"])
    ambulance2 = Ambulance("Type A", "available", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])
    ambulance3 = Ambulance("Type A", "on mission", (50.095340, 18.920282), ["Defibrillator", "Oxygen tank"])



    employee1 = Employee("John", "Doe", 12000.0)
    employee2 = Employee("Jane", "Smith", 8000.0)

    driver1 = Driver("Mike", "Johnson", 10000.0, "DL12345", ["BLS"])
    driver2 = Driver("Anna", "Brown", 11500.0, "DL12346", ["ALS", "PHTLS"])

    # sprawdzenie czy to czasem nie są te same karetki
    if ambulance1 == ambulance2:
        raise ValueError("To są te same karetki!")

    # sprawdzenie ile mamy karetek
    print(Ambulance.get_instances_count())

    # ile mamy pracowników i kierowców
    print("number of employees:")
    print(Employee.get_max_id())
    print(employee1.display_info())
    print(employee2.display_info())
    print(driver1.display_info())
    print(driver2.display_info())

    #tworzenie stacji
    station1 = Station((50.095340, 19.920282), ambulance1, driver1, employee1)
    #sprawdzanie informacji o stacji
    station1.stationinfo()
    #sprawdzenie czy na stacji jest karetka
    station1.is_ambulance_here()

    # stworzenie kolejki
    queue = IncidentQueue()

    # zaraportowanie 2 zgłoszeń
    incident1 = Incident("Power outage in sector 4", 2, "03:02", (49.044340, 13.995282), "Monika", "Musztarda")
    incident2 = Incident("Fire alarm in building 21", 5, "03:04", (53.732340, 16.0442841), "Jan", "Banan")
    queue += incident1
    queue += incident2
   

    #lista ambulansów
    ambulance_list = [ambulance1, ambulance2, ambulance3]

    # wypisz wszystkie zgłoszenia
    print("Aktualne zgłoszenia:")
    print(queue)


    # daj kierowcy podwyżkę za super zasługi
    print(f"Przed podwyżką: {driver1.display_info()}")
    driver1.update_salary(5000.12)
    print(f"Po podwyżce: {driver1.display_info()}")

    #dopasowanie karetki do zdarzenia
    print('\n')
    print("Wydarzenia wraz obslugujacymi je karetkami: ")
    queue.match_ambulance_with_incident(ambulance_list)
    
    print('\n')
    print("Kolejnosc obslugiwanych wydarzen: ")
    print(queue)

if __name__ == "__main__":
    run_application()