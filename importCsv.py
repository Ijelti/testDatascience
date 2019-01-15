import csv

B=[]
dic={}
#Importation du ficier csv
def importer(path):
    condition=0
    with open(path, newline='') as csvfile:
        fichier = csv.reader(csvfile, delimiter='%', quotechar='|')
        for row in fichier:
            if condition == 1:
                k=row[0]
                p=k.split(";")
                if p[9]!= "NULL":
                    B.append([p[2],p[9]])# B est une liste de liste qui regroupe les utilisateurs (iduser,action) 
            condition=1   
    return B            
            
# Creation d'iun dictionnaire qui contient les iduser et leurs Typeactions 
def dictionnaireAction(B):
    for liste in B:
        iduser=liste[1]
        action=liste[0]
        if iduser not in dic.keys():
            dic[iduser]=[action]
        else:
            dic[iduser].append(action)        
    return dic

    

  

  
        
    

        
