import random
pointswhite=0
pointsblack=0
skakiera=[1,2,3,4,5,6,7,8]
for i in range(100):
    print(i+1,'ος ΓΥΡΟΣ')
    #ΧΡΗΣΙΜΟΠΟΙΩ ΔΥΟ ΜΕΤΑΒΛΗΤΕΣ ΓΙΑ ΤΙΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ ΤΟΥ ΚΑΘΕ ΠΙΟΝΙΟΥ
    leukp1=random.choice(skakiera)
    leukp2=random.choice(skakiera)
    aks1=random.choice(skakiera)
    aks2=random.choice(skakiera)
    vas1=random.choice(skakiera)
    vas2=random.choice(skakiera)
    while ((leukp1==aks1) and (leukp2==aks2) or (leukp1==vas1 and leukp2==vas2) or (aks1==vas1 and aks2==vas2)):
        leukp1=random.choice(skakiera)
        leukp2=random.choice(skakiera)
        aks1=random.choice(skakiera)
        aks2=random.choice(skakiera)
        vas1=random.choice(skakiera)
        vas2=random.choice(skakiera)
    if (leukp1==vas1 or leukp2==vas2):
        pointswhite=pointswhite+1
        print('Ο ΛΕΥΚΟΣ ΠΥΡΓΟΣ ΕΦΑΓΕ ΤΗΝ ΜΑΥΡΗ ΒΑΣΙΛΙΣΣΑ')
    if ((vas1-leukp1)==(vas2-leukp2) or (vas1-leukp1)==(leukp2-vas2) or (leukp1-vas1)==(vas2-leukp2) or (leukp1-vas1)==(leukp2-vas2)):
        pointswhite=pointswhite+1
        print('O ΛΕΥΚΟΣ ΑΞΙΩΜΑΤΙΚΟΣ ΕΦΑΓΕ ΤΗΝ ΜΑΥΡΗ ΒΑΣΙΛΙΣΣΑ')
    if (vas1==leukp1 or vas2==leukp2):
        pointsblack=pointsblack+1
        print('Η ΜΑΥΡΗ ΒΑΣΙΛΙΣΣΑ ΕΦΑΓΕ ΤΟΝ ΛΕΥΚΟ ΠΥΡΓΟ')
    if (vas1==aks1 or vas2==aks2):
        pointsblack=pointsblack+1
        print('Η ΜΑΥΡΗ ΒΑΣΙΛΙΣΣΑ ΕΦΑΓΕ ΤΟΝ ΛΕΥΚΟ ΑΞΙΩΜΑΤΙΚΟ')
    if ((vas1-leukp1)==(vas2-leukp2) or (vas1-aks1)==(leukp2-vas2) or (leukp1-vas1)==(vas2-leukp2) or (leukp1-vas1)==(leukp2-vas2)):
        pointsblack=pointsblack+1
        print('Η ΜΑΥΡΗ ΒΑΣΙΛΙΣΣΑ ΕΦΑΓΕ ΤΟΝ ΛΕΥΚΟ ΠΥΡΓΟ ')
    if ((vas1-aks1)==(vas2-aks2) or (vas1-aks1)==(aks2-vas2) or (aks1-vas1)==(vas2-aks2) or (aks1-vas1)==(aks2-vas2)):
        pointsblack=pointsblack+1
        print('Η ΜΑΥΡΗ ΒΑΣΙΛΙΣΣΑ ΕΦΑΓΕ ΤΟΝ ΛΕΥΚΟ ΑΞΙΩΜΑΤΙΚΟ')
print('Ο ΠΑΙΚΤΗΣ ΜΕ ΤΑ ΛΕΥΚΑ ΠΙΟΝΙΑ ΚΕΡΔΙΣΕ',pointswhite,'ΒΑΘΜΟΥΣ')
print('O ΠΑΙΚΤΗΣ ΜΕ ΤΑ ΜΑΥΡΑ ΠΙΟΝΙΑ ΚΕΡΔΙΣΕ',pointsblack,'ΒΑΘΜΟΥΣ')
