import random
import over

class Planet_travel:
    def __init__(self, planet, destination, fuel, docking_module, chance_of_success, num_of_trip):
        self.current_fuel = fuel
        self.current_planet = planet
        self.planet_order = ["Thorodin", "Ydalir", "Vidar", "____", "Folkvang"]
        self.destination = destination
        self.docking_module = docking_module
        self.chance_of_success = chance_of_success
        self.num_of_trip = num_of_trip

    def travel(self):
        if(self.destination in self.planet_order):
            fuelconsumption:int = abs(self.current_planet-self.planet_order.index(self.destination))
            print(f"\tMap: {self.planet_order}")
            print(f"\tSuccess chance: {self.chance_of_success}%")
            self.current_fuel -= fuelconsumption

            if fuelconsumption > self.current_fuel:
                print(f"\n\t[You dont have enough fuel]\n")
                return self.current_fuel, self.chance_of_success, self.num_of_trip
            elif self.docking_module == 1:
                # self.current_fuel -= fuelconsumption
                print(f"\tDestination: {self.planet_order[self.current_planet]}")
                print(f"\tRemaining Fuel: {self.current_fuel}")
                self.num_of_trip += 1
                return self.current_fuel, self.chance_of_success, self.num_of_trip
            else:
                if self.chance_of_success == 0:
                    over.bad_ending("Your landing was not successful! No chance of success!")
                
                if self.chance_of_success == random.randrange(0, 101):
                    over.bad_ending("Your landing was not successful, you blew up!")
                else:
                    self.chance_of_success += 1
                    print(f"\tDestination: {self.planet_order[self.current_planet]}")
                    print(f"\tRemaining Fuel: {self.current_fuel}")
                    # print(f"\tMap: {self.planet_order}")
                    self.num_of_trip += 1
                    return self.current_fuel, self.chance_of_success, self.num_of_trip
        return
    
    def get_chance_of_success(self):
        return self.chance_of_success

class Planets:
    planet_order = ["Thorodin", "Ydalir", "Vidar", "Folkvang"]

    def __init__(self, name, fuel_need, tech_level, surface):
        self.name = name
        self.fuel_need = fuel_need
        self.tech_level = tech_level
        self.surface = surface

    def datasheet(self, current_planet):
        if current_planet == "Thorodin":
            print(f"-------------------------------------------")
            print(f"-------------------------------------------")

        

    





