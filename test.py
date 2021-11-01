from typing import Counter, Sequence
import numpy as np
import os
import time
t1_start = time.time() 
def XOR(a,b):
    x=0
    if a==1 and b==1:
        x=0
    elif a==0 and b==0:
        x=0
    else:
        x=1

    return x 

def AND(a,b):
    if a==1 and b==1:
        return 1
    else:
        return 0

def NOT(b):
    if b==1:
        return 0
    else:
        return 1
    


# Amino ={ 
#     "Arg" : ["CGU" , "CGC" , "CGA" , "CGG"],
#     "phe": ["UUU","UUC"],
#     "leu": ["UUA","UUG"],
#     "Leu" : ["UUA" , "UUG" , "CUU" , "CUC" , "CUA" , "CUG"],
#     "Ser" : ["UCU" , "UCC" , "UCA" , "UCG"],
#     "Tyr" : ["UAU" , "UAC" ],
#     "Cys" : ["UGU" , "UGC"],
#     "Trp" : ["UGG"],
#     "Pro" : ["CCU" , "CCC" , "CCA" , "CCG"],
#     "His" : ["CAU" , "CAC"],
#     "Gin" : ["CAA" , "CAG"],
    
#     "Ile" : ["AUU" , "AUC" , "AUA"],
#     "Met" : ["AUG"],
#     "Thr" : ["ACU" , "ACC" , "ACA" , "ACG"],
#     "Asn" : ["AAU" , "AAC"],
#     "Lys" : ["AAA" , "AAG"],
#     "Ser" : ["AGU" , "AGC"],
#     "Arg" : ["AGA" , "AGG"],
#     "Val" : ["GUU" , "GUC" ,"GUA" ,"GUG"],
#     "Ala" : ["GCU" , "GCC" ,"GCA" ,"GCG"],
#     "Asp" : ["GAU" , "GAC"],
#     "Glu" : ["GAA" , "GAG"],
#     "Gly" : ["GGU" , "GGC" , "GGA" , "GGG"],
#     "Stop" : ["UAA" , "UAG" , "UGA"],
     

# }
Amino = [["Arg","CGU" , "CGC" , "CGA" , "CGG"],
   [ "phe", "UUU","UUC"],
   [ "leu", "UUA","UUG"],
    ["Leu" ,"UUA" , "UUG" , "CUU" , "CUC" , "CUA" , "CUG"],
   [ "Ser" ,"UCU" , "UCC" , "UCA" , "UCG"],
   [ "Tyr" ,"UAU" , "UAC" ],
   [ "Cys" ,"UGU" , "UGC"],
    ["Trp" ,"UGG"],
    ["Pro", "CCU" , "CCC" , "CCA" , "CCG"],
    ["His" ,"CAU" , "CAC"],
    ["Gin" ,"CAA" , "CAG"],
    
    ["Ile" ,"AUU" , "AUC" , "AUA"],
    ["Met" ,"AUG"],
    ["Thr" ,"ACU" , "ACC" , "ACA" , "ACG"],
    ["Asn" ,"AAU" , "AAC"],
    ["Lys" ,"AAA" , "AAG"],
    ["Ser" ,"AGU" , "AGC"],
    ["Arg" ,"AGA" , "AGG"],
    ["Val" ,"GUU" , "GUC" ,"GUA" ,"GUG"],
    ["Ala" ,"GCU" , "GCC" ,"GCA" ,"GCG"],
    ["Asp" ,"GAU" , "GAC"],
    ["Glu" ,"GAA" , "GAG"],
    ["Gly" ,"GGU" , "GGC" , "GGA" , "GGG"],
    ["Stop" ,"UAA" , "UAG" , "UGA"],

]
def compliment(x):
    ch=""
    st=""
    if len(x)>3:
        li=x.split("-")
        for char in li[0]:
            if char== 'C' or char=='c':
                ch=ch+'G'
            elif char=='U':
                ch=ch+'A'
            elif char=='G':
                ch=ch+'C'
            elif char=='A':
                ch=ch+'U'
            print(ch)
        li[0]=ch
        for i in li:
            st+=i+"-"
        return st
    else:
        for char in x:
            if char== 'C' or char=='c':
                ch=ch+'G'
            elif char=='U':
                ch=ch+'A'
            elif char=='G':
                ch=ch+'C'
            elif char=='A':
                ch=ch+'U'
            print(ch)
        return ch

