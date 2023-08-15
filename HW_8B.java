
import java.util.Scanner;
import java.text.DecimalFormat;

public class HW_8B
{
   public static void main(String[]args)
   {
      Scanner keyboard = new Scanner(System.in);
      DecimalFormat formatter = new DecimalFormat("##0.0000");
      int selection = 0;
      double meters = 0;
      double kilometers;
      double inches;
      double feet;
      
      do
      {
         showMenu();
         System.out.println("Please make a selection: ");
         selection = keyboard.nextInt();
         
         if (selection >= 1 && selection < 4) 
         {
            System.out.println("Please enter the number of meters you want to convert: ");
            meters = keyboard.nextDouble();
         }
            
         while (meters < 0) 
         {
             System.out.println("Invalid entry.");
             System.out.println("Please enter a positive number: ");
             meters = keyboard.nextDouble();
         }

         switch (selection) 
         {
            case 1:
            
                kilometers = calcKilometers(meters);
                System.out.println(meters + " meters is " + formatter.format(kilometers) + " kilometers.");
                break;
                
            case 2:
            
                inches = calcInches(meters);
                System.out.println(meters + " meters is " + formatter.format(inches) + " inches.");
                break;
                
            case 3:
            
                feet = calcFeet(meters);
                System.out.println(meters + " meters is " + formatter.format(feet) + " feet.");
                break;
                
            case 4:
            
               break;
               
            default:
            
               System.out.println("Invalid selection.");
               break;
               
        }
      
      }while(selection !=4);
  }
    
   
   public static void showMenu()
    {
      System.out.println("\nMETER CONVERSION");
      System.out.println(" 1) Convert to Kilometers");
      System.out.println(" 2) Convert to Inches");
      System.out.println(" 3) Convert to Feet");
      System.out.println(" 4) Quit the Program");
    }
    
   public static double calcKilometers(double m1)
   {
      return m1 * 0.001;
   }
   
   public static double calcInches(double m1)
   {
      return m1 * 39.37;
   }
   
   public static double calcFeet(double m1)
   {
      return m1 * 3.281;
   }
}