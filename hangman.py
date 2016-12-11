import random
criteria = False
wordline = 0
word = None
guesses = ''
f = open("5desk.txt", "r")
dictlines = f.readlines()
f2 = open("hangman.txt", "r")
hanglines = f2.readlines()
hangman = ""
beghang = 0
endhang = 5


print """
  ___ ___                                              
 /   |   \_____    ____    ____   _____ _____    ____  
/    ~    \__  \  /    \  / ___\ /     \\\\__  \  /    \ 
\    Y    // __ \|   |  \/ /_/  >  Y Y  \/ __ \|   |  \\
 \___|_  /(____  /___|  /\___  /|__|_|  (____  /___|  /
       \/      \/     \//_____/       \/     \/     \/ 

 ________     
|        |
|
|
|
|
"""

while (criteria==False):
	wordline = random.randint(1,61405)
	word = dictlines[wordline].upper()
	if (len(word)-2 >= 4) & (len(word)-2 <=7): 
		criteria = True
		# print "The word is %s" % word
	word = word[:len(word)-2]
remaining = 6
print "Secret word: ",
print "_ " * len(word)

while(remaining > 0):
	win = True
	print ""
	guess = str(raw_input("Choose a letter: ")).upper()
	guesses += guess
	if guess not in word:
		remaining -= 1
		if remaining != 6:
			beghang += 6
			endhang += 6
		print "WRONG!"
	else:
		print "Correct."
	print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
	print "Tries remaining: %d\t Previous guesses: %s\n" % (remaining, guesses)
	

	for line in hanglines:
		hangman += line
	i = beghang
	while (i >= beghang) & (i <= endhang):
		print hangman.splitlines()[i]
		i += 1
	print "\nSecret word: ",
	for char in word:
		if char in guesses:
			print char,
		else:
			print "_",
			win = False
	print "\n"

	if win:
		print "You win!"
		break


if remaining == 0:
	print "\nYou lose!"
	print "The word was: %s" % word


