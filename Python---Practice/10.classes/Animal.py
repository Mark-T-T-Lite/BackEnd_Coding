#Animal category definition 
class Animal():
    
    def __init__(self, name):
        #some attributes common to animals 
        self.name = name
        self.reproduction = "unknown" 
        self.defence_mechanism = "unknown"
        self.species = "unknown"
        self.skin = "unknown"
        self.feeding_type = "unknown"
        self.animal_sound = "unknown"
        self.phylum = "unknown"
        self.legs = "unknown"
        self.motion_method = "unknown"

    #identify    
    def id(self):
        print("name: "+ self.name)
        print("feeding_type: "+self.feeding_type)
        print("animal_sound: "+self.animal_sound)        
        print("motion_method: "+self.motion_method)
        print("reproduction: "+self.reproduction)
        print("defence_mechanism: "+self.defence_mechanism)
        print("scientific name: "+self.species)
        print("phylum: "+self.phylum)        
        print("skin: "+self.skin) 
        print("legs_no: "+self.legs)
        
        

def main():
           
    name = input("\nThe name of the Animal please (either lion or cow or snail or fish)\n")
    animal = Animal(name)   #creates animal object

    #make the animal object unique
    if name == "lion" or name =="Lion" or name =="LION":
        animal.species = "Panthera leo"
        animal.skin = "Golden brown, alot of fur"
        animal.feeding_type = "Canivore"
        animal.animal_sound = "Roar"
        animal.phylum = "Vertebrate"
        animal.legs = "4"
        animal.motion_method = "Walks or runs on land"
        animal.reproduction = "Mating and giving birth to cubs"
        animal.defence_mechanism = "uses claws and the canines"


    elif name == "cow" or name =="Cow" or name =="COW":
        animal.species = "Bos taurus"
        animal.skin = "Patched hide, little fur"
        animal.feeding_type = "Herbivore"
        animal.animal_sound = "Moo"            
        animal.phylum = "Vertebrate"
        animal.legs = "4"
        animal.motion_method = "Walks or runs on land"
        animal.reproduction = "Mating and giving birth to calves"
        animal.defence_mechanism = "uses horns and the hooves"

    elif name == "snail" or name =="SNAIL" or name =="Snail":
        animal.species = "Gastropoda"
        animal.feeding_type = "mostly herbivore"
        animal.animal_sound = "unknown"
        animal.phylum = "Invertebrate"
        animal.legs = "1 'foot'"
        animal.motion_method = "Crawls"
        animal.reproduction = "lays eggs"
        animal.defence_mechanism = "hides in its shell"
        
    elif name== "fish" or name =="FISH" or name =="Fish":
        animal.species = "Chondrichthyes"
        animal.skin = "Scales"
        animal.feeding_type = "other smaller fish, plankton"
        animal.animal_sound = "Oscillates swim bladder among other ways"
        animal.phylum = "Vertebrate"
        animal.legs = "fins"
        animal.motion_method = "Swims under water"
        animal.reproduction = "lays eggs"
        animal.defence_mechanism = "uses its fins"

    #display unique animal's features 
    animal.id()
    del(animal)
    
#Execution begins here        
for n in range(4): 
    main()
    

    
    


    


