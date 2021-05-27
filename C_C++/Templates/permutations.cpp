// For each letter in a,b,c we can create 2 combinations hence 3*2

#include<iostream>
using namespace std;

template<class T>
inline void Swap(T& a,T& b){
    //Swap a and b
        T temp = a; a=b; b=temp;
}
template<class T>
void Perm(T list[], int k, int m){
  //Generates all permutations of list[k:m].
    int i;
    if(k == m){
        // output a permutation
        for(i = 0; i <= m; i++)
          cout<<list[i];
        cout << endl;
    }
    else {// list [k:m] has more than one permutation
    //generate these recursively
    for(i = k; i<=m; i++){
        Swap(list[k],list[i]);
        Perm(list,k+1,m);
        Swap(list[k],list[i]);
    }

               }
}

int main(){
    char list[] = {'a','b','c'};
    Perm(list,0,2);
    return 0;
}
