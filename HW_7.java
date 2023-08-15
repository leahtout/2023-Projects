
import java.util.Scanner;
import java.text.DecimalFormat;

public class HW_7
{
   public static void main(String[]args)
   {
      Scanner keyboard = new Scanner(System.in);
      DecimalFormat formatter = new DecimalFormat("#0");
      int Rooms = 0;
      int occupied = 0;
      int totalRooms = 0;
      int totalOccupied = 0;
      double percentage;
      int floors;
      
      System.out.println("Please enter the number of floors in the hotel: ");
      floors = keyboard.nextInt();
      
      while(floors < 1)
      {
         System.out.println("You have entered an invalid number of floors. ");
         System.out.println("Please enter the number of floors in the hotel: ");
         floors = keyboard.nextInt();
         
      }
      
      for(int counter = 1; counter <= floors; ++counter)
      {  
         if (counter != 13) {
           System.out.println("Please enter the number of rooms on floor #: " + counter);
           Rooms = keyboard.nextInt();
           
     
            while(Rooms < 10)
            {
               System.out.println("You have entered an invalid number of rooms. ");
               System.out.println("Please enter the number of rooms on floor #: " + counter);
               Rooms = keyboard.nextInt();
            }
           
           totalRooms = totalRooms + Rooms;
          
           System.out.println("Please enter the number of occupied rooms on floor #: " 
                              + counter);
           occupied = keyboard.nextInt();
           
           totalOccupied = occupied + totalOccupied;
         }
       
      }
      
      percentage =  (double)(totalOccupied)/(double)(totalRooms) * 100;
      System.out.println("\nThe hotel has a total of " + totalRooms + " rooms.");
      System.out.println(totalOccupied + " of the rooms are occupied.");
      System.out.println(formatter.format(percentage) + "% of the rooms are occupied.");

   }
}