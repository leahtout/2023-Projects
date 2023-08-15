

import java.util.Scanner;
import java.text.DecimalFormat;

public class HW_5
{
   public static void main(String[]args)
   {
      Scanner keyboard = new Scanner(System.in);
		DecimalFormat formatter = new DecimalFormat("0.0000");
      int choice;
      double radius = 0;
      double circumference;
      double area;
      
      System.out.println("CIRCLE CALCULATOR MENU");
      System.out.println("1) Calculate the Area of a Circle");
      System.out.println("2) Calculate the Circumference of a Circle");
      System.out.println("3) Quit the Program\n");
      System.out.println("Make a selection by choosing a number: ");
      choice = keyboard.nextInt();
      
      if(choice == 1 || choice == 2)
		{
			System.out.println("Please enter the radius of the circle: ");
			radius = keyboard.nextDouble();
		}
      
      switch(choice)
      {
        case 1:
    
         area = Math.PI * radius * radius;
         System.out.println("The area of the circle with radius " 
                            + radius + " is: " + formatter.format(area));
         break;
        
        case 2:
        
         circumference = 2 * radius * Math.PI;
         System.out.println("The circumference of the circle with radius " 
                            + radius + " is: " + formatter.format(circumference));
         break;
        
        case 3:
        
         System.out.println("You have chosen to quit the program.");
         break;
         
        default:
        
         System.out.println("You have made an invalid selection.");
        }
   }
}