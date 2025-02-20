import datetime
import numpy as np
import matplotlib.pyplot as plt
from tabulate import tabulate

class AskingError(Exception):
    pass

class LessError(Exception):
    pass

class NumError(Exception):
    pass

current_date = datetime.datetime.now().strftime("%Y/%m/%d %H:%M")

# First option to display the list of vehicles
def displayCars():
    try:
        with open("Vehicle.txt", "r") as file:
            content = file.read().split("\n")
        
        car_list = []
        user_input = input("Enter 'A' for available cars and 'R' for rented cars: ")
        
        for line in content:
            car_details = line.split(",")
            car_list.append(car_details)
        
        if user_input in ["A", "R"]:         
            filter_car_list = []
            for car in car_list:
                if car and car[-1] == user_input:
                    filter_car_list.append(car)
            car_table = tabulate(filter_car_list, 
                                 headers=["Vehicle ID", "Description", "Type", "Free Mileage", "Daily Rate", "Status"], 
                                 tablefmt="grid")
            print(car_table)
            print("\n")
        else:
            raise AskingError
        
        main_menu()
    except AskingError:
        print("\n------ Please Enter only 'A' or 'R' ---------\n")
        main_menu()

# Function to more new vehicles
def addAnotherVehicle():
    add_another = input("Do you want to add another vehicle? Press 'Y' for yes and 'N' for no: ")
    if add_another == "Y":
        addVehicle()
    elif add_another == "N":
        main_menu()
    else:
        print("Please enter either 'Y' or 'N'.")
        addAnotherVehicle()

# Function to originally add vehicle information
def addVehicle():
    try:
        vehicle_id = input("Enter the vehicle ID: ")
        with open("Vehicle.txt", "r") as file:
            content = file.read().split("\n")
        
        for line in content:
            if vehicle_id in line:
                print("This vehicle ID is already being used. Please enter another ID.")
                main_menu()
        
        vehicle_name = input("Enter vehicle's name: ")
        vehicle_type = input("Enter the type of vehicle ('O' for ordinary or 'P' for premium): ")
        
        if vehicle_type == "P":
            mileage_allowance = float(input("Enter the mileage allowance for the premium vehicle: "))
            if not isinstance(mileage_allowance, float):
                raise ValueError
        elif vehicle_type == "O":
            mileage_allowance = 0
        else:
            raise Exception
        
        daily_rate = float(input("Enter the daily rent rate for the vehicle: "))
        if daily_rate <= 0 or not isinstance(daily_rate, float):
            raise LessError
        
        vehicle_status = "A"
        
        with open("Vehicle.txt", "a") as file:
            file.write(f"\n{vehicle_id},{vehicle_name},{vehicle_type},{mileage_allowance},{daily_rate},{vehicle_status}\n")
        
        print("The vehicle has been successfully added.")
        addAnotherVehicle()
    except ValueError:
        print("Enter a valid number value.")
        addVehicle()
    except LessError:
        print("Enter a number greater than zero.")
        addVehicle()
    except Exception:
        print("Enter only 'O' or 'P'.")
        addVehicle()

# Function to delete vehicle information from the text file
def deleteVehicle():
    try:
        vehicle_id = input("Enter the vehicle ID: ")
        with open("Vehicle.txt", "r") as file:
            content = file.read().split("\n")
        
        deleted_vehicles = []
        vehicle_found = False
        
        for line in content:
            if vehicle_id in line:
                deleted_vehicles.append(line)
                content.remove(line)
                vehicle_found = True
        
        if not vehicle_found:
            raise AskingError
        
        with open("Vehicle.txt", "w") as file:
            for line in content:
                file.write(line + "\n")
        
        with open("deletedVehicles.txt", "a") as file:
            for line in deleted_vehicles:
                file.write(line + "\n")
        
        print("The vehicle info has been successfully deleted.")
        deleteAnotherVehicle()
    except AskingError:
        print("Vehicle ID not found. Enter the correct vehicle ID.")
        deleteVehicle()

def deleteAnotherVehicle():
    user_input = input("Do you want to delete another vehicle? Press 'Y' for yes and 'N' for no: ")
    if user_input == "Y":
        deleteVehicle()
    elif user_input == "N":
        main_menu()
    else:
        print("Press either 'Y' or 'N'.")
        deleteAnotherVehicle()

def rentDetails(vehicle_id, renter_id, rent_date, start_odometer, daily_rate, accessories_cost):
    with open("rentVehicle.txt", "a") as file:
        file.write(f"\n{vehicle_id},{renter_id},{rent_date},{start_odometer},{daily_rate},{accessories_cost}")
    print("Renting is successful\n")

