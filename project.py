import datetime
import numpy as np
import matplotlib.pyplot as mp
class AskingError(Exception):
    pass
class LessError(Exception):
    pass
class NumError(Exception):
    pass
current_date=datetime.datetime.now().strftime("%Y/%m/%d %H:%M")


#1st option
def displayCars():
    try:
        dispfile = open("Vehicle.txt","r")
        content=dispfile.read()
        content=content.split("\n")
        dl=[]
        ask=input("enter 'A' if you want available cars and 'R' if you want rented cars:")
        for i in content:
            dl.append(i)
        if(ask=="A" or ask=="R"):
            print("Vehicle ID | "+"Description | "+"Type | "+"free mileage | "+"Daily rate | "+"Status")
            print()
            for j in dl:
                dl2=j.split(",")
                if(ask=="A"):
                    if "A" in dl2:
                        for x in dl2:
                            if x.endswith("A"):
                                print(x)
                            else:
                                print(x,end="  |  ")
                        print()
                elif(ask=="R"):
                    if "R" in dl2:
                        for x in dl2:
                            if x.endswith("R"):
                                print(x)
                            else:
                                print(x,end="  |  ")
                        print()
        else:
            raise AskingError
        dispfile.close()
        main_menu()
    except AskingError:
        print("")
        print("------ Please Enter only 'A' or 'R' ---------")
        print("")
        main_menu()




def addAnotherVehicle():
        addAnother=input("Do you want to add another vehicle? press 'Y' if yes and 'N' if no:")
        if addAnother=="Y":
            AddVehicle()
        elif addAnother=="N":
            main_menu()
        else:
            print ("Please enter either 'Y' or 'N'.")
            addAnotherVehicle()



def AddVehicle():
    try:
        vehicleID=input("Enter the vehicle ID: ")
        dispfile = open("Vehicle.txt","r")
        content=dispfile.read()
        content=content.split("\n")
        dispfile.close()
        for i in content:
            if vehicleID in i:
                print("This vehicle ID is already being used. Please enter another ID.")
                main_menu()
        else:
            Vname=input("Enter vehicle's name:")
            Vtype=input("Enter the type of vehicle. Either 'O' for ordinary or 'P' for premium:")
            if(Vtype=="P"):
                MilAllow=float(input("Enter the mileage allowance for the premium vehicle:"))
                if(type(MilAllow)!=float):
                    raise ValueError
                MilAllow2=str(MilAllow)
            elif(Vtype=="O"):
                MilAllow=str(0)
            else:
                raise Exception
            Vrent=float(input("Enter the Daily rent rate for the vehicle in integers or float only:"))
            if(Vrent<=0) or (type(Vrent)!=float):
                raise LessError
            Vrent2=str(Vrent)
            Vstatus=("A")
            editfile = open("Vehicle.txt","a")
            editfile.write("\n"+vehicleID + ",")
            editfile.write(Vname + ",")
            editfile.write(Vtype + ",")
            editfile.write(MilAllow2 + ",")
            editfile.write(Vrent2 + ",")
            editfile.write(Vstatus + "\n")
            editfile.close()
            print("The vehice has been successfully added.")
            addAnotherVehicle()
    except ValueError:
        print("Enter the number value only and more than or equal to zero only.")
        AddVehicle()
    except LessError:
        print("Enter the number value only and more than zero.")
        AddVehicle()
    except Exception:
        print("Enter only 'O' or 'P'.")
        AddVehicle()




def DeleteVehicle():
    try:
        vehicleID=input("Enter the vehicle ID: ")
        dispfile = open("Vehicle.txt","r")
        content=dispfile.read()
        content=content.split("\n")
        dispfile.close()
        dl=[]
        t=0
        for i in content:
            if vehicleID in i:
                dl.append(i)
                content.remove(i)
                t=t+1
        if(t==0):
            raise AskingError
        editfile = open("Vehicle.txt","w")
        for edit_content in content:
            editfile.write(edit_content + "\n")
        editfile.close()
        editdelete = open("deletedVehicles.txt","a")
        for edit2 in dl:
            editdelete.write(edit2 + "\n")
        editdelete.close()
        print("The vehicle info has been successfully deleted.")
        deleteAnotherVehicle()
    except AskingError:
        print("Vehicle ID not found. Enter the correct vehicle ID.")
        DeleteVehicle()

#delete vehicle sub function
def deleteAnotherVehicle():
    print("Do you want to delete another vehicle?")
    x=(input("press 'Y' if yes and 'N' if no:"))
    if(x=="Y"):
        DeleteVehicle()
    elif(x=="N"):
        main_menu()
    else:
        print("Press either Y or N")
        deleteAnotherVehicle()


#sub function for 3rd option
def rentDetails(a,b,c,d,e,f):
    dispfile=open("rentVehicle.txt","a")
    dispfile.write("\n")
    dispfile.write(a)
    dispfile.write(",")
    dispfile.write(b)
    dispfile.write(",")
    dispfile.write(c)
    dispfile.write(",")
    dispfile.write(d)
    dispfile.write(",")
    dispfile.write(e)
    dispfile.write(",")
    dispfile.write(f)
    print("Renting is successful","\n")
    dispfile.close()




