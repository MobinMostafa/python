# name= 'mobin'
# print(name[0:3])

# name=input('Write your name\n')
# print("Good Morning", name)

letter = ''' Dear <|name|> 
 You are selected.

 Date <|date|>
'''
name=input('Enter your name\n')
date=input('Enter your date\n')

letter= letter.replace("<|name|>", name)
letter= letter.replace("<|date|>", date)

print(letter)