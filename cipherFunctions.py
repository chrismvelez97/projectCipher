import string

alphabet = list(string.ascii_lowercase)

def messageToNumber(message,alphabet=alphabet):
	messageAsNumbers = []
	
	for letter in message:
		position = alphabet.index(letter)
		
		messageAsNumbers.append(position)
	
	return (messageAsNumbers)

def shiftNumbers(list,shift=1):
	shiftedList = []
	
	for number in list:
		number = number + shift
	
		shiftedList.append(number)
	
	return (shiftedList)
	
def shiftAsEncryption(list,alphabet=alphabet):
	encryptedMessage = ""
	
	for number in list:
		encryptedMessage = encryptedMessage + alphabet[number]
	
	return (encryptedMessage)


def checkOutOfBounds(numList):
	outOfBoundsList = []
	
	for item in numList:
		
		if 0 < item < 26:
			outOfBoundsList.append(item)
			
		elif item < 0:
			newShift = item + 26
			
			outOfBoundsList.append(newShift)
			
		else:
			newShift = item - 26
			
			outOfBoundsList.append(newShift)
			
	return (outOfBoundsList)

