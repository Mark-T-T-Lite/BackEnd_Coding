#include<stdio.h>

int main()
 {
   FILE *fp;
   char ch='Y',fileName[20];

   struct employee
   {
       char name[40];
       int age;
       float bs;
    }e;

    printf("Input name of file to Write\n");
    gets(fileName);

  fp=fopen(fileName,"wb");
  if(fp==NULL)
  {
      puts("Cannot Open or Find ");
         puts(fileName);
         return 1;
  }
  while(ch=='Y')
  {
      printf ( "\nEnter name, age and basic salary: " ) ;
      scanf ( " %s %d %f", e.name, &e.age, &e.bs ) ;
      fwrite(&e,sizeof(e),1,fp) ;

      printf ( "Add another record (Y/N) " ) ;
      fflush ( stdin ) ;
      ch = getche( ) ;
   }
  fclose(fp);
  return 0;
 }
