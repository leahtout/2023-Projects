
import java.util.Scanner;
import java.text.DecimalFormat;

public class HW_8A
{
   public static void main(String[]args)
   {
      Scanner keyboard = new Scanner(System.in);
      DecimalFormat formatter = new DecimalFormat("#0.0");
      int firstScore;
      int secondScore;
      int thirdScore;
      int forthScore;
      int fifthScore;
      double average;
      double total;
      char letter1, letter2, letter3, letter4, letter5, averageLetter;
      
      System.out.println("Please enter the first score between 0 and 100: ");
      firstScore = keyboard.nextInt();
      
      while(firstScore < 0 || firstScore > 100)
      {
         System.out.println("You have entered an invalid test score.");
         System.out.println("Please enter the first score between 0 and 100: ");
         firstScore = keyboard.nextInt();
      }
      
      System.out.println("Please enter the second score between 0 and 100: ");
      secondScore = keyboard.nextInt();
      
      while(secondScore < 0 || secondScore > 100)
      {
         System.out.println("You have entered an invalid test score.");
         System.out.println("Please enter the second score between 0 and 100: ");
         secondScore = keyboard.nextInt();
      }
      
      System.out.println("Please enter the third score between 0 and 100: ");
      thirdScore = keyboard.nextInt();
      
      while(thirdScore < 0 || thirdScore > 100)
      {
         System.out.println("You have entered an invalid test score.");
         System.out.println("Please enter the third score between 0 and 100: ");
         thirdScore = keyboard.nextInt();
      }
      
      System.out.println("Please enter the forth score between 0 and 100: ");
      forthScore = keyboard.nextInt();
      
      while(forthScore < 0 || forthScore > 100)
      {
         System.out.println("You have entered an invalid test score.");
         System.out.println("Please enter the forth score between 0 and 100: ");
         forthScore = keyboard.nextInt();
      }
      
      System.out.println("Please enter the fifth score between 0 and 100: ");
      fifthScore = keyboard.nextInt();
      
      while(fifthScore < 0 || fifthScore > 100)
      {
         System.out.println("You have entered an invalid test score.");
         System.out.println("Please enter the fifth score between 0 and 100: ");
         fifthScore = keyboard.nextInt();
      }
      
      total = calcAverage(firstScore, secondScore, thirdScore, forthScore, fifthScore);
      
      average = total;
      
      letter1 = determineGrade(firstScore);
      letter2 = determineGrade(secondScore);
      letter3 = determineGrade(thirdScore);
      letter4 = determineGrade(forthScore);
      letter5 = determineGrade(fifthScore);
      averageLetter = determineGrade(average);
      
      System.out.println("The first letter grade is: " + letter1);
      System.out.println("The second letter grade is: " + letter2);
      System.out.println("The third letter grade is: " + letter3);
      System.out.println("The fourth letter grade is: " + letter4);
      System.out.println("The fifth letter grade is: " + letter5);
      System.out.println("\nThe average test score is: " + formatter.format(average));
      System.out.println("The average grade is " + averageLetter);
   }
   
   public static double calcAverage(double a, double b, double c, double d, double e)
   {
      return (a + b + c + d + e) / 5;
   }
   
   public static char determineGrade(double sc)
   {
      if(sc >= 90 && sc <= 100)
      {
         return 'A';
      }  
      
      if(sc < 90 && sc >=80)
      {
         return 'B';
      }
      
      else if(sc < 80 && sc >= 70)
      {
         return 'C';
      }
      
      else if(sc < 70 && sc >=60)
      {  
         return 'D';
      }
      
      else
      {
         return 'F';
      }
   }
}