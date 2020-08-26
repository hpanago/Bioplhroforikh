RNA=input("Please insert RNA: ")
first_of_the_bond=RNA[0]
maxUA=0
maxCG=0
maxGC=0 
maxAU=0
if (len(RNA) % 2) == 0:
   second_of_the_bond=RNA[len(RNA)]
else:
   second_of_the_bond=RNA[len(RNA)-1]
bond=first_of_the_bond+second_of_the_bond
max=0
max_bonds=[0,0,0,0]
i=1
while i<len(RNA):
   first_of_the_bond=RNA[i];
   if (len(RNA) % 2) == 0:
    second_of_the_bond=RNA[len(RNA)-i]
   else:
    second_of_the_bond=RNA[len(RNA)-i+1]
   c_bond=first_of_the_bond+second_of_the_bond;
   if bond==c_bond:
    if c_bond=="UA" :
	  maxUA+=1;
    elif c_bond=="CG" :
	  maxCG+=1;	
    elif c_bond=="GC" :
	  maxGC+=1;	
    elif c_bond=="AU" :
	  maxAU+=1;
   elif c_bond!=bond :
    if c_bond=="UA" :
      max_bonds[0]=maxUA;
	  maxUA=0
	elif c_bond=="CG" :
	 max_bonds[1]=maxCG;	
	 maxCG=0	
	elif c_bond=="GC" :
	  max_bonds[2]=maxGC;	
	  maxGC=0	
	elif c_bond=="AU" :
	  max_bonds[3]=maxAU
	  maxAU=0
   bond=c_bond
   print(c_bond)
   i+=1
for x in max_bonds :
  if max_bonds[i]>max:
    max=max_bonds[i]
print("The max number of non-alternating bonds is: "+ str(max))