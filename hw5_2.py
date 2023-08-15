# Leah Toutounjian
# HW5_2


def main():
    
    index = 0 
    totalSales = 0
    averageSales = 0
    largestSalesAmount = 0
    smallestSalesAmount = 0
    
    Monday = int(input("Enter the store sales figures for Monday: "))
    Tuesday = int(input("Enter the store sales figures for Tuesday: "))
    Wednsday = int(input("Enter the store sales figures for Wednsday: "))
    Thursday = int(input("Enter the store sales figures for Thursday: "))
    Friday = int(input("Enter the store sales figures for Friday: "))
    Saturday = int(input("Enter the store sales figures for Saturday: "))
    Sunday = int(input("Enter the store sales figures for Sunday: "))
    
    weekSales = [Monday, Tuesday, Wednsday, Thursday, Friday, Saturday, Sunday]
    
    for sales in weekSales:
        totalSales += sales
        averageSales = totalSales / 7
        weekSales.sort()
        smallestSalesAmount = weekSales[0]
        largestSalesAmount = weekSales[6]
        
    print("\nSTORE WEEKLY RESULTS")
    print("--------------------")
    print("The total sales for this week was",totalSales,"sales.")
    print(f"The average sales for this week was {averageSales:,.0f} sales.")
    print("The largest sales amount for this week was",largestSalesAmount,"sales.")
    print("The smallest sales amount for this week was",smallestSalesAmount,"sales.")
    
    
main()