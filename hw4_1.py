# Leah Toutounjian
# HW4_1

def main():
    
    selection = "a"
    day = 0
    
    while selection != "q" and selection != "Q":
        print("\nDATE PROCESSING MENU")
        print("-----------------------------------")
        print("a) Process and Display a Date")
        print("q) Quit the Program")
        
        selection = input("\nPlease make a selection: ")
        
        while selection != "a" and selection != "q":
            print("Invalid selection. Please try again!")
            selection = input("\nPlease make a selection: ")
        
        if selection == "a" or selection == "A":
            
            enteredDates = str(input("\nPlease enter dates in this form [mm/dd/yyyy] : "))
            month, day, year = enteredDates.split("/")
            enteredDates = enteredDates.replace("/", "")
            enteredDates = enteredDates.isdigit()
            
            while enteredDates == False:
                print("\nInvalid input!")
                enteredDates = str(input("Please enter dates in this form [mm/dd/yyyy] : "))
                month, day, year = enteredDates.split('/')
                enteredDates = enteredDates.replace("/", "")
                enteredDates = enteredDates.isdigit()
                     
            if month == "01":
                month = "January"
            
            elif month == "02":
                month = "February"
                
            elif month == "03":
                month = "March"
            
            elif month == "04":
                month = "April"
            
            elif month == "05":
                month = "May"
                
            elif month == "06":
                month = "June"
                
            elif month == "07":
                month = "July"
                
            elif month == "08":
                month = "August"
            
            elif month == "09":
                month = "September"
            
            elif month == "10":
                month = "October"
            
            elif month == "11":
                month = "November"
            
            elif month == "12":
                month = "December" 
                
            
            print("\nYour converted date is: " + month + " " + day + ", " + year + ".")
            

main()

