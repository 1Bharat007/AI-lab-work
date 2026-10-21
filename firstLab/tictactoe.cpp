// tic tac toe game
#include <iostream>
using namespace std;

void board(char a[])

{
    printf(" %c | %c | %c \n", a[0], a[1], a[2]);
    printf("---+----+--\n");
    printf(" %c | %c | %c \n", a[3], a[4], a[5]);
    printf("---+----+--\n");
    printf(" %c | %c | %c \n", a[6], a[7], a[8]);
    printf("---+----+--\n");

}

int main() {
    char a[] = {' ',' ',' ',' ',' ',' ',' ',' ',' '};

    
    cout << "Welcome to Tic Tac Toe" << endl;
    board(a) ;


    while(1)
    {
        int x ;
        cout<<"enter the position of x" ;
        cin>>x;

        if(a[x-1] == ' ')
        {
            a[x-1] = 'x' ;
        }
        else
        {
            cout<<"position is already filled" ;
            continue ;
        }
        board(a) ;

        if(a[0] == a[1] && a[1] == a[2])
        {
            cout<< "player 1 is winner" ;
           break ;
        }
        else if(a[0] == a[3] && a[3] == a[6])
        {
            cout<< "player 1 is winner" ;
        }
        else if(a[0]==a[])


        
    }



    return 0;
}