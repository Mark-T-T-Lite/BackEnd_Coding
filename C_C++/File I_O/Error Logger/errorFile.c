#include<stdio.h>

int main()
{
    FILE *fp;
    char ch, fileName[20];

     printf("Input name of file to Read\n");
     gets(fileName);

     fp=fopen(fileName,"w");  //Access to open file's structure
     /*if(fp==NULL)
     {
         puts("Cannot Open or Find ");
         puts(fileName);
         return 1;
     }*/

    while(!feof(fp))
    {
        ch=fgetc(fp);  //Access Structure,access buffer first character.

        if(ferror(fp))
        {
            perror(fileName);
            break;
        }

        if(ch==EOF)
            break;

        printf("%c",ch);

    }
    fclose(fp);
    return 0;
}
