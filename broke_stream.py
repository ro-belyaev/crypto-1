def readAllCiphertexts():
	ciphertexts = []

	cipher = open("ciphertext/target", "rb")
	ciphertexts.append(cipher.read())
	cipher.close()

	for i in range(1, 11):
		fileName = "ciphertext/ciphertext-" + str(i)
		cipher = open(fileName, "rb")
		ciphertexts.append(cipher.read())
		cipher.close()

	return ciphertexts


def strxor(a, b):     # xor two strings of different lengths
    if len(a) > len(b):
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a[:len(b)], b)])
    else:
        return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b[:len(a)])])


def getXoredCombinations(ciphertexts, targetPos):
	"""returns combinations of xored ciphertexts
	xor element in targetPos position with others
	result is list of hex decoded strings"""
	xoredCiphertexts = []
	index = []
	for i in range(0, targetPos):
		index.append(i)
	for i in range(targetPos, len(ciphertexts)):
		index.append(i)

	for i in index:
		xoredCiphertexts.append(strxor(ciphertexts[targetPos].decode("hex"), ciphertexts[i].decode("hex")))
	return xoredCiphertexts

properSymbols = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', \
	'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', \
	'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', \
	'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
	'1', '2', '3', '4', '5', '6', '7', '8', '9', '0', \
	' ', '(', ')', '\'', '-', '<', '>', '?', '"', '.', ',', '/', ':')

def isCharAProperSymbol(char):
	for c in properSymbols:
		if c == char:
			return True
	return False

def getListOfProperSymbolsInPositionI(xoredCiphertexts, i):
	listOfProperSymbols = []
	result = False

	for j in range(0, len(xoredCiphertexts)):	#if position i is too big, return empty list
		if len(xoredCiphertexts[j]) >= i:
			result = True
			break

	if not result:
		return ['`']

	for possibleChar in properSymbols:
		isProperSymbol = True
		for j in range(0, len(xoredCiphertexts)):
			cipher = xoredCiphertexts[j]
			if len(cipher) < i:
				continue
			symbol = cipher[i]
			chechedSymbol = chr(ord(possibleChar) ^ ord(symbol))
			if not isCharAProperSymbol(chechedSymbol):
				isProperSymbol = False
				break
		if isProperSymbol:
			listOfProperSymbols.append(possibleChar)

	if not listOfProperSymbols:
		listOfProperSymbols.append('`')

	return listOfProperSymbols

def maxLenOfSubList(l):
	"""l is a list of sublists;
		returns len of biggest sublist"""
	length = 0
	for i in range(0, len(l)):
		sublist = l[i]
		if len(sublist) > length:
			length = len(sublist)
	return length

def printMessage(properSymbolsOfAllPositions, decodedChars):
	"""for each position on target message print all possible characters"""
	for i in range(0, len(target)):
		print str(i + 1).rjust(2), ' ',
	print

	maxSubListLen = maxLenOfSubList(properSymbolsOfAllPositions)
	for level in range(0, maxSubListLen):
		for num in range(0, len(target)):
			if decodedChars[num]:
				if level == 0:
					print decodedChars[num].rjust(2), ' ',
				else:
					print ' '.rjust(2), ' ',
			else:
				char = ' '
				if level < len(properSymbolsOfAllPositions[num]):
					char = properSymbolsOfAllPositions[num][level]
					if char == ' ':
						char = '^'
				print char.rjust(2), ' ',
		print

def decodeCiphertext(cipher, key):
	"""cipher is a string, and key is a dictionary
		returns dictionary"""
	decoded = {}
	for i in range(0, len(cipher)):
			if len(key) <= i and key[i]:
				decoded[i] = chr(ord(key[i] ^ ord(cipher[i])))
			else:
				decoded[i] = None

def computeKey(ciphertextNum, ciphertexts, decodedCiphertext):
	"""ciphertextNum is index of ciphertext in ciphertexts list"""
	cipher = ciphertexts[ciphertextNum].decode('hex')
	key = {}
	for i in range(0, len(decodedCiphertext)):
		if decodedCiphertext[i]:
			key[i] = chr(ord(decodedCiphertext[i]) ^ ord(cipher[i]))
		else:
			key[i] = None
	return key





ciphertexts = readAllCiphertexts()
target = ciphertexts[0].decode("hex")

xoredCiphertexts = getXoredCombinations(ciphertexts, 0)

properSymbolsOfAllPositions = []
for i in range(0, len(target)):
	properSymbolsOfAllPositions.append(getListOfProperSymbolsInPositionI(xoredCiphertexts, i))

decodedTarget = {}
for i in range(0, len(target)):
	decodedTarget[i] = None


decodedTarget = {
	0: 'T',
	1: 'h',
	2: 'e',
	3: ' ',
	4: 's',
	5: 'e',
	6: 'c',
	7: 'r',
	8: 'e',
	9: 't',
	10: ' ',
	11: 'm',
	12: 'e',
	13: 's',
	14: 's',
	15: 'a',
	16: 'g',
	17: 'e',
	18: ' ',
	19: 'i',
	20: 's',
	21: ':',
	22: ' ',
	23: 'W',
	24: 'h',
	25: 'e',
	26: 'n',
	27: ' ',
	28: 'u',
	29: 's',
	30: 'i',
	31: 'n',
	32: 'g',
	33: ' ',
	34: 'a',
	35: ' ',
	36: '',
	37: '',
	38: '',
	39: '',
	40: '',
	41: '',
	42: ' ',
	43: 'c',
	44: 'i',
	45: 'p',
	46: 'h',
	47: 'e',
	48: 'r',
	49: ',',
	50: ' ',
	51: 'n',
	52: 'e',
	53: 'v',
	54: 'e',
	55: 'r',
	56: ' ',
	57: 'u',
	58: 's',
	59: 'e',
	60: ' ',
	61: 't',
	62: 'h',
	63: 'e',
	64: ' ',
	65: 'k',
	66: 'e',
	67: 'y',
	68: ' ',
	69: 'm',
	70: 'o',
	71: 'r',
	72: 'e',
	73: ' ',
	74: 't',
	75: 'h',
	76: 'a',
	77: 'n',
	78: ' ',
	79: 'o',
	80: 'n',
	81: 'c',
	82: 'e',
}

# key = computeKey(0, ciphertexts, decodedTarget)

printMessage(properSymbolsOfAllPositions, decodedTarget)

#The ... message is ( When using ...) ... cipher
