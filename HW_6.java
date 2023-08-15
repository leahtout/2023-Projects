
import java.util.Scanner;
import java.text.DecimalFormat;

public class HW_6
{
   public static void main(String[]args)
   {
      Scanner keyboard = new Scanner(System.in);
      DecimalFormat formatter = new DecimalFormat("$#0.00") ;
      int choice;
      double totalSales = 0;
      
      
      do
      {
         System.out.println("\nBOOK CLUB MEMBERSHIP MENU");
         System.out.println("1) Sell a Six Month Membership");
         System.out.println("2) Sell a Twelve Month Membership");
         System.out.println("3) Quit the Program");      
         System.out.println("\nMake a selection by choosing a number: ");
         
         choice = keyboard.nextInt();
         
         switch(choice)
         {
            case 1:
            
            totalSales = totalSales + 50.50;
            System.out.println("You sold a six month membership.");
            break;
            
            case 2:
            
            totalSales = totalSales + 99.00;
            System.out.println("You sold a 12 month membership.");
            break;
            
            case 3:
            
            System.out.println("The total book club membership sales were " 
                                + formatter.format(totalSales));
            break;
                          
            
            default:
            
            System.out.println("You have made an invalid selection.");
            break;
         }
      
      }while(choice != 3); 
    }
}