def rentVehicle():
    try:
        vehicle_id = input("Enter the vehicle ID: ")
        with open("Vehicle.txt", "r") as file:
            content = file.read().split("\n")
        
        vehicle_found = False
        for line in content:
            vehicle_details = line.split(",")
            if vehicle_id in line:
                vehicle_found = True
                if line.endswith("R"):
                    print("Sorry! This vehicle is not available.\nPlease enter another vehicle ID.\n")
                    rentVehicle()
                else:
                    if vehicle_details[2] == "O":
                        updated_line = line[:-1] + "R"
                        renter_id = input("Enter your renter ID: ")
                        start_odometer = float(input("Enter the initial odometer reading: "))
                        if not isinstance(start_odometer, float) or start_odometer <= 0:
                            raise ValueError
                        accessories_cost = 0
                        print(f"Car {vehicle_id} is rented to {renter_id}\n")
                        print("************************** Vehicle Details ****************************")
                        print(f"Vehicle ID: {vehicle_id}")
                        print(f"Description: {vehicle_details[1]}")
                        print(f"Daily Rate: €{vehicle_details[4]}")
                        print(f"Accessories: €{accessories_cost}")
                        print(f"Status: {vehicle_details[5]}")
                        print(f"Renter ID: {renter_id}")
                        print(f"Date/time of rent: {current_date}")
                        print(f"Rent starting odometer: {start_odometer}")
                        rentDetails(vehicle_id, renter_id, current_date, start_odometer, vehicle_details[4], accessories_cost)
                        content.remove(line)
                        content.append(updated_line)
                        with open("Vehicle.txt", "w") as file:
                            for line in content:
                                file.write(line + "\n")
                    elif vehicle_details[2] == "P":
                        updated_line = line[:-1] + "R"
                        renter_id = input("Enter your renter ID: ")
                        start_odometer = float(input("Enter the initial odometer reading: "))
                        if not isinstance(start_odometer, float) or start_odometer <= 0:
                            raise ValueError
                        accessories_cost = 0
                        print("Do you want to add additional accessories to your vehicle?")
                        print("1. Mini-fridge")
                        print("2. GPS navigator")
                        print("3. Window blinds for blocking sunlight")
                        print("4. Emergency toolkit")
                        add_accessories = input("Press 'Y' for yes and 'N' for no: ")
                        if add_accessories == "Y":
                            while True:
                                accessory_choice = int(input("Enter the appropriate number: "))
                                if accessory_choice in [1, 2, 3, 4]:
                                    accessories_cost += 20
                                    more_accessories = input("Press 'Y' for another accessory and 'N' if not: ")
                                    if more_accessories == "N":
                                        break
                                    elif more_accessories not in ["N", "Y"]:
                                        raise AskingError
                                else:
                                    raise LessError
                        elif add_accessories not in ["N", "Y"]:
                            raise AskingError
                        print(f"Car {vehicle_id} is rented to {renter_id}\n")
                        print("************************** Vehicle Details ****************************")
                        print(f"Vehicle ID: {vehicle_id}")
                        print(f"Description: {vehicle_details[1]}")
                        print(f"Daily Rate: €{vehicle_details[4]}")
                        print(f"Accessories: €{accessories_cost}")
                        print(f"Status: {vehicle_details[5]}")
                        print(f"Renter ID: {renter_id}")
                        print(f"Date/time of rent: {current_date}")
                        print(f"Rent starting odometer: {start_odometer}")
                        rentDetails(vehicle_id, renter_id, current_date, start_odometer, vehicle_details[4], accessories_cost)
                        content.remove(line)
                        content.append(updated_line)
                        with open("Vehicle.txt", "w") as file:
                            for line in content:
                                file.write(line + "\n")
                break
        if not vehicle_found:
            print("The vehicle ID entered is wrong.\nPlease enter the correct vehicle ID.")
        main_menu()
    except AskingError:
        print("Either press 'Y' or 'N' only.")
        rentVehicle()
    except ValueError:
        print("Please enter the odometer reading only in number format.")
        rentVehicle()
    except LessError:
        print("Please enter only the numbers mentioned above.")
        rentVehicle()

# Function to check and calculate how much to charge the customers for renting vehicles
def transact(vehicle_id, renter_id, return_date, start_odometer, end_odometer, kms_run, rent_charge):
    with open("Transactions.txt", "a") as file:
        file.write(f"\n{vehicle_id},{renter_id},{return_date},{start_odometer},{end_odometer},{kms_run},{rent_charge}")
    print(f"Car {vehicle_id} is returned.\n")

