subjectList=["English","Spanish","Algebra","Geography","Theater"]
gpas=[3.12 , 3.45, 2.99]

if(subjectList[0]=="Geography"):
    takingGeography="true"
    if(subjectList[1]=="Geography"):
        takingGeography="true"
        if(subjectList[2]=="Geography"):
            takingGeography="true"
            if(subjectList[3]=="Geography"):
                takingGeography="true"
                if(subjectList[4]=="Geography"):
                    takingGeography="true"
else:
    takingGeography="false"
                    
average= (gpas[0] + gpas[1] + gpas[2])/3
if(average>=3.33):
    print(average,"Average is greater or equal to 3.33")
    
else:
    print(average,"Average is less than 3.33")
