
'''
#The MAIN TEST CODE FOR THIS LIBRARY
import os
import fileLib

def main():
    start()
    georeferences = fileLib.read_georeferences("georreference.txt") 
    fileLib.print_georeferences (georeferences)


def start():
    clear_screen()
    print("RF Planner\n\r")

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

if __name__ == "__main__":
    main()
'''


def read_georeferences(file_path):
    try:
        with open(file_path, 'r') as file:
            georeferences = []
            for line in file:
                parts = line.strip().split(',')
                if len(parts) != 3:
                    parts = line.strip().split(';')
                if len(parts) != 3:
                    parts = line.strip().split('\t')
                if len(parts) == 3:
                    location_name, latitude, longitude = parts
                    georeferences.append((location_name, float(latitude), float(longitude)))
                else:
                    print("Skipping invalid line:", line)
        return georeferences
    except FileNotFoundError:
        print("File not found:", file_path)
        return []

def print_georeferences ( georeferences ):
    if not isinstance(georeferences, list):
        raise TypeError("Input must be a list")
'''
    if georeferences:
        print("Read georeferences:")
        for georef in georeferences:
            print("Location Name:", georef[0])
            print("Latitude:", georef[1])
            print("Longitude:", georef[2])
            print()
    else:
        print("No georeferences read or file not found.")
'''