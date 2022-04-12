# -*- coding: utf-8 -*-
"""
Le but de ce code est de réaliser un algorithme
évolutionnaire

"""

# %% Importation des libraries necessaires
import math
import random
import csv
import time
# %% Initialisation

start = time.time()
N=1200
#N correspond a la taille de chaque generation. Les nouvelles generations
#contiennent N/3 des individus de la generation precedente
#N doit donc etre divisible par 3


# %% Recuperation et stockage des valeurs du fichiers position_sample.csv

f= open('/home/rmak09/Desktop/S2/Data & IA/position_sample.csv','r')
X=[]
Y=[]
T=[]
csvr = csv.reader(f)
t=[]
f.readline()

for line in csvr :

    t=line[0].split(';')
    T.append(float(t[0]))
    X.append(float(t[1]))
    Y.append(float(t[2]))
    
f.close()
# %% Création d'un individu

def random_individu():
    L=[]
    for i in range (6) :
        L.append(round(random.uniform(-100,100), 3))
    
    return L

# %% Création d'une population d'individu
def random_population() :
    L=[]
    for i in range(N) :
        L.append(random_individu()) 
    
    return L

# %% Création de la fonction fitness 
#NOTE : La fonction fitness prend en paramètre une population d'individu
def fitness(population) :
    
    Result=[]

    for element in population :
        p1 = element[0]
        p2 = element[1]
        p3 = element[2]
        p4 = element[3]
        p5 = element[4]
        p6 = element[5]

        EC=[]

        for i in range (len(X)) :
            xelement = X[i]
            yelement = Y[i]     
            Normeth= math.sqrt(xelement**2+yelement**2)
            Normexp= math.sqrt(round(p1*math.sin(p2*T[X.index(xelement)]+p3),3)**2+round(p4*math.sin(p5*T[Y.index(yelement)]+p6),3)**2)
            ecart = abs(Normeth - Normexp)
            EC.append(ecart)
        
        mean = round(sum(EC)/len(X),3)
        Result.append(mean)

    return Result 
#Retourne une liste de taille N ou les elements 
#representent la distance moyenne entre les points pour chacun des individus

# %% Selection des meilleurs individus 
    

def Selection (population, Result) :
    T=[]

    for element in Result :
        T.append(element)
        
    T.sort()

    L=[]
    
    d = min(T,key = lambda x:abs(x-0))
    index= Result.index(d)
    
    L.append(population[index])    
    T.remove(d)

    for i in range(0,int((N/3)-1)) :
        j = min(T,key = lambda x:abs(x-0))
        index= Result.index(j)
    
        L.append(population[index])
        T.remove(j)
    return L,d,L[0]


#La fonction retourne La liste de taille N/3 des meilleurs individus de la generation
#Elle retourne le meilleur resulat fitness trouvée + l'individu correspondant

# %% Fonction mutation + croisement
 
def mutation(individu) :
    population=[]

    for element in individu :
        population.append(element)
    r=int(round(random.uniform(1,6),0))
    
    
    for i in range (r) :
        z=int(round(random.uniform(0,5),0))
            
             

        population[z]= round(random.uniform(-100,100), 3)

    return population

def croisement(indiv1,indiv2) :
        return indiv2[:3] +indiv1[-3:]



# %% main


def f ():

    Generation = random_population()
    i=1000000
    compteur =1
    while i>0.1 :
        NextGen=[]
        r=fitness(Generation)
        Bestof=Selection(Generation,r)
        for element in Bestof[0]:
            muta=mutation(element)
            NextGen.append(muta)
            cross=croisement(element,Bestof[0][random.randint(0, (N/3)-1)])
            NextGen.append(cross)

        if Bestof[1]!=i :
            print('Best individual is '+str(Bestof[2])+' With a mean distance between theoretical and experimental points of : '+str(Bestof[1])+' after '+str(compteur)+ ' generations\n')
        compteur+=1
 
        NextGen.extend(Bestof[0])
            
        Generation=NextGen
        i=Bestof[1]
    end=time.time()

    print(str(end-start)+' secondes')
    return None

f()