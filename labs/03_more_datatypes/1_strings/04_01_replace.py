'''
Write a script that takes a string of words and a symbol from the user.
Replace all occurrences of the first letter with the symbol. For example:

String input: more python programming please
Symbol input: #
Result: #ore python progra##ing please

'''

# get user input (sentence)
sentence = input("Please enter a sentence: ")
# get user input (symbol)
symbol = input("Please enter a symbol: ")
# get first letter of sentence
first = sentence[0]
# replace all occurences of first letter with symbol
print(sentence.replace(first, symbol))