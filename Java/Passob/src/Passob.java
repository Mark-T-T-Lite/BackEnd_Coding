class Block{
	int a,b,c, volume;

	Block(int i, int j, int k){
		a=i;
		b=j;
		c=k;
		volume=a*b*c;

	}
	//return true if ob defines same block
	boolean sameBlock(Block ob){
		if((ob.a==a) & (ob.b==b) & (ob.c==c)) return true;
		else return false;
	}
	//return true if ob has same volume
	boolean sameVolume(Block ob){
		if(ob.volume==volume) return true;
		else return false;
	}
	}
	 class Passob{
		public static void main(String[] args){
			Block ob1= new Block(10,15,2);
			Block ob2= new Block(10,15,2);
			Block ob3= new Block (2,3,4);

			System.out.println("ob1 same dime as ob2 ?" + ob1.sameBlock(ob2));
			System.out.println("ob1 same volume as ob2 ?" + ob1.sameVolume(ob2));
			System.out.println("ob1 same as ob2 ?" + ob1.sameBlock(ob3));
		}
	}
