/* File-copy program which copies text, .com and .exe files */
#include <stdio.h>
#include <stdlib.h>
 #include <fcntl.h>
 #include "D:\\Mark_T\\softwares\\CodeBlocks\\MinGW\\include\\sys\\types.h" // if present in sys directory use
#include "D:\\Mark_T\\softwares\\CodeBlocks\\MinGW\\include\\sys\\stat.h"

int main(int argc, char* argv[] )
{
    char  buffer[512], sourceFile[128], targetFile[128] ;
    int  inhandle, outhandle, bytes ;

    /* printf ( "\nEnter source file name" ) ;
     gets ( sourceFile );*/
     if(argc>3)
     {
         puts("Too many arguments to file copy program");
         exit(-2);
     }

    inhandle = open ( argv[1], O_RDONLY | O_BINARY ) ;

    if ( inhandle == -1 )
        {
            puts ( "Cannot open Source file" ) ;
            exit(-1) ;
        }

   /* printf ( "\nEnter target file name" ) ;
    gets ( targetFile ) ;*/

    outhandle = open ( argv[2], O_CREAT | O_BINARY | O_WRONLY, S_IWRITE ) ;

    if ( inhandle == -1 )
        {
            puts ( "Cannot open Target file" ) ;
            close ( inhandle ) ;
            exit(-1) ;
        }

        while(1)
        {
            bytes = read ( inhandle, buffer, 512 ) ;
            if ( bytes > 0 )
            {
                write ( outhandle, buffer, bytes ) ;
                printf("\nWriting from buffer");
            }

            else
                break;
        }
        close ( inhandle ) ;
        close ( outhandle ) ;

    return 0;
}
