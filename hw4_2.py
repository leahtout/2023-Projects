# Leah Toutounjian
# HW4_2


def main():
    
    inventory = ()
    selection = "a"
    index = -1

    inventory = (
        (".-"), ("-..."), ("-.-."), #this third is letters A-Z in order
        ("-.."), ("."),("..-."),
        ("--."),("...."), (".."), 
        (".---"),("-.-"), (".-.."), 
        ("--"), ("-."),("---"), 
        (".--."), ("--.-"), (".-."), 
        ("..."),("-"), ("..-"),
        ("...-"),(".--"), ("-..-"),
        ("-.--"), ("--.."),
   
        ("-----"), #this third is numbers 0-9 in order
        (".----"), ("..---"), ("...--"), 
        ("....-"), ("....."),("-...."), 
        ("--..."), ("---.."),("----."),
   
        (" "), ("..--.."), (".-.-.-"),
        ("--..--")
        )        
    
    characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 ?.,"
    
    while selection != "q" and selection != "Q":
        print("\nMORSE CODE CONVE?RTER MENU")
        print("---------------------------")
        print("a) Enter a String to convert")
        print("q) Quit the program")
      
        selection = input("\nPlease make a selection: ")
        
        while selection != "a" and selection != "q":
            print("Invalid selection. Please try again!")
            selection = input("\nPlease make a selection: ")
            
        if selection == "a" or selection == "A":
            
            morseCode = ""
            
            words = str(input("Please enter a word: "))
            words = words.upper()
                     
            while words == False:
                print("\nInvalid Input. Try Again!")
                words = str(input("Please enter a word: "))
                words = words.upper()
                words = words.isalnum()    
            
            for word in words:
                index = characters.index(word)
                if index >= 0:
                    morseCode = morseCode + inventory[index] + " "            
                
            print("\nThe morse code for the word(s) " + words + " is: " + morseCode) 
            #BTW, when you put outputted morse code into another online converter, it doesn't show the space because you need to add "/" in the
            #online versions converter. However, in my code you can see it very clearly! (:
            
main()