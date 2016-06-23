import lists
import re
import random

def rvrsKnot(string):
    #todo: do not reverse vowel clusters
    #	   do not reverse standard english consonant sounds
    #	   do not reverse punctuation
    #	   retain case. 
    rvrs = ''
    count = len(string)
    for i in range(0,len(string)):
	count -= 1
	rvrs += string[count]
    return rvrs

def rawRKnot(string):
    return string[::-1]

def rPalKnot(string):
    if string == rvrsKnot(string):
	return string
    else:
	return 'Hey... %s isn\'t a palendrome. How am I supposed to reverse that?!' % string

def faceKnot(string):
    #todo: take punctuation and put it after my face.
    return '%s with my face' %(string)

def codeKnot(string,code1,code2):
	for i in range (0,len(code1)):
	    string = string.replace(code1[i],code2[i])
	return string
	#making actual changes now. Still has many bugs. 
	#Mostly because of characters like i, e, o, 
	#replacing more compicated characters. 
	#' i' is a temporary solution. 
	#But that creates further problems down the line.

def vmmtKnot(string):
	vowelMovement = ''
	test = r'[aeiou]'
	vowel = lists.lists('vowels')
	for i in range(0,len(string)):
	    if re.match(test, string[i]):
		vowelMovement += vowel[random.randint(0,len(vowel)-1)]
	    else:
		vowelMovement += string[i]
	return vowelMovement

def sortKnot(string):
	#expand string to list
	workList = list(string)
	#sort the list
	workList.sort()
	#shrink the list to output string
	clean = ''.join(workList)
	return clean



#palendromize
#Alphabetize chars
#shuffle words
#inconsonants
#Tom Marvolo Riddle
#Drunken Censor
#piglatin
#pu language (Jane Austen ==> Japune Aupustepun)
#bear translator
#Enigma

def main():
    arg0 = raw_input('rvrs, rPal, rawR, face, pinYin, wadeGiles, pu, vmmt, sort or something else? ')

    if arg0 == 'rvrs':
	arg1 = str(raw_input('Enter text for reversal: '))
        print rvrsKnot(arg1)
    elif arg0 == 'rawR':
	arg1 = str(raw_input('Enter text for raw Reversal: '))
	print rawRKnot(arg1)
    elif arg0 == 'face':
	arg1 = str(raw_input('Enter text: '))
	print faceKnot(arg1)
    elif arg0 == 'pinYin':
	arg1 = str(raw_input('Enter Wade-Giles text: '))
	arg2 = lists.lists('wadeGiles')
	arg3 = lists.lists('pinYin')
	print codeKnot(arg1,arg2,arg3)
    elif arg0 == 'wadeGiles':
	arg1 = str(raw_input('Enter PinYin text: '))
	arg2 = lists.lists('wadeGiles')
	arg3 = lists.lists('pinYin')
	print codeKnot(arg1,arg3,arg2)
    elif arg0 == 'pu':
	arg1 = str(raw_input('Enter non-pu text: '))
	arg2 = lists.lists('vowels')
	arg3 = lists.lists('puVowels')
	print codeKnot(arg1,arg2,arg3)
    elif arg0 == 'rPal':
	arg1 = str(raw_input('Enter palendrome to be reversed: '))
	print rPalKnot(arg1)
    elif arg0 == 'vmmt':
	arg1 = str(raw_input('Enter feed for the vowel movement: '))
	print vmmtKnot(arg1)
    elif arg0 == 'sort':
	arg1 = str(raw_input('Enter characters for sorting: '))
	print sortKnot(arg1)
    else:
	print 'Uh... I haven\'t gotten the Merit Badge for that knot yet.'
if __name__ == '__main__':
    main()
