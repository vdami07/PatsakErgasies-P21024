import random
pointswhite=0
pointsblack=0
skakiera=[1,2,3,4,5,6,7,8]
for i in range(100):
    print(i+1,'ος ΓΥΡΟΣ')
    #ΧΡΗΣΙΜΟΠΟΙΩ ΔΥΟ ΜΕΤΑΒΛΗΤΕΣ ΓΙΑ ΤΙΣ ΣΥΝΤΕΤΑΓΜΕΝΕΣ ΤΟΥ ΚΑΘΕ ΠΙΟΝΙΟΥ ΚΑΙ ΣΕ ΑΥΤΗ ΤΗΝ ΑΣΚΗΣΗ ΑΝΤΙΣΤΟΙΧΑ ΜΕ ΤΗΝ ΑΣΚΗΣΗ 6
    leukp1=random.choice(skakiera)
    leukp2=random.choice(skakiera)
    aks1=random.choice(skakiera)
    aks2=random.choice(skakiera)
    while ((leukp1==aks1) and (leukp2==aks2)):
        leukp1=random.choice(skakiera)
        leukp2=random.choice(skakiera)
        aks1=random.choice(skakiera)
        aks2=random.choice(skakiera)
    if (leukp1==aks1 or leukp2==aks2):
        pointswhite=pointswhite+1
        print('Ο ΛΕΥΚΟΣ ΠΥΡΓΟΣ ΕΦΑΓΕ ΤON ΜΑΥΡΟ ΑΞΙΩΜΑΤΙΚΟ')
    elif ((aks1-leukp1)==(aks2-leukp2) or (aks1-leukp1)==(leukp2-aks2) or (leukp1-aks1)==(aks2-leukp2) or (leukp1-aks1)==(leukp2-aks2)):
        pointsblack=pointsblack+1
        print('O ΜΑΥΡΟΣ ΑΞΙΩΜΑΤΙΚΟΣ ΕΦΑΓΕ ΤΟΝ ΛΕΥΚΟ ΠΥΡΓΟ')
    else:
        print('ΙΣΟΠΑΛΙΑ')
print('Ο ΠΑΙΚΤΗΣ ΜΕ ΤΟΝ ΛΕΥΚΟ ΠΥΡΓΟ ΣΥΓΚΕΝΤΡΩΣΕ ΜΕΤΑ ΑΠΟ 100 ΓΥΡΟΥΣ:',pointswhite,'ΠΟΝΤΟΥΣ')
print('Ο ΠΑΙΚΤΗΣ ΜΕ ΤΟΝ ΜΑΥΡΟ ΑΞΙΩΜΑΤΙΚΟ ΣΥΓΚΕΝΤΡΩΣΕ ΜΕΤΑ ΑΠΟ 100 ΓΥΡΟΥΣ:',pointsblack,'ΠΟΝΤΟΥΣ')
print('----------------------------------------------------------------------------')
print('ΑΥΤΗ ΗΤΑΝ Η ΣΚΑΚΙΕΡΑ 8Χ8 ΔΙΑΣΤΑΣΕΩΝ ΤΩΡΑ ΘΑ ΤΟΠΟΘΕΤΗΘΟΥΝ ΣΕ ΣΚΑΚΙΕΡΑ 7Χ7 ΔΙΑΣΤΑΣΕΩΝ')
#ΣΚΑΚΙΕΡΑ 7 ΕΠΙ 7
skakiera7epi7=[1,2,3,4,5,6,7]
pointsblack=0
pointswhite=0
for i in range(100):
    print(i+1,'ος ΓΥΡΟΣ')
    leukp1=random.choice(skakiera7epi7)
    leukp2=random.choice(skakiera7epi7)
    aks1=random.choice(skakiera7epi7)
    aks2=random.choice(skakiera7epi7)
    while ((leukp1==aks1) and (leukp2==aks2)):
        leukp1=random.choice(skakiera7epi7)
        leukp2=random.choice(skakiera7epi7)
        aks1=random.choice(skakiera7epi7)
        aks2=random.choice(skakiera7epi7)
    if (leukp1==aks1 or leukp2==aks2):
        pointswhite=pointswhite+1
        print('Ο ΛΕΥΚΟΣ ΠΥΡΓΟΣ ΕΦΑΓΕ ΤON ΜΑΥΡΟ ΑΞΙΩΜΑΤΙΚΟ')
    elif ((aks1-leukp1)==(aks2-leukp2) or (aks1-leukp1)==(leukp2-aks2) or (leukp1-aks1)==(aks2-leukp2) or (leukp1-aks1)==(leukp2-aks2)):
        pointsblack=pointsblack+1
        print('O ΜΑΥΡΟΣ ΑΞΙΩΜΑΤΙΚΟΣ ΕΦΑΓΕ ΤΟΝ ΛΕΥΚΟ ΠΥΡΓΟ')
    else:
        print('ΙΣΟΠΑΛΙΑ')
