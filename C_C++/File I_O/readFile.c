#include<stdio.h>

int main()
{
    FILE *fp;
    char ch, fileName[20];

     printf("Input name of file to Read\n");
     gets(fileName);

     fp=fopen(fileName,"r");  //Access to open file's structure
     if(fp==NULL)
     {
         puts("Cannot Open or Find ");
         puts(fileName);
         return 1;
     }

    while(1)
    {
        ch=fgetc(fp);  //Access Structure,access buffer first character.
        if(ch==EOF)
            break;

        printf("%c",ch);

    }
    fclose(fp);
    return 0;
}
