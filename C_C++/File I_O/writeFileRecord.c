/*#include<stdio.h>

int main()
 {
   FILE *fp;
   char ch='Y',fileName[20];

   struct employee
   {
       int age;
       char name[40];
       float bs;
    }e;

    printf("Input name of file to Write\n");
    gets(fileName);

  fp=fopen(fileName,"w");
  if(fp==NULL)
  {
      puts("Cannot Open or Find ");
         puts(fileName);
         return 1;
  }
  while(ch=='Y')
  {
      printf ( "\nEnter name, age and basic salary: " ) ;
      scanf ( "%s %d %f", e.name, &e.age, &e.bs ) ;
      fprintf ( fp, "%s %d %f\n", e.name, e.age, e.bs ) ;

      printf ( "Add another record (Y/N) " ) ;
      fflush ( stdin ) ;
      ch = getche( ) ;
   }
  fclose(fp);
 }
*//* Reads records from binary file and displays them on VDU */
 #include "stdio.h"
 main( )
  {
      FILE  *fp ;
      struct emp   {   char  name[40] ;   int  age ;   float  bs ;   } ;
      struct emp  e ;

 fp = fopen ( "EMP.txt", "rb" ) ;

 if ( fp == NULL )  {   puts ( "Cannot open file" ) ;  return 1;}

 while ( fread ( &e, sizeof ( e ), 1, fp ) == 1 )   printf ( "\n%s %d %f", e.name, e.age, e.bs ) ;

 fclose ( fp ) ; }
