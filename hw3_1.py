# Leah Toutounjian
# HW3_1

def main():
    
    amountSpent = 1
    totalSpent = 0
    totalOver = 0
    totalUnder = 0
    
    amountBudgeted = int(input("Enter amount budgeted for the month: "))
    
    while amountBudgeted < 0:
        print("Budgeted amount can not be negative.  Try again")
        
        amountBudgeted = int(input("Enter amount budgeted for the month: "))
        
    while amountSpent != 0:
        
        amountSpent = int(input("Enter an amount spent(0 to quit): "))
        
        while amountSpent < 0:
            print("Amount spent can not be negative.  Try again")
            
            amountSpent = int(input("Enter an amount spent(0 to quit): "))
            
        totalSpent = amountSpent + totalSpent

    if amountSpent == 0:
        
        print(f"Budgeted: ${amountBudgeted:,.2f}")
        
        print(f"Spent: ${totalSpent:,.2f}")
        
        if totalSpent > amountBudgeted:
            
            totalOver = totalSpent - amountBudgeted
            
            print(f"You are ${totalOver:,.2f} over budget. PLAN BETTER NEXT TIME!")
            
        elif totalSpent == amountBudgeted:
            
            print("Spending matches budget. GOOD PLANNING!")
        
        else:
            totalUnder = amountBudgeted - totalSpent
            
            print(f"You are ${totalUnder:.2f} under budget. WELL DONE!")
            
    
main()