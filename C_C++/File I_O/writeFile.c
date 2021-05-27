#include<stdio.h>

int main()
{
    FILE *fp;
    char ch='a', fileName[20];

     printf("Input name of file to Write\n");
     gets(fileName);

     fp=fopen(fileName,"w");  //Access to open file's structure
     if(fp==NULL)
     {
         puts("Cannot Open or Find ");
         puts(fileName);
         return 1;
     }

    while(1)
    {
        fputc(ch,fp);

            break;
            }
    fclose(fp);
    return 0;
}
