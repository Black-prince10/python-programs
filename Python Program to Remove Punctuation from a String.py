'''
Punctuation:
The practice, action, or system of inserting points or other small marks into texts, in order to aid 
interpretation; division of text into sentences, clauses, etc., is called punctuation. -Wikipedia
Punctuation are very powerful. They can change the entire meaning of a sentence.
See this example:
"Woman, without her man, is nothing" (the sentence boasting about men's importance.)
"Woman: without her, man is nothing" (the sentence boasting about women's importance.)
This program is written to remove punctuation from a statement
'''
#define punctuation 
punctuation = '''''!()-[]{};:'"\,<>./?@#$%^&*_~'''

#take input from the user 
string_txt = input("Enter a string:")

#removing the punctuation from the string 
no_punc = ""
for ch in string_txt:
	if ch not in punctuation:
	    no_punc += ch 

#displaying  new string 
print(no_punc)