#3rd option
def rentVehicle():
    try:
        vehicleID=input("Enter the vehicle ID: ")
        dispfile = open("Vehicle.txt","r+")
        content=dispfile.read()
        content=content.split("\n")
        dispfile.close()
        dl=[]
        x=0
        y=0
        y=int(y)
        for i in content:
            i4=i.split(",")
            y=y+1
            if vehicleID in i:
                x=x+1
                if (i.endswith("R")):
                    print("Sorry! this vehicle is not available.","\n","Please enter some other vehicle ID.","\n")
                    rentVehicle()
                else:
                    if(i4[2]=="O"):
                        i2=i[:-1] + "R"
                        dl.append(i2)
                        for j in dl:
                            dl2=j.split(",")
                        print("the vehicle is available")
                        renterID=input("Enter your renter ID: ")
                        rent_starting_odometer=float(input("Enter the initial odometer reading:"))
                        if(type(rent_starting_odometer)!=float) or (rent_starting_odometer<=0):
                            raise ValueError
                        acctotal=int(0)
                        acctotal2=str(acctotal)
                        print("Car",vehicleID,"is rented to",renterID,"\n")
                        print("************************** Vehicle Details ****************************")
                        print("Vehicle ID=",vehicleID)
                        print("Description=",dl2[1])
                        print("Daily Rate= €"+dl2[4])
                        print("accessories= €"+acctotal2)
                        print("Status=",dl2[5])
                        print("renter ID=",renterID)
                        print("Date/time of rent=",current_date)
                        print("rent starting odometer=",rent_starting_odometer)
                        rent_starting_odometer2=str(rent_starting_odometer)
                        daily_rate=str(dl2[4])
                        rentDetails(vehicleID,renterID,current_date,rent_starting_odometer2,daily_rate,acctotal2)
                        content.remove(i)
                        content.insert(y,i2)
                        editfile = open("Vehicle.txt","w")
                        for edit_content in content:
                            editfile.write(edit_content + "\n")
                        editfile.close()
                    elif(i4[2]=="P"):
                        i2=i[:-1] + "R"
                        dl.append(i2)
                        for j in dl:
                            dl2=j.split(",")
                        print("the vehicle is available")
                        renterID=input("Enter your renter ID: ")
                        rent_starting_odometer=float(input("Enter the initial odometer reading:"))
                        if(type(rent_starting_odometer)!=float) or (rent_starting_odometer<=0):
                            raise ValueError
                        accnumber=0
                        print("Do you want to add additional accessories to your vehicle?")
                        print("Mini-fridge:","                         1")
                        print("GPS navigator:","                       2")
                        print("window blinds for blocking sunlight:"," 3")
                        print("emergency toolkit:","                   4")
                        y2=input("Press 'Y' if yes and 'N' if no:")
                        if(y2=="Y"):
                            while True:
                                x2=int(input("Enter the appropriate number:"))
                                if(x2==1 or x2==2 or x2==3 or x2==4):
                                    accnumber=accnumber+1
                                    x4=input("press 'Y' if you want another accessory and 'N' if not:")
                                    if(x4=="N"):
                                        break
                                    elif(x4!="N" and x4!="Y"):
                                        raise AskingError
                                else:
                                    raise LessError
                        elif(y2!="N" and y2!="Y"):
                            raise AskingError
                        acctotal=(20*accnumber)
                        acctotal2=str(acctotal)
                        print("Car",vehicleID,"is rented to",renterID,"\n")
                        print("************************** Vehicle Details ****************************")
                        print("Vehicle ID=",vehicleID)
                        print("Description=",dl2[1])
                        print("Daily Rate= €"+dl2[4])
                        print("accessories= €"+acctotal2)
                        print("Status=",dl2[5])
                        print("renter ID=",renterID)
                        print("Date/time of rent=",current_date)
                        print("rent starting odometer=",rent_starting_odometer)
                        rent_starting_odometer2=str(rent_starting_odometer)
                        daily_rate=str(dl2[4])
                        rentDetails(vehicleID,renterID,current_date,rent_starting_odometer2,daily_rate,acctotal2)
                        content.remove(i)
                        content.insert(y,i2)
                        editfile = open("Vehicle.txt","w")
                        for edit_content in content:
                            editfile.write(edit_content + "\n")
                        editfile.close()
                break
        if(x==0):
            print("the vehicle id entered is wrong","\n","please enter the correct vehicle ID")
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



#sub function for 4th option
def transact(a,b,c,d,e,f,g):
    dispfile=open("Transactions.txt","a")
    dispfile.write("\n")
    dispfile.write(a)
    dispfile.write(",")
    dispfile.write(b)
    dispfile.write(",")
    dispfile.write(c)
    dispfile.write(",")
    dispfile.write(d)
    dispfile.write(",")
    dispfile.write(e)
    dispfile.write(",")
    dispfile.write(f)
    dispfile.write(",")
    dispfile.write(g)
    print("Car",a,"is returned.","\n")
    dispfile.close()