# Function to let users return and stop the vehicle rent
def rentComplete():
    try:
        vehicle_id = input("Enter the vehicle ID: ")
        with open("Vehicle.txt", "r") as file:
            content = file.read().split("\n")
        
        vehicle_found = False
        for line in content:
            if vehicle_id in line:
                vehicle_found = True
                if line.endswith("A"):
                    print("Sorry! This vehicle is not rented.\nPlease enter another vehicle ID.\n")
                    main_menu()
                    break
                else:
                    updated_line = line[:-1] + "A"
                    with open("rentVehicle.txt", "r") as file:
                        rent_data = file.read().split("\n")
                    
                    for rent_line in rent_data:
                        if vehicle_id in rent_line:
                            rent_details = rent_line.split(",")
                            start_date = int(rent_details[2][8:10])
                            start_day = datetime.timedelta(days=start_date)
                            today_date = datetime.datetime.now()
                            end_date = today_date - start_day + datetime.timedelta(days=1)
                            end_date_str = end_date.strftime("%d")
                            end_date_int = int(end_date_str)
                            end_odometer = float(input("Enter the final odometer reading: "))
                            if end_odometer <= float(rent_details[3]):
                                raise ValueError
                            kms_run = end_odometer - float(rent_details[3])
                            daily_rate = float(rent_details[4])
                            if rent_details[2] == "O":
                                rent_charge = (end_date_int * daily_rate) + (end_date_int * float(rent_details[5])) + (kms_run * 0.020)
                            elif rent_details[2] == "P":
                                rent_charge = (end_date_int * daily_rate) + (end_date_int * float(rent_details[5])) + (kms_run * 0.025)
                            rent_charge = str(rent_charge)
                            print(f"Car {vehicle_id} is returned from {rent_details[1]}")
                            print("************************** Vehicle Details ****************************")
                            print(f"Vehicle ID: {vehicle_id}")
                            print(f"Description: {rent_details[1]}")
                            print(f"Daily Rate: {daily_rate}")
                            print(f"Accessories: {rent_details[5]}")
                            print(f"Renter ID: {rent_details[1]}")
                            print(f"Date/time of return: {current_date}")
                            print(f"Rent starting odometer: {rent_details[3]}")
                            print(f"Rent end odometer: {end_odometer}")
                            print(f"Kms run: {kms_run}")
                            print(f"Rental charges: {rent_charge} Euros")
                            transact(vehicle_id, rent_details[1], current_date, rent_details[3], end_odometer, kms_run, rent_charge)
                            content.remove(line)
                            content.append(updated_line)
                            with open("Vehicle.txt", "w") as file:
                                for line in content:
                                    file.write(line + "\n")
                            break
        if not vehicle_found:
            print("The vehicle ID entered is wrong.\nPlease enter the correct vehicle ID.")
        main_menu()
    except ValueError:
        print("Enter the odometer reading in number format and more than the initial reading.")
        rentComplete()

# Function to check which vehicles are premium brands
def vehicleChart():
    with open("Vehicle.txt", "r") as file:
        content = file.read().split("\n")
    
    ordinary_cars = []
    premium_cars = []
    car_types = ["Ordinary", "Premium"]
    car_counts = []
    
    for line in content:
        car_details = line.split(",")
        if car_details[2] == "O":
            ordinary_cars.append(car_details[0])
        elif car_details[2] == "P":
            premium_cars.append(car_details[0])
    
    car_counts.append(len(ordinary_cars))
    car_counts.append(len(premium_cars))
    
    plt.bar(car_types, car_counts)
    plt.ylabel("Number of cars")
    plt.show()
    main_menu()

# Exit the system
def exit():
    print("Thanks for using Car Rental System. Bye! Bye!")

# Main menu for the system
def main_menu():
    try:
        print("       Vehicle Rent Menu")
        print("1. Display Available Cars")
        print("2. Add/Delete Vehicle Info")
        print("3. Rent Vehicle")
        print("4. Complete Rent")
        print("5. Reporting Vehicle Information")
        print("6. Exit")
        choice = int(input("Enter the appropriate number given above: "))
        if choice == 1:
            displayCars()
        elif choice == 2:
            sub_choice = int(input("Enter 1 to add a vehicle info and 2 to delete a vehicle info: "))
            if sub_choice == 1:
                addVehicle()
            elif sub_choice == 2:
                deleteVehicle()
            else:
                raise AskingError
        elif choice == 3:
            rentVehicle()
        elif choice == 4:
            rentComplete()
        elif choice == 5:
            vehicleChart()
        elif choice == 6:
            exit()
        else:
            print("Enter only the options given above")
            main_menu()
    except AskingError:
        print("Please enter only 1 or 2.")
        main_menu()
    except ValueError:
        print("Enter only the options given above")
        main_menu()

main_menu()
