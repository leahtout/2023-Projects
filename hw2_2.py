# Leah Toutounjian
# HW2_2

def main():
    pocketNum = int(input("Enter a pocket number from 0 to 36: "))
    
    if pocketNum == 0:
        print("Green")
    
    elif pocketNum >= 1 and pocketNum <= 10:
        
        if pocketNum % 2 == 0:
            print("Black")
        
        else:
            print("Red")
    
    
    elif pocketNum >= 11 and pocketNum <= 18:
        
        if pocketNum % 2 == 0:
            print("Red")
            
        else:
            print("Black")
    
    elif pocketNum >= 19 and pocketNum <= 28:
        
        if pocketNum % 2 == 0:
            print("Black")
            
        else: 
            print("Red")
            
    elif pocketNum >= 29 and pocketNum <= 36:
        
        if pocketNum % 2 == 0:
            print("Red")
            
        else: 
            print("Black")     

    else:
        print("Error: Invalid input")


main()