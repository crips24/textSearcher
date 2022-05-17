f = open(input("entrez le chemin du ficher texte a analyser: "),'r')
w = open('reslutat.txt','w')
elementCherche=input("que chercher dans le texte ? : ")


for line in f :
    index=+1
    if elementCherche in line:
        
        print(line)
        w.writelines(line)
f.close
w.close
