/* 
Leah Toutounjian
CSIS 112
Programming Exam #1
Summer 2023
*/

import java.util.Scanner;
import java.text.DecimalFormat;

public class Exam_1
{
   public static void main(String[]args)
   {
      Scanner keyboard = new Scanner(System.in);
		DecimalFormat formatter = new DecimalFormat("$#0.00");
      int selection;
      String name = ""; //use "" to initialize a STRING. cannot use 0 as that is an 
                          //integer, therefore you must use the "". 
      int minutesUsed = 0;
      double baseCost = 0;
      double excessMinutesCost = 0;
      double totalCost = 0;
      int excessMinutes = 0;
      
      System.out.println("CELLPHONE BILL GENERATOR");
      System.out.println("-----------------------------");
      System.out.println("1) PLAN 1: 500 Minute Plan");
      System.out.println("2) PLAN 2: Unlimited Minute Plan");
      System.out.println("3) Quit the program");
      System.out.println("Please make a selection: ");
      selection = keyboard.nextInt();
      keyboard.nextLine();
      
      if(selection == 1 || selection == 2)
		{
			System.out.println("Please enter your name: ");
			name = keyboard.nextLine();
		}
     
      
      switch(selection)
      {
         case 1:
         
            System.out.println("How many minutes did you use this month?");
            minutesUsed = keyboard.nextInt();
            
            baseCost = 24.99;
            
            excessMinutes = minutesUsed - 500;
            excessMinutesCost = (excessMinutes * .18);
            
            totalCost = baseCost + excessMinutesCost;
            break;
         
         case 2:
         
            baseCost = 59.99;
            
            excessMinutesCost = 0;
            
            totalCost = baseCost + excessMinutesCost;
            
            break;
            
         case 3:
         
            System.out.println("Thank you for using the program! You quit the program.");
            break;
         
         default:
         
            System.out.println("You have made an invalid selection.");
      }
      
      if(minutesUsed <= 500)
      {
         excessMinutes = 0;
         excessMinutesCost = 0;
         totalCost = baseCost;
      }
      
      if(selection == 1 || selection == 2)
		{
			System.out.println("\nCELL PHONE BILL");
         System.out.println("CUSTOMER:  " + name);
         System.out.println("-------------------------");
         System.out.println("Base Cost:              " + formatter.format(baseCost));
         System.out.println(excessMinutes + " Extra Minutes:      "
                            + formatter.format(excessMinutesCost));
         System.out.println("                        --------");
         System.out.println("TOTAL COST:             " + formatter.format(totalCost));
         
		}
   }
}