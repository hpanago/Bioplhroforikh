import random
import sys

def check() :
 ok=False    
 DNA = input("Please insert bacterium's DNA: ")   
 while ok==False :
  for x in DNA :
    if x is not "A" and x is not "C" and x is not "G" and x is not "T" :
     DNA=input("Wrong DNA sequence.Please insert correct DNA: ")
    else :
     ok=True
 return DNA
    
cont=True
inf=sys.maxsize
while cont==True :
    new_DNA=" "
    DNA=check()
    for x in DNA :
     part_of_DNA=x
     if part_of_DNA is "A" :
        rnA=random.randint(1,5) 
        for x in range(rnA) :
         part_of_DNA+="A"
     elif part_of_DNA is "C" :
        rnC=random.randint(1,10)
        for x in range(rnC) :
         part_of_DNA+="C"
     elif part_of_DNA is "G" :
        rnG=random.randint(1,inf)
        for x in range(rnG) :
          part_of_DNA+="G"
     elif part_of_DNA is "T" :
        rnT=random.randint(1,inf)
        for x in range(rnT) :
          part_of_DNA+="T"      
     new_DNA+=part_of_DNA     
    print("The infected version of: "+ DNA + " is " + new_DNA)     
    answer=input("Do you want to enter a new bacterium's DNA: ")
    if answer is "N":
     cont=False
    elif answer is "Y" :
     cont=True