import csv

#Creatiojn du fichier csv [email / segment / nombreAction]
def writterCsv(my_dict1,my_dict2,pathoutput):
    with open(str(pathoutput), 'w') as f:
        for key1,value in my_dict1.items():
            for key2,value1 in my_dict2.items():
                if key1 == key2:
                    f.write('{0};{1};{2}\n'.format(value1,value[0],value[1]))
