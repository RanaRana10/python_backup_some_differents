from num2words import num2words
from word2number import w2n

number = 421237
words = num2words(number)

print(f"The number {number} in words is: {words}")
 


word_number = "four lakh, twenty-one thousand, two hundred and thirty-seven"
numeric_value = w2n.word_to_num(word_number)

print(f"The word '{word_number}' represents the number: {numeric_value}")
