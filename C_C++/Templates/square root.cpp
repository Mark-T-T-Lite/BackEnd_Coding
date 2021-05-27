#include <iostream>
#include <cmath>

using namespace std;
int main(void){
float value,squareroot;
    cout<<"Input a number for spuare root computation please!"<<endl;
    cin>>value;
    if(value>=0){
    squareroot= sqrtf(value);
        cout<<"Your result\n"<<squareroot;
}
    else cout<<" Go read math!";
    return 0;
}