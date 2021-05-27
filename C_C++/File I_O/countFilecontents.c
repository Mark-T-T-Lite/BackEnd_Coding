#include<stdio.h>  //defines FILE struct

 int main()
 {
     // Initiate File Opening
     FILE *fp;
     char ch, fileName[20];
     int nol=0, nos=0, nota=0, noc=0;

     printf("Input name of file to evaluate\n");
     gets(fileName);

     fp=fopen(fileName,"r");  //Access to open file's structure
     if(fp==NULL)
     {
         puts("Cannot Open or Find file.");
         return 1;
     }
      //Access Buffer
     while(1)
     {
         ch=fgetc(fp);  //Access first character in buffer through fp
         if(ch==EOF)
            break;

         noc++;
         if(ch==' ')
            nos++;

         if(ch=='\n')
            nol++;

         if(ch=='\t')
            nota++;
     }
     fclose(fp); //Close file
     //Report
     printf("Report On file:\t");
     puts(fileName);
     printf("\nNumber Of Characters In file:%d",noc);
     printf("\nNumber Of Spaces In file:%d",nos);
     printf("\nNumber Of Tabs In file:%d",nota);
     printf("\nNumber Of Newlines In file:%d",nol);

     return 0;
 }