print('Ο ΠΑΙΚΤΗΣ ΜΕ ΤΟΝ ΛΕΥΚΟ ΠΥΡΓΟ ΣΥΓΚΕΝΤΡΩΣΕ ΜΕΤΑ ΑΠΟ 100 ΓΥΡΟΥΣ:',pointswhite,'ΠΟΝΤΟΥΣ')
print('Ο ΠΑΙΚΤΗΣ ΜΕ ΤΟΝ ΜΑΥΡΟ ΑΞΙΩΜΑΤΙΚΟ ΣΥΓΚΕΝΤΡΩΣΕ ΜΕΤΑ ΑΠΟ 100 ΓΥΡΟΥΣ:',pointsblack,'ΠΟΝΤΟΥΣ')
print('----------------------------------------------------------------------------')
print('ΑΥΤΗ ΗΤΑΝ Η ΣΚΑΚΙΕΡΑ 7Χ7 ΔΙΑΣΤΑΣΕΩΝ ΤΩΡΑ ΘΑ ΤΟΠΟΘΕΤΗΘΟΥΝ ΣΕ ΣΚΑΚΙΕΡΑ 7Χ8 ΔΙΑΣΤΑΣΕΩΝ')
#ΣΚΑΚΙΕΡΑ 7 ΕΠΙ 8
skakiera7=[1,2,3,4,5,6,7]
skakiera8=[1,2,3,4,5,6,7,8]
pointsblack=0
pointswhite=0
for i in range(100):
    print(i+1,'ος ΓΥΡΟΣ')
    leukp1=random.choice(skakiera7)
    leukp2=random.choice(skakiera8)
    aks1=random.choice(skakiera7)
    aks2=random.choice(skakiera8)
    while ((leukp1==aks1) and (leukp2==aks2)):
        leukp1=random.choice(skakiera7)
        leukp2=random.choice(skakiera8)
        aks1=random.choice(skakiera7)
        aks2=random.choice(skakiera8)
    if (leukp1==aks1 or leukp2==aks2):
        pointswhite=pointswhite+1
        print('Ο ΛΕΥΚΟΣ ΠΥΡΓΟΣ ΕΦΑΓΕ ΤON ΜΑΥΡΟ ΑΞΙΩΜΑΤΙΚΟ')
    elif ((aks1-leukp1)==(aks2-leukp2) or (aks1-leukp1)==(leukp2-aks2) or (leukp1-aks1)==(aks2-leukp2) or (leukp1-aks1)==(leukp2-aks2)):
        pointsblack=pointsblack+1
        print('O ΜΑΥΡΟΣ ΑΞΙΩΜΑΤΙΚΟΣ ΕΦΑΓΕ ΤΟΝ ΛΕΥΚΟ ΠΥΡΓΟ')
    else:
        print('ΙΣΟΠΑΛΙΑ')
print('Ο ΠΑΙΚΤΗΣ ΜΕ ΤΟΝ ΛΕΥΚΟ ΠΥΡΓΟ ΣΥΓΚΕΝΤΡΩΣΕ ΜΕΤΑ ΑΠΟ 100 ΓΥΡΟΥΣ:',pointswhite,'ΠΟΝΤΟΥΣ')
print('Ο ΠΑΙΚΤΗΣ ΜΕ ΤΟΝ ΜΑΥΡΟ ΑΞΙΩΜΑΤΙΚΟ ΣΥΓΚΕΝΤΡΩΣΕ ΜΕΤΑ ΑΠΟ 100 ΓΥΡΟΥΣ:',pointsblack,'ΠΟΝΤΟΥΣ')
