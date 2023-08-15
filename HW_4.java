/* 
Leah Toutounjian
CSIS 112
Homework #4
Summer 2023
*/

import java.util.Scanner;
import java.text.DecimalFormat;

public class HW_4
{
   public static void main(String[]args)
   {
      Scanner keyboard = new Scanner(System.in);
      DecimalFormat formatter = new DecimalFormat("$#0.00") ;
      int treeHeight;
      int numTrees;
      int forDelivery;
      double singleTree = 0;
      double treeCost;
      double deliveryCost;
      double totalCost;
      
      System.out.println("How many trees do you want to purchase?");
      numTrees = keyboard.nextInt();
      
      System.out.println("Enter the height of trees you want to purchase.");
      treeHeight = keyboard.nextInt();
      
      System.out.println("Would you like the trees delivered? Enter 1 for Yes, Enter 0 for No.");
      forDelivery = keyboard.nextInt();
      
      if(treeHeight < 3)
       {
         singleTree = 39.00;
       }
      
      else if(treeHeight >= 3 && treeHeight <= 5) 
       {
         singleTree = 69.50;
       }
       
      else if(treeHeight > 5 && treeHeight < 8)
       {
         singleTree = 99.00;
       }
       
      else if(treeHeight > 8)
       {
         singleTree = 199.50;
       }
       
      treeCost = singleTree * numTrees;
       
      if(forDelivery == 1)
       {
         if(numTrees < 5)
          {
            deliveryCost = 10.00 * numTrees;
          }
          
         else
          {
            deliveryCost = 50.00;
          }
       }
            
      else
       {
         deliveryCost = 0.00;
       }

       totalCost = treeCost + deliveryCost;
       
      System.out.println("Green Fields Landscaping");
      System.out.println("Evergreen Tree Invoice");
      System.out.println(numTrees + " Trees at " + singleTree + "0 each: " 
                         + formatter.format(treeCost));
      System.out.println("Delivery Charge: \t " + formatter.format(deliveryCost));
      System.out.println("\t \t \t --------");
      System.out.println("TOTAL:\t\t\t" + formatter.format(totalCost));    
      }
}