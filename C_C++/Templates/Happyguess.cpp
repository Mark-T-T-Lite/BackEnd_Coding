#include <iostream>

using namespace std;
int main(void){
    char a;
    while(1){
    cout<<"HAPPY GUESS v1.01"<<endl<<"WELCOME TO HAPPY GUESS"<<endl<<"Its for letters, and numbers"<<endl<<"Guess Boy! GUESS"<<endl;
        cin>>a;
       
        if(a==120){
            cout<<"You did it!";
            break;
        }
        else
        cout<<"FAILED"<<endl<<endl<<"TRY AGAIN BOY"<<endl;
    
}
        return 0;
    }