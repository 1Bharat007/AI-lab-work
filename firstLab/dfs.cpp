//  rock paper scissor  game 

#include<iostream>
#include<ctime>
#include<cstdlib>
#include<string.h>
// #include<boolean>
using namespace std ;
int main()
{ 
    bool s = true ;
    string choice = "" ;
    while(s)
{
    cout<<"select rock , paper , scissor" << endl ;
cin>>choice ;
    int randnumber = (time(nullptr)) ;
     if(choice == "rock" && randnumber%3 == 1)
     cout<<"computer is winner" ;
     else if(choice == "paper" && randnumber%3 == 2)
     cout<<"computer is winner" ;
     else if(choice == "rock")
     cout<< "You are winner" ;
     else if(choice == "scissor" && randnumber%3 ==0)
     cout<<"computer is winner" ;
     else 
     cout<<"you are winner" ;

     cout<<endl;
     cout<< "write exit to end the game" ;
     string entry = "" ;
     cin>> entry ;
     if(entry == "exit") 
     break ;


}
    return 0 ;
}