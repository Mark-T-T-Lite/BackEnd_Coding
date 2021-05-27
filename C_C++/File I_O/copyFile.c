
#include<stdio.h>

int main()
{
    FILE *sf,*tf;
    char ch, fileName[20];

     printf("Input name of file to Read\n");
     gets(fileName);

     sf=fopen(fileName,"r");  //Access to open file's structure
     if(sf==NULL)
     {
         puts("Cannot Open or Find ");
         puts(fileName);
         return 1;
     }
     printf("Input name of file to Write\n");
     gets(fileName);

     tf=fopen(fileName,"w");  //Access to open file's structure
     if(tf==NULL)
     {
         puts("Cannot Open or Find ");
         puts(fileName);
         return 1;
     }

    while(1)
    {
        ch=fgetc(sf);  //Access Structure,access buffer first character.
        if(ch==EOF)
            break;
         else
            fprintf(tf,"%x",ch);

    }
    fclose(sf);
    fclose(tf);
    return 0;
}
