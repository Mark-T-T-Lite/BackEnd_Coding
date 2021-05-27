/* A menu-driven program for elementary database management */
#include <stdlib.h>
#include <stdio.h>

 int main( )
 {
     FILE  *fp, *ft ;
     char  another, choice ;
     struct employee
     {
         char  name[40] ;
         int  age ;
         float  bs ;
     } e;
     char  empname[40],fileName[20] ;
     long int  recsize ;

     printf("Input name of Database file to operate\n");
     gets(fileName);

     fp = fopen ( fileName, "rb+" ) ;

        if ( fp == NULL )
            {
                fp = fopen ( fileName, "wb+" ) ;

                if ( fp == NULL )
                    {
                        puts ( "Cannot open file" ) ;
                        return 1;
                    }
            }

    recsize = sizeof ( e ) ;

    while ( 1 )
        {
            system("cls") ;

            printf ( "1. Add Records\n\n" ) ;
            printf ( "2. List Records\n\n" ) ;
            printf ( "3. Modify Records\n\n" ) ;
            printf ( "4. Delete Records\n\n" ) ;
            printf ( "0. Exit\n\n" ) ;
            printf ( "Your choice?\n" ) ;

            fflush ( stdin ) ;
            choice = getche( ) ;

              switch ( choice )
              {
                  case '1' :
                {
                    fseek ( fp, 0 , SEEK_END ) ;
                    another = 'Y' ;

                    while ( another == 'Y' )
                        {
                            printf ( "\nEnter name, age and basic sal. " ) ;
                            scanf ( "%s %d %f", e.name, &e.age, &e.bs ) ;
                            fwrite ( &e, recsize, 1, fp ) ;
                            printf ( "\nAdd another Record (Y/N) " ) ;
                            fflush ( stdin ) ;
                            another = getche( ) ;
                        }

                    break ;
                }
                    case '2' :
                {
                   rewind ( fp ) ;

                    while ( fread ( &e, recsize, 1, fp ) == 1 )
                        printf ( "\n%s %d %f\n", e.name, e.age, e.bs ) ;
                    system("pause");
                    break ;
                  }

                case '3' :
                {
                    another = 'Y' ;
                    while ( another == 'Y' )
                        {
                            printf ( "\nEnter name of employee to modify \n" ) ;
                            scanf ( "%s", empname ) ;

                            rewind ( fp ) ;
                            while ( fread ( &e, recsize, 1, fp ) == 1)
                                 {
                                     if ( strcmp ( e.name, empname ) == 0 )
                                     {
                                         printf ( "\nEnter new name, age & bs\n");
                                         scanf ( "%s %d %f", e.name, &e.age,&e.bs ) ;
                                         fseek ( fp, - recsize, SEEK_CUR ) ;
                                        fwrite ( &e, recsize, 1, fp ) ;
                                        break ;
                                      }
                                  }

                      printf ( "\nModify another Record (Y/N) " ) ;
                      fflush ( stdin ) ;
                      another = getche( ) ;
                      }

                        break ;
           }
           case '4' :
            {
                another = 'Y' ;
                while ( another == 'Y' )
                    {
                        printf ( "\nEnter name of employee to delete " ) ;
                        scanf ( "%s", empname ) ;

                        ft = fopen ( "TEMP.DAT", "wb" ) ;

                        rewind ( fp ) ;
                        while ( fread ( &e, recsize, 1, fp ) == 1 )
                            {
                                if ( strcmp ( e.name, empname ) != 0 )
                                fwrite ( &e, recsize, 1, ft ) ;
                            }

                        fclose ( fp ) ;
                        fclose ( ft ) ;

                    remove ( fileName ) ;
                    rename ( "TEMP.DAT", fileName ) ;

                    fp = fopen ( fileName, "rb+" ) ;

                    printf ( "Delete another Record (Y/N) " ) ;
                    fflush ( stdin ) ;
                    another = getche( ) ;
           }
           break ;
            }

            default:
                fclose ( fp ) ;

                exit(1);
                }
        }
 }
