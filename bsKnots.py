#english vowel sounds:     a e i o u y (maintain vowel cluster order)
#english consonant sounds: p b t d k g th f v s z sh j ch dj w ng h l r m n 


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

def faceKnot(string):
    #todo: take punctuation and put it after my face.
    return '%s with my face%s' %(string,punc)

#palendromize
#Alphabetize chars
#shuffle words
#vowel movements
#inconsonants
#Tom Marvolo Riddle
#Drunken Censor
#piglatin
#pu language (Jane Austen ==> Japune Aupustepun)
#bear translator
#Enigma

def main():
    arg0 = raw_input('Do you want rvrs, rawR, face or something else? ')

    if arg0 == 'rvrs':
	arg1 = str(raw_input('Enter text for reversal: '))
        print rvrsKnot(arg1)
    elif arg0 == 'rawR':
	arg1 = str(raw_input('Enter text for raw Reversal: '))
	print rawRKnot(arg1)
    elif arg0 == 'face':
	arg1 = str(raw_input('Enter text: '))
	print faceKnot(arg1)
    else:
	print 'Uh... I haven\'t gotten the Merit Badge for that knot yet.'
if __name__ == '__main__':
    main()
