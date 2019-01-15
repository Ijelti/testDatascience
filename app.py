import sys 
from importCsv import importer, dictionnaireAction  
from segmentation import segmentUser , fussion 
from output import writterCsv
 
#fonction d'affichage 
def affichage(pathinput1,pathinput2,pathoutput):
    doc=importer(pathinput1)
    dil=dictionnaireAction(doc)
    my_dict1=segmentUser(dil)
    my_dict2=fussion(pathinput2) 
    writterCsv(my_dict1,my_dict2,pathoutput)


if __name__== '__main__':
    print('sys.argv:', sys.argv)
    if len(sys.argv)>1:
        affichage(sys.argv[1],sys.argv[2],sys.argv[3])
    else:
        print("manque d'argument")
        