# Leah Toutounjian
# HW5_3

import random

def main():
    
    selection = "0"
    
    rows = int(input("\nPlease enter the number of rows in the list: "))
    columns = int(input("Please enter the number of columns in the list: "))
    
    twoDimentionalList = []
    
    for r in range(rows):
        
            row = []
            
            for c in range(columns):
                
                randNum = random.randint(1, 20)
                row.append(randNum)
                
            twoDimentionalList.append(row)
            
    print("\nHere is your list:",twoDimentionalList)
    
    while selection != "5":
        
        print("\n1.  Sum a Row")
        print("2.  Sum the Corners")
        print("3.  Sum a Column")
        print("4.  Find a Number frequencey")
        print("5.  Quit the Program")
        
        selection = input("\nPlease make a selection: ")
        
        if selection == "1":
            
            rowNumber = int(input("\nPlease enter a row number: "))
            
            if rowNumber > rows or rowNumber < 1:
                
                print("\nInvalid row Number!")
                
            else:
                
                rowSumn = 0
                
                for nums in twoDimentionalList[rowNumber - 1]:
                    
                    rowSumn = rowSumn + nums
                
                print("\nThe sum of row",rowNumber,"is:",rowSumn)
                
        elif selection == "2":
            
            topLeft = twoDimentionalList[0][0]
            topRight = twoDimentionalList[0][-1]
            bottomLeft = twoDimentionalList[-1][0]
            bottomRight = twoDimentionalList[-1][-1]
            
            sumOfFourCorners = topLeft + topRight + bottomLeft + bottomRight            
            
            print("\nThe sum of the four corners is:",sumOfFourCorners)
            
            sumOfFourCorners = 0
            
        elif selection == "3":
            
            columnNumber = int(input("\nPlease enter a column number: "))
            
            if columnNumber > columns or columnNumber < 1:
                
                print("\nError! Invalid column Number!")
                
            else:
                
                columnSum = 0
                
                for nums in twoDimentionalList:
                    
                    columnSum = columnSum + nums[columnNumber - 1]
                   
                print("\nThe sum of column",columnNumber,"is:",columnSum)
            
        elif selection == "4":
            
            randomNumInput = int(input("\nPlease enter a random number between the range 1-20: "))
                                 
            while randomNumInput < 1 or randomNumInput > 20:
                
                print("\n    Error! Invalid input. Please try again.")
                randomNumInput = int(input("\nPlease enter a random number between the range 1-20: "))

            numTimesInList = 0
                
            for row in twoDimentionalList:
                    
                for values in row:
                        
                    if values == randomNumInput:
                            
                        numTimesInList += 1
                
            print("\nThe number",randomNumInput,"is in the list",numTimesInList,"times.")
            
            numTimesInList = 0 

        elif selection == "5":
            
            print("\nYou quit the program!")
        
        else:
            
            print("\nError! Invalid selection! Please try again.")

main()



