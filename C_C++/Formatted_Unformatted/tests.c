#include<stdio.h>
int main()
{
   /* //Formatted functions

    char surname1[]="MARK",Surname2[]="Paul";
    char surname3[]="Aarom",Surname4[]="Moses";
    printf ( "\n%20s %20s", surname1,Surname2 ) ;
    printf ( "\n%-20s %-20s\a", surname3,Surname4 ) ;
    */
    //sprintf and sscanf
  /*   int i=10;
    char ch='A',str[20];
    float a = 3.14;
    printf("\n%4d %4c %4f ",i,ch,a);
    sprintf(str,"%2d%2c%2.3f ",i,ch,a);
    printf("\n%2s",str);
    sscanf("Hello","%10s",str);
    printf("\n%2s",str);
*/

//UnFormatted Functions
//GETCH,...
  /*  char  ch ;

    printf ( "\nPress any key to continue" ) ;
    getch( ) ;  // will not echo the character

    printf ( "\nType any character" ) ;
    ch = getche( ) ;  // will echo the character typed

    printf ( "\nType any character" ) ;
    getchar( ) ;  // will echo character, must be followed by enter key
    printf ( "\nContinue Y/N" ) ;
    fgetchar( ) ;  // will echo character, must be followed by enter key
*/
//PUTCH..

    char ch='B';
    putch(ch);
    putch('A');
    fputchar(ch);
    fputchar('A');
    putchar(ch);
    putchar('A');
    return 0;
}
