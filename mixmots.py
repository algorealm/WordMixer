def melangeMots(mot1,mot2):
    compteur = 0
    for i in mot1:
        print(i)
        compteur += 1
        n = compteur
        for i in mot2:
            n += -1
            if n == 0:
                print(i)
                break        

melangeMots('evegoyer','dereckpiche')







