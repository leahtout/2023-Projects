/*
Leah Toutounjian
CSIS 112
Exam #2
Summer 2023
*/

import java.util.Scanner;
import java.text.DecimalFormat;

public class Exam_2
{
   public static void main(String[]args)
   {
      Scanner keyboard = new Scanner(System.in);
      DecimalFormat formatter = new DecimalFormat("$#0.00");
      int lawnSizeFeet;
      int weeksMowed;
      double totalMowCost;
      double weeklyMowingFee;
      double serviceCharge;
      int selection = 0;
      int selection2 = 0;
      double totalCost;
      
    do{
    
      displayMenu();
      
      System.out.println("\nPlease make a selection: ");
      selection = keyboard.nextInt();
      
      switch(selection)
      {
         case 1:
           System.out.println("What is the size of the lawn in square feet?");
           lawnSizeFeet = keyboard.nextInt();
           
           while(lawnSizeFeet < 0)
           {
              System.out.println("You cannot enter a negative number.");
              System.out.println("What is the size of the lawn in square feet?");
              lawnSizeFeet = keyboard.nextInt();
           }
           
           System.out.println("How many weeks would you like your lawn to be mowed for?");
           weeksMowed = keyboard.nextInt();
           
           System.out.println("Will you pay for services in advance or weekly? Enter 1 for in advance or 2 for weekly.");
           selection2 = keyboard.nextInt();
           
           if(selection2 == 1)
           {
              serviceCharge = 0.00;
           }                      
                   
           else
           {
              serviceCharge = calcServiceCharge(weeksMowed);
           }            
           
           weeklyMowingFee = calcWeeklyMowFee(lawnSizeFeet);
           
           totalMowCost = calcTotalMowCost(weeklyMowingFee, weeksMowed);
           
           totalCost = totalMowCost + serviceCharge;
           
           System.out.println("LISA'S LAWN MOWING SERVICE - INVOICE");
           System.out.println("-----------------------------------------");
           System.out.println("Size of Lawn:      " + lawnSizeFeet);
           System.out.println("Number of Weeks:   " + weeksMowed);
           System.out.println("Weekly Mowing Fee: " + formatter.format(weeklyMowingFee));
           System.out.println("\nTotal Mowing Fee:   " + formatter.format(totalMowCost));
           System.out.println("Service Charge:     " + formatter.format(serviceCharge));
           System.out.println("                    --------");
           System.out.println("TOTAL COST:       " + formatter.format(totalCost));
           
           break;
           
           case 2:
           
           System.out.println("You chose to quit the program!");
           break;
           
           default:
           
           System.out.println("Invalid Selection.");
           break;
      }
      
     }while(selection != 2);
     
   }
   
   public static void displayMenu()
   {
      System.out.println("\nLAWN MOWING INVOICE GENERATOR");
      System.out.println("1)Calculate and Display Invoice");
      System.out.println("2)Quit Program");
   }
   
   public static double calcWeeklyMowFee(double a)
   {
      if(a < 350)
      {
         return 20.00;
      }
      
      else if(a >= 350 && a < 550)
      {
         return 30.00;
      }
      
      else if(a >= 550)
      {
         return 40.00;
      }
      
      else
      {
         return 0.00;
      }
   }
   
   public static double calcTotalMowCost(double a, double b)
   {
      return a * b;
   }
   
   public static double calcServiceCharge(double a)
   {
      return a * 1.20;
   }
}   
