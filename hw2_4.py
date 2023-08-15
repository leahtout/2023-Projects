# Leah Toutounjian
# HW2_4

def main():
    
    vegetarian = input("Is anyone in your party a vegetarian? ")
    vegan = input("Is anyone in your party a vegan? ")
    glutenFree = input("Is anyone in your party gluten free? ")
    
    print("Here are your restaurant choices:")
    
    if vegetarian == "yes" and vegan == "yes" and glutenFree == "yes":
        print("Corner Cafe")
        print("Chef's Kitchen")
        
    elif vegetarian == "yes" and vegan == "no" and glutenFree == "yes":
        print("Main Street Pizza")
        print("Corner Cafe")
        print("Chef's Kitchen")
        
    elif vegetarian == "yes" and vegan == "yes" and glutenFree == "no":
        print("Corner Cafe")
        print ("Chef's Kitchen")
        
    elif vegetarian == "no" and vegan == "yes" and glutenFree == "yes":
        print("Corner Cafe")
        print("Chef's Kitchen")
        
    elif vegetarian == "no" and vegan == "yes" and glutenFree == "no":
        print("Corner Cafe")
        print("Chef's Kitchen")
    
    elif vegetarian == "yes" and vegan == "no" and glutenFree == "no":
        print("Mama's Fine Italian")
        print("Main Street Pizza")
        print("Corner Cafe")
        print("Chef's Kitchen")   
        
    elif vegetarian == "no" and vegan == "no" and glutenFree == "no":
        print("Joe's Gourmet Butgers")
        print("Mama's Fine Italian")
        print("Main Street Pizza")
        print("Corner Cafe")
        print("Chef's Kitchen")
        
    elif vegetarian == "no" and vegan == "no" and glutenFree == "yes":
        print("Main Street Pizza")
        print("Corner Cafe")
        print("Chef's Kitchen")
        
main()