#4th option
def rentComplete():
    try:
        vehicleID=input("Enter the vehicle ID: ")
        dispfile = open("Vehicle.txt","r")
        content=dispfile.read()
        content=content.split("\n")
        dispfile.close()
        dl=[]
        rl=[]
        x=0
        y=0
        y=int(y)
        for i in content:
            y=y+1
            if vehicleID in i:
                r=i.split(",")
                x=x+1
                if (i.endswith("A")):
                    print("Sorry! this vehicle is not rented.","\n","Please enter some other vehicle ID.","\n")
                    main_menu()
                    break
                else:
                    i2=i[:-1] + "A"
                    rl.append(i2)
                    for k in rl:
                        rl2=k.split(",")
                    readfile=open("rentVehicle.txt","r")
                    data=readfile.read()
                    data=data.split("\n")
                    readfile.close()
                    for h in data:
                        if vehicleID in h:
                            x=x+1
                            dl.append(h)
                            for j in dl:
                                dl2=j.split(",")
                                start_date=(dl2[2])
                                start_date=start_date[8:]
                                start_date=start_date[:3]
                                start_date=int(start_date)
                            start_day=datetime.timedelta(days=start_date)
                            today_date=datetime.datetime.now()
                            add_date=datetime.timedelta(days=1)
                            end_date = today_date - start_day + add_date
                            end_date_str=end_date.strftime("%d")
                            end_date_int=int(end_date_str)
                            rent_end_od_int=float(input("Enter the final odometer reading:"))
                            if(rent_end_od_int<=float(dl2[3])):
                                raise ValueError
                            kms_run=(rent_end_od_int-float(dl2[3]))
                            daily_rate=rl2[4]
                            daily_rate=float(daily_rate)
                            if r[2]=="O":
                                rent_charge=(int(end_date_int)*int(daily_rate))+(int(end_date_int)*int(dl2[5]))+(int(kms_run)*(0.020))
                            elif r[2]=="P":
                                rent_charge=(int(end_date_int)*int(daily_rate))+(int(end_date_int)*int(dl2[5]))+(int(kms_run)*(0.025))
                            rent_charge=str(rent_charge)
                    print("Car",vehicleID,"is returned from",dl2[1])
                    print("************************** Vehicle Details ****************************")
                    print("vehicle ID=",vehicleID)
                    print("Description=",rl2[1])
                    print("Daily Rate=",rl2[4])
                    print("Accessories=",dl2[5])
                    print("Renter ID=",dl2[1])
                    print("Date/time of return =",current_date)
                    print("rent starting odometer=",dl2[3])
                    rent_end_od=str(rent_end_od_int)
                    print("rent end odometer=",rent_end_od)
                    print("kms.run=",kms_run)
                    kms_run2=str(kms_run)
                    print("rental charges=",rent_charge,"Euros")
                    transact(vehicleID,dl2[1],current_date,rl2[3],rent_end_od,kms_run2,rent_charge)
                    content.remove(i)
                    content.insert(y,i2)
                    editfile=open("Vehicle.txt","w")
                    for edit_content in content:
                        editfile.write(edit_content + "\n")
                    editfile.close()
                    break
        if(x==0):
            print("the vehicle id entered is wrong","\n","please enter the correct vehicle ID")
        main_menu()
    except  ValueError:
        print("enter the odometer reading in number format and more than the initial reading.")
        rentComplete()


#5th option
def VehicleChart():
    dispfile = open("Vehicle.txt","r")
    content=dispfile.read()
    content=content.split("\n")
    dl=[]
    dl3=[]
    dl4=[]
    typelist=["Ordinary","premium"]
    carslist=[]
    for i in content:
        dl.append(i)
    for j in dl:
        dl2=j.split(",")
        if (dl2[2]=="O"):
            dl3.append(dl2[0])
        elif (dl2[2]=="P"):
            dl4.append(dl2[0])
    x,y=len(dl3),len(dl4)
    carslist.append(x)
    carslist.append(y)
    mp.bar(typelist,carslist)
    mp.show()
    mp.ylabel("Number of cars")
    main_menu()








#6th option
def exit():
    print("Thanks for using Car Rental System. Bye! Bye!")



def main_menu():
    try:
        print("       ","Vehicle Rent Menu")
        print("Display Available Cars:","        ","1")
        print("Add/Delete Vehicle Info:","       ","2")
        print("Rent Vehicle:","                  ","3")
        print("Complete Rent:","                 ","4")
        print("Reporting vehicle information:"," ","5")
        print("Exit:","                          ","6")
        choice=int(input("Enter the appropriate number given above:"))
        if choice==1:
            displayCars()
        if choice==2:
            x=int(input("Enter 1 if you want to add a vehicle info and 2 if you want to delete a vehicle info:"))
            if x==1:
                AddVehicle()
            elif x==2:
                DeleteVehicle()
            elif(x!=1 and x!=2):
                raise AskingError
        elif choice==3:
            rentVehicle()
        elif choice==4:
            rentComplete()
        elif choice==5:
            VehicleChart()
        elif choice==6:
            exit()
        elif(type(choice)!=float):
            raise ValueError
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