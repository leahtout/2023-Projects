# Leah Toutounjian
# HW5_1

def main():
    
    selection = 0
    groceryList = []
    
    while selection != "7":
        
        print("\n1.  Add an Item to the Grocery List")
        print("2.  Remove an Item from the Grocery List")
        print("3.  Sort the Grocery List (in alphabetical order)")
        print("4.  Search the List for an Item")
        print("5.  Change the Quantity of a List Item")
        print("6.  Print the List")
        print("7.  Quit the Program")
        
        selection = input("\nPlease make a selection: ")
        
        if selection == "1":
            
            itemName = str(input("\nPlease enter the name of the item: "))
            itemName = itemName.capitalize()
            itemQuantity = int(input("Please enter the quantity of the item: "))
            
            itemExists = None
            
            for item in groceryList:
                if item[0] == itemName:
                    itemExists = item
            
            if itemExists is None:
                bothItemAndQuantity = (itemName, itemQuantity)
                groceryList.append(bothItemAndQuantity)
                print("\nHere is your grocery list:", groceryList)
                
            else:
                print("\nError! This item already exists in the list!")      
                
        elif selection == "2":
            itemRemove = str(input("\nPlease enter the name of the item you wish to remove: "))
            itemRemove = itemRemove.capitalize()
        
            itemExists2 = None  #yes, i'm going to have multiple of the itemExists just in 1 2 3 form because why not lol
        
            for item in groceryList:
                if item[0] == itemRemove:
                    itemExists2 = item 
        
            if itemExists2 is not None:
                groceryList.remove(itemExists2)
                print("\nItem removed from your gorcery list!")
                
            else:
                print("\nError! This item does not exist in your list!")
        
            print("\nHere is your updated grocery list:",groceryList)        
                    
        elif selection == "3":
            
            groceryList.sort()
            print("\nHere is your sorted list: ",groceryList)
            
        elif selection == "4":
            
            itemSearching = str(input("\nPlease enter the name of the item you are searching for: "))
            itemSearching = itemSearching.capitalize()
        
            itemExists3 = None
        
            for item in groceryList:
                if item[0] == itemSearching:
                    itemExists3 = item
                    item = None
        
            if itemExists3 is not None:
                print("\n", itemSearching, "is in the grocery list!")
                
            else:
                print("\n" + itemSearching, "is not in the grocery list!") 
                     
        elif selection == "5":
                
            changeQuantity = input("\nPlease enter the name of the item you want to change the quantity of: ")
            changeQuantity = changeQuantity.capitalize()
            
            itemExists4 = None
            index = 0
            
            while index < len(groceryList):
                    
                item = groceryList[index]
                    
                if item[0] == changeQuantity and itemExists4 is None:
                    
                    newQuantity = int(input("Please enter the new quatity of the item: "))
                    groceryList[index] = (item[0], newQuantity)
                    itemExists4 = index
                    
                index = index + 1
                
                newQuantity = groceryList
            
                if itemExists4 is not None:
                    print("You updated your quantity for",item,". Here is your new grocery list:",newQuantity,".")
            
            print("\nItem is not in your grocery list!")  
            
        elif selection == "6":
            print("Your grocery list is:",groceryList)
            
        
        elif selection == "7":
            print("\nThank you for using this program!")
            print("You quit!")
            
            
        else:
            print("\nError! You entered an invalid selection. Please try again!")
          
main()
