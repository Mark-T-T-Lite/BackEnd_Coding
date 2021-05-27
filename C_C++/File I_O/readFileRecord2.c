//ead records from a file using structure
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
    } ;
    struct employee e;

     printf("Input name of record to read\n");
     gets(fileName);

   fp = fopen ( fileName, "rb" ) ;

 if(fp==NULL)
     {
         puts("Cannot Open or Find ");
         puts(fileName);
         return 1;
     }
fflush(stdin);
 while ( fread(&e,sizeof(e),1,fp)==1)
    printf ("\n%s %d %f", e.name, e.age, e.bs ) ;

 fclose ( fp ) ;
 return 0;
 }

