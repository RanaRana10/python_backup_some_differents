# # Function to reverse a text string
# def reverse_text(text):
#     return text[::-1]

# # Input text
# input_text = "Rana Universe"

# # Call the function to reverse the text
# reversed_text = reverse_text(input_text)

# # Print the reversed text
# print(reversed_text)






# texts = "Rana Universe"
# print(texts.replace("a","B",6))





# texts = "Rana Univaersea"
# print(texts.find("a"))
# print(texts.rfind("a"))





# texts = "Rana Univerase"
# print(texts.index("a"))
# print(texts.rindex("a"))





# texts = "Rana Univerase"
# print(texts.partition("a"))
# print(texts.rpartition("a"))





# text = "apple,orange,banana"
# result = text.split('orange')  # Splits using comma as the delimiter, starting from the right
# print(result)








# str1 = "Rana"
# str2 = "Universe"
# print(str1 +" "+ str2)




# text = "আশাক"
# length = len(text)
# print(length)




# text = "This is Rana Universe"
# print(text[1:6])




# text = "Python is easy and Python is powerful"
# count = text.count("y")
# print(count)




# sentence = "I like programming in Java"
# new_sentence = sentence.replace("Java", "Python")
# print(new_sentence)




# text = "Python"
# centered_text = text.center(9, "-")
# print(centered_text)





# number = "42"
# zero_filled_number = number.zfill(12)
# print(zero_filled_number)




# text = "Hello, World!"
# encoded_bytes = text.encode("utf-8")
# decoded_text = encoded_bytes.decode("utf-8")
# print(encoded_bytes)
# print(decoded_text)






text = "Hello, world! This is Python."
translation_table = str.maketrans({'e': 'E', 'o': None, 'i': 'I'})
translated_text = text.translate(translation_table)

print(translated_text)







