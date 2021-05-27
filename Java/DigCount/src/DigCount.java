import java.util.Scanner;
public class DigCount{
	public static void main (String[] args){
int Sum1=0, a;
		while(true)
		{  Sum1=0;
			Scanner input = new Scanner(System.in);
			System.out.println("Input number for sum of digits");
  int  Numb=input.nextInt();
			while(Numb!=0){
				a=Numb%10;
				Numb/=10;
				Sum1+=a;
				
			}
			System.out.println("The sum of digits is" + Sum1);
		}
	}
}
