import csv

dic2={}
#Calcul des points pour chauque Typeaction
def intervallePoints(k):
    point=0
    if k in range(0,10):
        point=0
    elif k in range(10,20):
        point=1
    elif k in range(20,30):
        point=2
    elif k in range(30,40):
        point=3
    elif k in range(40,50):
        point=4
    elif k in range(50,60):
        point=5
    return point

# l'intervalle de segmentation des utilisateurs 
def intervalleSegment(k):
    segment=0   
    if k in range(0,4):
        segment=1
    elif k in range(5,9):
        segment=2
    elif k in range(10,14):
        segment=3
    elif k in range(15,19):
        segment=4
    else:
        segment=5
    return segment


#segmentation des utilisateurs et le calcul du nombre d'action
def segmentUser(dico):
    dic2["IdUser"]=["sgmentation","nbrAction"]
    for iduser in dico.keys():
        somme=0
        comp=0
        for m in dico[iduser]:
            somme =somme + intervallePoints(int(m)) #pour calculer les points des actions 
            comp=comp+1 # pour calculer le nombre des actions 
        dic2[iduser]=[intervalleSegment(int(somme)),comp] # un dic contient le iduser comme clé  , une liste [segment de l'utilisateur, nombre des action] comme valeur
    return dic2 

#affectation des email à leurs utilisateurs       
def fussion(path):
    dicfusion={}
    with open(path, newline='') as csvfile:
        fichier = csv.reader(csvfile, delimiter='%', quotechar='|')
        for row in fichier:
            k=row[0]
            p=k.split(";")
            dicfusion[p[0]]=p[1]       
    return dicfusion                
              
                
                
                
                
                
                
                
                
                
                