import java.util.Scanner;
import java.util.*;
public class DigCount{
	public static void main (String[] args){
int Sum1=0 , a;
		while(true)
		{  
			Scanner input = new Scanner(System.in);
			System.out.println("Input number for sum of digits");
  int  Numb=input.nextInt();
			System.out.println("Input number of digits");
			int b=input.nextInt();
			for(int count=0;count<b;count++){
				a=Numb%10;
				Numb/=10;
				Sum1+=a;
				
			}
			System.out.println("The sum of digits is" + Sum1);
		}
	}
}
