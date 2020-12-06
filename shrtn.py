import sys

vowels = ('a','e','i','o','u')

def shortenfunc (word) :
	shrtname = ""
	shrtname = word[0]
	for x in word[2::].lower() :
    		if x not in vowels :
        		shrtname = shrtname + x
        print (shrtname)
	   
shortenfunc (sys.argv[1])
