'''
#The MAIN TEST CODE FOR THIS LIBRARY
import os
import fileLib
import plannerLib

def main():
    prepare_to_start_app()
    georeferences = fileLib.read_georeferences("georreference.txt") 
    fileLib.print_georeferences (georeferences)
    NewPlanner = plannerLib.Planner("NOUVENN - Project-HZ",georeferences,100)
    NewPlanner.printPlanner()

def prepare_to_start_app():
    clear_screen()
    print("RF PLANNER 2.0\n\r")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()

'''

class DevicePosition:
    def __init__(self,DevicePosition_name, DevicePosition_latitude, DevicePosition_longitude, DevicePosition_range):
        self.DevicePosition_name = DevicePosition_name
        self.DevicePosition_latitude = DevicePosition_latitude
        self.DevicePosition_longitude = DevicePosition_longitude
        self.DevicePosition_range = DevicePosition_range
        self.DevicePosition_density = 0
    
    def __str__(self):
        return  f"{self.DevicePosition_name},{self.DevicePosition_latitude},{self.DevicePosition_longitude},{self.DevicePosition_range},{self.DevicePosition_density}"


class Planner:
    def __init__(self, Planner_name, List_georeferences, default_range = 90):
        self.Planner_name = Planner_name
        self.DevicePositionList = []

        if not isinstance(List_georeferences, list):
            raise TypeError("Input must be a list")
        if List_georeferences:
            print("Read georeferences:")
            for georef in List_georeferences:
                self.DevicePositionList.append(DevicePosition(georef[0],georef[1],georef[2],default_range))
        else:
            print("No georeferences read or file not found.")

    def printPlanner (self):
        print( f"{self.Planner_name}---------------------------")
        for georef in self.DevicePositionList:
                print(georef)