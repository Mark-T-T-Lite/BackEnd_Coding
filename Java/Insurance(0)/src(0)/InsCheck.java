import java.util.Scanner;
class InsCheck
{
	public static void main(String[] args)
	{
      int health, age, location, sex;
		Scanner input = new Scanner(System.in);
		while (true)
		{
			System.out.println("INSURANCE CHECKPOINT");
			
			System.out.println("We check whether you should be insured by Premium InsuranceLtd");
			System.out.println("Choose an appropriate letter");
			System.out.println("WHAT IS YOUR HEALTH \n 1.Excellent \t\t\t 2.Poor ");
			health = input.nextInt();
			System.out.println("WHAT IS YOUR AGE \n 1.Below 25 years \t\t\t 2.Between 25 and 35 years \t\t\t  3. Above 35 years");
			age = input.nextInt();
			System.out.println("WHAT IS YOUR LOCATION \n 1.City \t\t\t 2.Village ");
			location = input.nextInt();
			System.out.println("WHAT IS YOUR SEX \n 1.Male \t\t\t 2.Female");
			sex = input.nextInt();

		      gauge:{
				if ((health == 1) && (age == 2) && (location == 1) && (sex == 1))
				{
					System.out.println("You are eligible for \n \t Premium rate: Rs.4/thousand \t\t\t Max Policy Amt: Rs 2 lakhs");
					break gauge;
					
				}
				if ((health == 1) && (age == 2) && (location == 1) && (sex == 2))
				{
					System.out.println("You are eligible for \n \t Premium rate: Rs.3/thousand \t\t\t Max Policy Amt: Rs 1 lakhs");
					break gauge;
				}

				if ((health == 2) && (age == 2) && (location == 2) && (sex == 1))
				{
					System.out.println("You are eligible for \n \t Premium rate: Rs.6/thousand \t\t\t Max Policy Amt: Rs 10000");
				break gauge;
				}
				
				System.out.println("Sorry, but you are not eligible for Insurance");
			}
		}
	}
}
