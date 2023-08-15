

import java.util.Scanner;
import java.text.DecimalFormat;

public class HW_7B
{
   public static void main(String[]args)
   {
      Scanner keyboard = new Scanner(System.in);
      DecimalFormat formatter = new DecimalFormat("$#,##0.00");
      int numDaysWorked = 0;
      double pay = 1;
      int num = 0;
      double totalPay = 0;
      
      System.out.println("Please enter the number of days you worked: ");
      numDaysWorked = keyboard.nextInt();
      
      while(numDaysWorked < 1)
      {
         System.out.println("You have entered an invalid number of days.");
         System.out.println("Please enter the number of days you worked: ");
         numDaysWorked = keyboard.nextInt();
      }
      
      for(int counter = 1; counter<=numDaysWorked; ++counter)
      {
         System.out.println("Pay for day #" + counter + ": " + formatter.format(pay));
         totalPay += pay;
         pay = pay * 2;
      }
      
      
      System.out.println("\nTOTAL PAY FOR " + numDaysWorked + " DAYS: " + formatter.format(totalPay));
    }
}