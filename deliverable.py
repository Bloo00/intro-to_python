from email.policy import default


idx = 'abcde'.index("d") #3

idx = idx + 11 # 14

idx * 2 # idx 14


#################### 2

num = 33

is_even = num%2 == 0
print(is_even) # flase
print(not is_even) #true


#################### 3

str1 = 'marker'
num = len('whiteboard') - len(str1)
print(num)   #4
str2 = 'bootcamp'
print(str2[num].upper())   #C
char = str2[num].lower() 
print(char + '!') #c



#################3## 4

sentence = 'welcome to bootcamp prep'
lastChar = sentence[len(sentence) - 1] 
print(lastChar) #p
print(sentence.index(lastChar)) # 18

##################### 5

age = 30
if (age > 30):
  print('older than 30')
else:
  print('younger than 30')

##################### 6

str = 'pizza'
if (len(str) > 10):
  print('long string')
else:
    print('short string')

if ([0] == 'p') :
  print('starts with p')

###################### 7

num = 15 
if (num % 3 == 0): 
  print('divisible by 3')
elif (num % 5 == 0): 
  print('divisible by 5')


####################### 8

num = 15 
if (num % 3 == 0): 
  print('divisible by 3')
elif (num % 5 == 0): 
  print('divisible by 5')


  ################### 9

str = 'General Assembly'
if (str[0] == str[0].upper()):
  print('starts with a capital!')

if (str[len(str) - 1] == str[len(str) - 1].upper()):
 print('ends with a capital!')


####################### 10

num = -44
if (num > 0) :
  print('positive')
elif (num < 0) :
  print('negative')
else :
  print(0)

if (num % 2 == 0) :
  print('even')
else: 
  print('odd')


############################################################################################ 4

num = 11
if (num > 5):
  ('if')

num = 5
if (num > 5):
  print('if')
else:
  print('else')

num = 0
if (num < 0): 
  print('if')
elif (num > 0):
  print('else if')
else: 
  print('else')

############################################33 5

def sayHello(name): 
  msg = 'Hello, ' + name + '. How are you?'
  return msg

print(sayHello('bootcamp prep'))

def checkNumber(num):
    if (num > 0): 
        return 'positive'
    elif (num < 0): 
        return 'negative'
    else: 
        return 'zero'
  

print(checkNumber(5))

def fizzBuzz1(max):
    for i in range(len(max)):
        if (i%3 == 0 and i % 5 !=0):
            print(i)
        elif (i % 5 == 0 and i % 3 != 0):
            print(i)
        elif(i % 5 == 0 and i % 3 == 0):
          print(i)
    
  

def evenCaps(sentence): 
  newSentence = ""

  for i in range(len(sentence)): 
    char = sentence[i]

    if (i % 2 == 0):
      capitalChar = char.upper()
      newSentence += capitalChar
    else:
      newSentence += char
    
  

  return newSentence
evenCaps("hihi hihi nhihi")
