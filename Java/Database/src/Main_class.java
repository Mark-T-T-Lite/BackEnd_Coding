import java.util.*;
import passWord.*;
public class Main
{
	public static void main(String[] args)
	{
		boolean pass= true;
		while(pass){
			passWord u1 = new passWord();
		Scanner input = new Scanner(System.in);

		System.out.print("Enter your name ");
		String userName1 = input.next();

		System.out.print("Enter second number: ");
		int passWord1 = input.nextInt();

		pass=u1.auth_method(userName1,passWord1);
	}
	}
}