/* Read records from a file using structure */
#include<stdio.h>
int main( )
{
    FILE  *fp ;
    char  fileName[20];

    struct employee
    {
        char  name[40] ;
        int  age ;
        float  bs ;
    }  e ;


     printf("Input name of record to read\n");
     gets(fileName);

   fp = fopen ( fileName, "r" ) ;

 if(fp==NULL)
     {
         puts("Cannot Open or Find ");
         puts(fileName);
         return 1;
     }

 while ( fscanf ( fp, "%s %d %f", e.name, &e.age, &e.bs ) != EOF )
    printf ( "\n%s %d %f", e.name, e.age, e.bs ) ;

 fclose ( fp ) ;
}
