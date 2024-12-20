# 2 = teli, 1 = félig, 0 = üres
fuel: int = 0
location: int = 0 # 0, 1, 2, 3, 4
# az "űrt" minding "_____"-el jelöljük, vagyis 5*_
map: str = ["Thorodin", "Ydalir", "Vidar", "_____", "Folkvang"]

def destination(dest):
    if dest == 0:
        print("Cobra")
    if dest == 1:
        print("Thorodin")
    if dest == 2:
        print("Ydalir")
    if dest == 3:
        print( "Vidar")
    if dest == 4:
        print( "Folkvang")

def status():
    print(f"location: {map[location]}")
    print(f"fuel: {fuel}")
    print(f"map: {map}")

def printmap():
    print(f"map: {map}")

def travel(destination:str, location:str, fuel:int):
    map: str = ["Thorodin", "Ydalir", "Vidar", "_____", "Folkvang"]
    if(destination in map):
        fuelconsumption:int = abs(location-map.index(destination))
        if fuelconsumption > fuel:
            print("you dont have enough fuel")
        else:
            fuel = fuel - fuelconsumption
            location=map.index(destination)
    else: print("destination does not exist")