#Reversing the word using Recurssion

def reverseWords(word):
	if word == "":
		return word
	else:
		substituteWord = word[1:]
		returnWord = reverseWords(substituteWord)
		solution = returnWord + word[0]
		return  solution

wordToBeReversed = raw_input('Enter the word to be reversed')
print reverseWords(wordToBeReversed)