def replace(x):
    
    name=x[-1]
    x=x[:-1]
    if name=='C':
        name='G'
    elif name=='G':
        name='C'
    elif name=='U':
        name='A'
    elif name=='A':
        name='U'
    x=x+name
    print(x)
    return x



def compute(codonarr, codonbinary, gate,inputline, gate_no):
    dummy=[]
    dummy.append(codonarr[0])
    f=open("codon.txt",'a')
    
    for x in range(0,gate_no):
        for y in range(0,inputline):
            print(x,"\n",y)
            if gate[x][y]==2:
                codonbinary[x+1][y]=NOT(codonbinary[x][y])
                codonarr[x+1][y]=compliment(codonarr[x][y])
                
            
            if gate[x][y]==0 or gate[x][y]==1:
                codonarr[x+1][y]=codonarr[x][y]
               
                codonbinary[x+1][y]=codonbinary[x][y]
                print(codonarr[x+1][y])
                
                print("here")
            elif gate[x][y]==-1:
                temp=""
                temp2=1
                for i in range(0,inputline):
                    if gate[x][i]==0:
                        temp+="-"+codonarr[x][i]
                        print(temp)
                        temp2= AND(temp2,codonbinary[x][i])
                codonbinary[x+1][y]= XOR(codonbinary[x][y],temp2)
                print("not here")
                if codonbinary[x+1][y]==1:
                    temp3=replace(temp)
                    codonarr[x+1][y]=codonarr[x][y]+temp3
                    
                else: 
                    codonarr[x+1][y]=codonarr[x][y]+temp
        print(codonarr[x+1])
        Y=codonarr[x+1]
        X=str(codonarr[x+1])
        f.write(X+"\n")
        
       
   
    print("\ncodon binary\n")
    for i in codonbinary:
        print(i)
        print("\n")
    print("\n\nGAte\n")
    for i in gate:
        print(i)
        print("\n")
    
    return Y
                    
def find_amino(codonarr,inputline):
    a=""
    for i in range(0,inputline):
        a+=codonarr[i]+"-"
    print(a,"\n\n\n")
    amino_acid= a.split("-")
    print(amino_acid)
    
    amino_str=[]
    for x in amino_acid:
        for list1 in Amino:
            for value in list1:
                if x==value:
                    amino_str.append(list1[0])
                    
    my_dict = {i:amino_str.count(i) for i in amino_str}

    print(my_dict)     #or print(my_dict) in python-3.x


    
    
    
    # mydict=Counter(amino_str)
    # # for i in amino_str:
    # #     mydict[i]=amino_str.count[i]

    # print(mydict)   


print("Enter two Codon")
inp=input()
inp2=input()
inpA=0
inpB=1
# if inpA==0:
#     inpB=1
# else:
#     inpB=0
print("\n Enter the input sequence")
Seq= input()
Seq= Seq.split(" ")
inputline=int(input("\n Enter the number of input line\n"))
gate_No= int(input("\n Enter the number of gate \n "))

t=[0]

for i in range(0,inputline-1):
    z=0
    t.insert(i,z)
codon_binary=[]
for i in range(0,gate_No+1):
    codon_binary.append(t)

codon_binary= np.array(codon_binary)
print(codon_binary)

for i in range(0,inputline):
    if Seq[i]==inp:
        codon_binary[0][i]=inpA
    elif Seq[i]==inp2:
        codon_binary[0][i]=inpB

