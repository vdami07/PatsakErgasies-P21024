import numpy
import random
daxt = ['small','mid','big']
summoves = 0
sum=0
def checkRows(values):
    for row in values:
        if len(set(row)) == 1:
            return row[0]
    return 0

def checkDiagonals(values):
    if len(set([values[i][i] for i in range(len(values))])) == 1:
        return values[0][0]
    if len(set([values[i][len(values)-i-1] for i in range(len(values))])) == 1:
        return values[0][len(values)-1]
    return 0

def check_win(values):
    for newvalues in [values, numpy.transpose(values)]:
        result = checkRows(newvalues)
        if result:
            return True
    return False
#ΧΡΗΣΙΜΟΠΟΙΩ ΤΡΙΑ ΤΕΤΡΑΓΩΝΑ 3Χ3 ΔΙΟΤΙ ΔΕΝ ΜΟΥ ΛΕΙΤΟΥΡΓΟΥΣΕ ΜΕ ΕΝΑΝ ΠΙΝΑΚΑ 3Χ3, ΩΣΤΟΣΟ ΤΩΡΑ ΛΕΙΤΟΥΡΓΕΙ
values0 = [['EMPTY', 'EMPTY', 'EMPTY'],
     ['EMPTY', 'EMPTY', 'EMPTY'],
     ['EMPTY', 'EMPTY', 'EMPTY']]
values1 = [['EMPTY', 'EMPTY', 'EMPTY'],
     ['EMPTY', 'EMPTY', 'EMPTY'],
     ['EMPTY', 'EMPTY', 'EMPTY']]
values2 = [['EMPTY', 'EMPTY', 'EMPTY'],
     ['EMPTY', 'EMPTY', 'EMPTY'],
     ['EMPTY', 'EMPTY', 'EMPTY']]

for i in range(101):
	plithos = [9,9,9]
	#ΤΟ ΠΑΙΧΝΙΔΙ ΣΤΑΜΑΤΑΕΙ ΜΟΝΟ ΟΤΑΝ ΥΠΑΡΞΕΙ ΝΙΚΗΤΡΙΑ ΤΡΙΑΔΑ ΔΑΧΤΥΛΙΩΝ
	while check_win(values0) == True and check_win(values1)==True and check_win(values2)==True :
		x=random.choice(daxt)
		y=random.randrange(0,3)
		z=random.randrange(0,3)
		summoves=summoves + 1
		if x=='small':
			plithos[0]=plithos[0]-1
			if values0[y][z] == 'ADDED' :
				print('ΥΠΑΡΧΕΙ ΗΔΗ ΔΑΧΤΥΛΙΟΣ ΙΔΙΟΥ ΜΕΓΕΘΟΥΣ ΣΕ ΑΥΤΗ ΤΗ ΘΕΣΗ')
				flagSM=False
				while flagSM == False:
					y=random.randrange(0,3)
					z=random.randrange(0,3)
					if values0[y][z] == 'EMPTY':
						flagSM = True
				if check_win(values0) == False:
					print('ΛΗΞΗ ΠΑΙΧΝΙΔΙΟΥ, ΝΙΚΗΣΑΝ ΟΙ ΜΙΚΡΟΙ ΚΡΙΚΟΙ')
					break
			else:
				values0[y][z]='ADDED'
				if check_win(values0) == False:
					print('ΛΗΞΗ ΠΑΙΧΝΙΔΙΟΥ, ΝΙΚΗΣΑΝ ΟΙ ΜΙΚΡΟΙ ΚΡΙΚΟΙ')
					break
		elif x== 'mid':
			plithos[1]=plithos[1]-1
			if values1[y][z] == 'ADDED' :
				print('ΥΠΑΡΧΕΙ ΗΔΗ ΔΑΧΤΥΛΙΟΣ ΙΔΙΟΥ ΜΕΓΕΘΟΥΣ ΣΕ ΑΥΤΗ ΤΗ ΘΕΣΗ')
				flagMED=False
				while flagMED == False:
					y=random.randrange(0, 3)
					z=random.randrange(0,3)
					if values1[y][z] == 'EMPTY':
						flagMED = True
				if check_win(values1) == False:
					print('ΛΗΞΗ ΠΑΙΧΝΙΔΙΟΥ, ΝΙΚΗΣΑΝ ΟΙ ΜΕΣΣΑΙΟΙ ΚΡΙΚΟΙ')
					break
			else:
				values1[y][z]='ADDED'
				if check_win(values1) == False:
					print('ΛΗΞΗ ΠΑΙΧΝΙΔΙΟΥ, ΝΙΚΗΣΑΝ ΟΙ ΜΕΣΣΑΙΟΙ ΚΡΙΚΟΙ')
					break
		else:
			plithos[2]=plithos[2]-1
			if values2[y][z] == 'ADDED' :
				print('ΥΠΑΡΧΕΙ ΗΔΗ ΔΑΧΤΥΛΙΟΣ ΙΔΙΟΥ ΜΕΓΕΘΟΥΣ ΣΕ ΑΥΤΗ ΤΗ ΘΕΣΗ')
				flagBIG=False
				while flagBIG == False:
					y=random.randrange(0, 3)
					z=random.randrange(0,3)
					if values2[y][z] == 'EMPTY':
						flagBIG = True
				if check_win(values2) == False:
					print('ΛΗΞΗ ΠΑΙΧΝΙΔΙΟΥ, ΝΙΚΗΣΑΝ ΟΙ ΜΕΓΑΛΟΙ ΚΡΙΚΟΙ')
					break
			else:
				values2[y][z]='ADDED'
				if check_win(values2) == False:
					print('ΛΗΞΗ ΠΑΙΧΝΙΔΙΟΥ, ΝΙΚΗΣΑΝ ΟΙ ΜΕΓΑΛΟΙ ΚΡΙΚΟΙ')
					break
	sum=summoves+sum
MESOSOROSVIMATON = sum/i
print('O ΜΕΣΟΣ ΟΡΟΣ ΒΗΜΑΤΩΝ ΚΑΤΑ ΤΗΝ ΔΙΑΡΚΕΙΑ ΤΩΝ 100 ΠΑΙΧΝΙΔΙΩΝ ΗΤΑΝ:', MESOSOROSVIMATON)
