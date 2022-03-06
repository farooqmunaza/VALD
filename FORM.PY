def inputs():
    Name = input("Enter your name :")
    Surname = input("Enter your surname :")
    Mob_No = input("Enter the mobile number :")
    if len(Mob_No):
        Birth_Date = input("Enter your birth date in dd-mm-yyyy format:")
        Age = input("Enter your age with months after decimal point :")#Convert the input such that it can accept float value
        print("Form is submitted")
    else:
        print("Not a valid number. Please enter a valid number")
        #Call the function
    print("\nThe details of the person are :\n","\nThe name is :\t", Name, "\nThe surname is :\t", , "\nThe mobile number is :\t", , "\nThe birth date is :\t", , "\nThe age is :\t", )
#Call the function