print(codon_binary)

#codonarr=[['A','A','A','A'],['','','',''],['','','','']]   

t2=[]
for i in range(0,inputline):
    t2.append(' ')
print(t2)

codonarr=[]
for i in range(0,gate_No+1):
    codonarr.append(t2)
print(codonarr)
#for i in range(0,inputline):
codonarr[0]=list.copy(Seq)


print(Seq)
print(codon_binary)
print(codonarr)

f=open("codon.txt",'w')
s=str(Seq)
f.write(s+"\n")
f.close()

print("\n Enter the gate configuration :\n ")


target=[]
t=[]

for i in range(gate_No):
    a=input()
    t.append(a)

for i in range(gate_No):
    s= t[i].split(" ")
    temp=[]
    for i in s:
        if i.isnumeric():
            temp.append(int(i))
    target.append(temp)

    

print(target)    


tempx=[]
for i in range(0,inputline):
    tempx.append(1)
print(tempx)

g1=[]
for i in range(0,gate_No):
    g1.append(tempx)

print(g1)
g=np.array(g1)
print(g)
g2=g
target=np.array(target)
j=0
for k in target:
    if j<gate_No:

        for i in k:
            if i==k[-1] and len(k)==1:
                g[j][i-1]=2
            elif i==k[-1]:
                g[j][i-1]=-1
            else:
                g[j][i-1]=0
        j=j+1
    else:
        break
print(g)


duplicate_codon=codonarr.copy()
codonarr1 =compute(codonarr,codon_binary,g,inputline,gate_No)
f1=open("codon.txt","r")
codonlist=[]
for x in f1:
    codonlist.append(x)

for h in codonlist:
    print(h)
    print("\n")

h=list(h)
print(codonarr1)
find_amino(codonarr1,inputline)



f1.close()
os.remove("codon.txt")
choice=0
while choice!=3:
    print("\n Enter your choice : \n1. For SMGF \n2. For PMGF \n3. exit")
    choice=int(input())
    if choice==1:
        faulty=int(input("\n enter the position of faulty gate: "))
        
        for i in range(0,inputline):
            g[faulty-1][i]=1

        print(g)

        f=open("codon.txt",'w')
        s=str(Seq)
        f.write(s+"\n")
        f.close()

        codonarr2= compute(duplicate_codon,codon_binary,g,inputline,gate_No)
        f1=open("codon.txt","r")
        codonlist1=[]
        for x in f1:
            codonlist1.append(x)

        for h in codonlist1:
            print(h)
            print("\n")
        find_amino(codonarr2,inputline)

        f1.close()
        os.remove("codon.txt")
    elif choice==2:

        print("\nEnter the number of gate: ")
        pos_gate=int(input())
        print("\n Enter the postion : ")
        pos=input()
        pos_arr=pos.split(" ")
        print(pos_arr)
        g2=np.array(g2)
        print(g2)
        for x in range(len(pos_arr)):
            pos_arr[x]=int(pos_arr[x])

        print(pos_arr)

        for value in pos_arr:
            g2[pos_gate-1][value-1]=1

        print(g2)
        count=0
        for x in range(inputline):
            if g2[pos_gate-1][x]==1:
                count=count+1

        if(count==inputline-1):
            for x in range(inputline):
                if g2[pos_gate-1][x]==-1:
                    g2[pos_gate-1][x]=2

        print(g2)       

        f=open("codon.txt",'w')
        s=str(Seq)
        f.write(s+"\n")
        f.close()

        codonarr2= compute(duplicate_codon,codon_binary,g2,inputline,gate_No)
        f1=open("codon.txt","r")
        codonlist1=[]
        for x in f1:
            codonlist1.append(x)

        for h in codonlist1:
            print(h)
            print("\n")
        find_amino(codonarr2,inputline)

        f1.close()
        os.remove("codon.txt")

t1_stop = time.time()
   

