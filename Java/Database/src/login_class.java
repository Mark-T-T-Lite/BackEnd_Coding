class passWord{
	
	public boolean auth_method(String Name,int key){
		
       if(key==1){
		System.out.println("Hello " + Name);
		return false;
		}
		else{
			System.out.println(" Wrong password");
			return true;
		}
		
		}
}
