#include <iostream>
#include <stdio.h>

using namespace std;

int main(void){

    double a,b,ans;
    char choice;

    while(1){
    
        cout<<" Welcome to Baby Calc v1.01"<<endl<<"For Babies such as Moses and Aaron"<<endl;
        cout<<endl<<"Give the numbers to either add,subtract,divide or multiply"<<endl<<endl;
        cout<<"Input first number"<<endl;
        cin>>a;
       
        cout<<endl<<"Choose:"<<endl<<"a for add"<<endl<<"s for subtract"<<endl<<"d for divide"<<endl<<"m for multiply"<<endl<<endl;
        cin>>choice;
        cout<<"Input second number"<<endl;
        cin>>b;
        
        if(choice=='a'){
            ans=a+b;
            cout<<endl<<"You asked for"<<endl<< a<<"+"<<b<<"="<<ans<<endl;
        }
        if(choice=='s'){
            ans=a-b;
            cout<<endl<<"You asked for"<<endl<< a<<"-"<<b<<"="<<ans<<endl;
        }
        
        if(choice=='m'){
            ans=a*b;
            cout<<endl<<"You asked for"<<endl<< a<<"*"<<b<<"="<<ans<<endl;
        }
        if(choice=='d'){
            ans=a/b;
            cout<<endl<<"You asked for"<<endl<< a<<"/"<<b<<"="<<ans<<endl;
        }
      cout<<endl<<endl;
}
    return 0;
}