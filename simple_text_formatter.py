text = "hello world"
text_1 = "hello World"
text_2 = "hello WORLD"
text_3 = "HELLO world"
text1 = " lorem ipsum dolor sit amet"
text2 = " testing whitespace"
text3 = " trimming spaces at the beginning"
text4 = "and spaces at the end"
text5 = " and spaces at both ends "
text6 = "a"
text7 = "b "
text8 = " c"
text9 = " d "
text10 = "d e f g h"
print(str(text.capitalize() + "."))
print(text_1.capitalize() + ".")
print(text_2.capitalize()  + "." )
print(text_3.capitalize() + ".")
print(text1.capitalize().strip() + "." )
print(text2.strip().capitalize() + ".")
print(text3.strip().capitalize() + ".")
print(text4.capitalize() + ".")
print(text5.strip().capitalize() + ".")
print(text6.capitalize() + ".")
print(text7.rstrip().capitalize() + ".")
print(text8.lstrip().capitalize() + ".")
print(text9.strip().capitalize() + ".")
print(text10.capitalize() + ".")