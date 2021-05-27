
#Applicant General definition 
class Applicant_Bio:
    
    def __init__(self, name):
        #Common BIODATA
        self.name = name
        self.age = 0
        self.gender = "unknown"
        self.home_district = "unknown"

class Qualification:
    def __init__(self):
        self.O_points = 0
        self.A_points = 0

    def checkPoints(self):

        if (self.O_points+self.A_points) >= 50:
            choice_lim=5
            choice = eval(input("You qualify for:\n1.Civil ENG.\n2.Electrical ENG\n3.Telecom Eng.\n4.Computer ENG.\n5.Mechanical Eng\n Choose"))
            return choice,choice_lim 
        elif (self.O_points+self.A_points) >= 46 and (self.O_points+self.A_points) <50:
            choice_lim=4
            choice = eval(input("You qualify for:\n2.Electrical ENG\n3.Telecom Eng.\n4.Computer ENG.\n5.Mechanical Eng\n Choose"))
            return choice,choice_lim
        elif (self.O_points+self.A_points) >= 44 and (self.O_points+self.A_points) <46:
            choice_lim=3
            choice = eval(input("You qualify for:\n3.Telecom Eng.\n4.Computer ENG.\n5.Mechanical Eng\n Choose"))
            return choice,choice_lim
        elif (self.O_points+self.A_points) >= 41 and (self.O_points+self.A_points) <44:
            choice_lim=2
            choice = eval(input("You qualify for:\n3.Telecom Eng.\n Choose\n"))
            return choice,choice_lim
        else:
            return 0        

class Preferences:
    def __init__(self,choice):
        self.choice = choice
        self.course_given = "unknown"
        self.entry_scheme= "unknown "

    def assignCourse(self, choice_lim):
        print(choice_lim)
        if self.choice == 1 and choice_lim>=5:
            self.course_given = "Bsc. Civil Eng."
           
        elif self.choice == 2 and choice_lim>=4:
            self.course_given = "Bsc. Electrical Eng."
            
        elif self.choice == 3 and choice_lim>=2:
            self.course_given = "Bsc. Telecommunications  Eng."
            
        elif self.choice == 4 and cchoice_lim>=2:
            self.course_given = "Bsc. Computer Eng."
            
        elif self.choice == 5 and choice_lim>=3:
            self.course_given = "Bsc. Mechanical Eng."
            
        else:
            print("pick one of the numbers")     
        
def main():
    choice_lim= -1
    
    name = input("\nEnter your full names\n")
    app1 = Applicant_Bio(name)   #creates the Applicant object

    #ENTER BIODATA
    app1.age = eval(input("Your Age?\n"))
    app1.gender = input("Your Gender\n")
    app1.home_district = input("Home District\n")

    # CHECKS AGE 
    if app1.age >= 16:
        app2 = Qualification()
        app2.O_points = eval(input("Place in Your O_level Points\n"))
        app2.A_points = eval(input("Place in Your A_level Points\n"))

        choice,choice_lim = app2.checkPoints()
        print(choice)
        if (choice>0):            
            app3 = Preferences(choice)
            if app1.age >= 25:
                app3.entry_scheme= input("Choose Entry Scheme :\nMature\nDirect\nDiploma\n")
            elif app1.age <25:
                app3.entry_scheme= input("Choose Entry Scheme :\nDirect\nDiploma\n")
            app3.assignCourse(choice_lim)

            print("Applicant Data")
            print("name: "+ app1.name)
            print("age: "+str(app1.age))
            print("gender: "+app1.gender)        
            print("home_district: "+app1.home_district)
            print("Olevel_points: "+str(app2.O_points))
            print("A level_points: "+str(app2.A_points))
            print("course_given: "+app3.course_given)
            print("Entry Scheme: "+app3.entry_scheme)
        else:
            print("You Can't do engineering this time")
        del(app2)
        del(app3)     
        
    else:
        # app1.id()
        print("You are not yet of age to qualify for applying to Makerere University")     
        del(app1)
        
    
#Execution begins here
choice = 0  
for n in range(2):     
    main()
    

    
    


    


