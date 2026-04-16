import random
symbols = ['!','@','#','$','%','^','&','*','(',')','-','_','=','+']
numbers = ['0','1','2','3','4','5','6','7','8','9']
letters = [
    'a','b','c','d','e','f','g','h','i','j',
    'k','l','m','n','o','p','q','r','s','t',
    'u','v','w','x','y','z',
    'A','B','C','D','E','F','G','H','I','J',
    'K','L','M','N','O','P','Q','R','S','T',
    'U','V','W','X','Y','Z'
]
print("Welcome to password Generator!")
n_letters = int(input("How many letters you want in your password?\n")) #4
n_symbols = int(input("How many symblos you want in your password?\n"))
n_numbers = int(input("How many numbers you want in your password?\n"))

password_list = []
for i in range(1, n_letters + 1): #1,2,3,4
  char = random.choice(letters)
  password_list.append(char)


for i in range(1, n_symbols+1):
  char = random.choice(symbols)
  password_list.append(char)


for i in range(1, n_numbers+1):
  char = random.choice(numbers)
  password_list.append(char)
print(password_list)
random.shuffle(password_list)
print(password_list)
# join() combines (joins) all elements of a list into one single string
password= "".join(password_list)
print(password)
 
