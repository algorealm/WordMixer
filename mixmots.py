def melangeMots(mot1,mot2):
    compteur = 0
    touLettres = '' 
    for i in mot1:
        compteur += 1
        n = compteur
        for t in mot2:
            n += -1
            if n == 0:
                break
        touLettres = touLettres + i + t
    print(mot1, 'et', mot2, ':') 
    print(touLettres)  
    
melangeMots(input('Premier mot'), input('Deuxième mot')) 







