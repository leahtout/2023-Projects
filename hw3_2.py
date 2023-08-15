# Leah Toutounjian
# HW3_1

import random

def main():
    
    selection = "a"
    
    while selection != "q" and selection != "Q":
        
        print("\n\tCOIN TOSS SIMULATION MENU")
        print("\t---------------------------")
        print("\ta)Simulate 100 Coin Tosses")
        print("\tq)Quit the program\n") 
        
        selection = input("\tPlease make a selection: ")
        
        if selection == "a":
            
            heads = 0
            tails = 0         
            
            for head_tail in range(100):
                head_tail = random.randint(0,1)
                
                if head_tail == 1:
                    heads = heads + 1
                    headsPercent = heads / 100.00
                    
                else:
                    tails = tails + 1
                    tailsPercent = tails / 100.00
                    
            
            print("\n\tCOIN TOSS STATISTICS")
            print("\tResult \t\t# Times    \t\t% Times")
            print("\t-------\t\t-----------\t\t-----------")
            print("\tHeads    \t\t",heads,f"\t\t{headsPercent:.2%}")
            print("\tTails    \t\t",tails,f"\t\t{tailsPercent:.2%}")            
        
        
        elif selection != "q":
            print("\n\tYou have made an invalid selection\n")
        
    
            
main()