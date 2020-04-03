'''print('Python {r}'.format(r='rules!'))'''


'''print(1>2)'''
'''my_file= ( "C:\\Users\\dp\\Documents\\my_file.txt" )
my_file=open('my_file.txt')
my_file.seek(0)
my_file.readlines()'''

'''s='hello'
a=s[4]+s[3]+s[2]+s[1]+s[0]
print(a)

print(s[::-1])'''

'''n=int(input("Enter any number:"))
n=str(n)
print(n[::-1])'''

'''list=[0]*3
print(list)'''

'''a=[0]
b=[0]
c=[0]
d=a+b+c
print(d)'''

'''list3 = [1,2,[3,4,'hello']]
list3[2][2]=str('goodbye')
print(list3)'''

'''list4 = [5,3,4,6,1]
list4.sort()
print(list4)'''

'''d = {'simple_key':'hello'}
print(d['simple_key'])'''

'''d = {'k1':{'k2':'hello'}}
print(d['k1']['k2'])'''

'''d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
print(d['k1'][0]['nest_key'][1][0])

d = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['hello']]}]}]}
print(d['k1'][2]['k2'][1]['tough'][2][0])'''

'''list5 = [1,2,2,33,4,4,11,22,3,3,2]
set5=set(list5)
print(set5)'''

'''x='Print only the words that start with s in this sentence'
t=x.split(' ')

mylist = list(t)

for letter in mylist:
    if letter[0]=='s':
        print(letter)'''


'''for i in range(0,11,2):
    print(i)'''

'''xyz=[num for num in range (0,51,3)]
print(xyz)'''
'''OR'''

'''xyz=[num for num in range(0,51) if num%3==0]
print(xyz)'''


'''for num in range(1,101):
    if num%3==0 and num%5==0:
        print("FizzBuzz")
    elif num%3==0:
        print("Fizz")
    elif num%5==0:
        print("Buzz")
    else:
        print(num)'''

'''st = 'Print every word in this sentence that has an even number of letters'

t=st.split(' ')

mylist=list(t)

for letter in mylist:
    if len(letter)%2==0:
        print(letter)'''

'''st = 'Create a list of the first letters of every word in this string'#use list comprehension
mylist=st.split(' ')

thelist=[x[0] for x in mylist]
print(thelist)'''

'''def dog_check(mystring):
    if 'dog' in mystring.lower():
        return True
    else:
        return False

t= dog_check('The Dog Ran Away')
print(t)'''

'''def dog_check(mystring):
    return 'dog' in mystring.lower()

t=dog_check('Dog DOGG DOug')
print(t)'''

'''def mystring(x):
    return x
t=mystring("Hello World!")
print(t)'''

'''def myfunc(*args):
    return(list(args%2==0))

t=myfunc(10,11,12,13,14)
print(t)'''



'''LESSER OF TWO EVENS: Write a function that returns the lesser of two given numbers if both numbers are even, 
but returns the greater if one or both numbers are odd¶
lesser_of_two_evens(2,4) --> 2
lesser_of_two_evens(2,5) --> 5'''


'''def myfunc(n1,n2):
    if n1>n2:
        if n1%2==0 and n2%2==0:
            print(n2)
        else:
            print(n1)
    else:
        if n1%2==0 and n2%2==0:
            print(n1)
        else:
            print(n2)

t=myfunc(10,123)
print(t)'''

'''def animal_crackers(w1,w2):
    return w1[0]==w2[0]
t=animal_crackers(w1='Fast',w2='Cheetah')
print(t)'''

'''def myfunc(n1,n2):
    return (n1+n2)==20 or n1==20 or n2==20
t=myfunc(10,10)
print(t)'''

'''def myfunc(word):
    if len(word)<4:
        print("Word is too short.Minimum 4 letters required.")
    else:
        b=word[0].upper()+word[1:3]+word[3].upper()+word[4:]
        return b

t=myfunc(word='aditya')
print(t)'''

'''def myfunc(a):
    b= a.split(" ")
    return " ".join(b[::-1])
    
t=myfunc(a='I am Groot')
print(t)'''

'''def myfunc(a):
    return abs((100-a)<10) or abs((200-a)<100)

t=myfunc(a=1030)
print(t)'''

'''def myfunc(a):
    for i in range(0,len(a)-1):
        if a[i]==3 and a[i+1]==3:
            return True
    return False

t=myfunc(a='has_33([1, 3, 3])')
print(t)'''

'''def volume(a):
    vol=(4/3)*3.14*(a**3)
    return vol
t=volume(a=3)
print(t)'''

'''def range_check(num,minm,maxm):
    if num<minm or num>maxm:
        return False
    else:
        return True

t=range_check(num=3324,minm=12,maxm=135)
print(t)'''

'''def myfunc(a):
    b=a.split()
    for i in b:
        if i  .isupper():
            c=[]
            c.append(i)
            return ("Uc char are=",len(c))  #INCOMPLETE
            
        if i .islower():
            d=[]
            d.append(i)
            return("Lc char are=",len(d))

            
t=myfunc(a='Hello Mr. Rogers, how are you this fine Tuesday?')
print(t)'''

'''def myfunc(a):
    uc=0
    lc=0
    for i in a:
        if i .isupper():
            uc+=1
        if i .islower():
            lc+=1
    return ("UC are=",uc, "LC are=",lc)


t=myfunc(a='Hello Mr. Rogers, how are you this fine Tuesday?')
print(t)'''


'''def myfunc(a):
    b=set(a)
    return list(b)

t=myfunc(a=[1,1,1,2,2,2,3,3,3,4,4,5,5])
print(t)'''

'''def myfunc(a):
    b=a[0]
    for i in a:
        b*=i
    return b
t=myfunc(a=[1, 2, 3, -4])
print(t)'''

'''def myfunc(a):
    return a[::1]==a[::-1]

t=myfunc(a='tots')
print(t)'''

'''import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    a=set(alphabet)
    return a<=(set(str1.lower()))

t=ispangram("The quick brown fox jumps over the lazy dog")
print(t)'''

########################################################################################################################

'''def basic_board():
    print("     !     !     ")
    print("     !     !     ")
    print("     !     !     ")
    print("_____!_____!_____")
    print("     !     !     ")
    print("     !     !     ")
    print("     !     !     ")
    print("_____!_____!_____")
    print("     !     !     ")
    print("     !     !     ")
    print("     !     !     ")
    print("     !     !     ")

t = basic_board()
print(t)'''



'''def basic_board(board):
    print(board[7] + "|" + board[8] + "|" + board[9])
    print("-|-|-")
    print(board[4] + "|" + board[5] + "|" + board[6])
    print("-|-|-")
    print(board[1] + "|" + board[2] + "|" + board[3])

test_board=['#','o','x','o','x','o','x','o','x','o']
t=basic_board(board=test_board)
print(t)'''




'''print("Welcome to TicTacToe!")

while True:
    theBoard = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

if play_game == 'y':
    game_on = True
else:
    game_on = False'''


'''def display_board(board):
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')'''






'''def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input('Player 1: Do you want to be X or O? ').upper()

    if marker == 'X':
        return ('X', 'O')
    else:
        return ('O', 'X')


def place_marker(board, marker, position):
    board[position] = marker


def win_check(board, mark):
    return ((board[7] == board[8] == board[9] == mark) or  # toph
            (board[4] == board[5] == board[6] == mark) or  # middleh
            (board[1] == board[2] == board[3] == mark) or  # bottomh
            (board[7] == board[4] == board[1] == mark) or  # leftv
            (board[8] == board[5] == board[2] == mark) or  # middleh
            (board[9] == board[6] == board[3] == mark) or  # righth
            (board[7] == board[5] == board[3] == mark) or  # diag1
            (board[9] == board[5] == board[1] == mark))  # diag2


import random


def choose_first():
    flip = random.randint(0, 1)
    if flip == 0:
        return 'Player 1 '
    else:
        return 'Player 2 '


turn = choose_first()


def space_check(board, position):
    board[position] == ' '


def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
        else:
            # BOARD FULL for TRUE
            return True


def player_choice(board):
    position = 0
    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input("Enter any position:(1-9)"))
    return True


def replay():
    choice = int(input("Do you want to play again?Yes or No"))

    return choice == 'Yes'


print("Welcome to TicTacToe!")

while True:
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    turn = choose_first()
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter y or n.')

    if play_game == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player1':
            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player1_marker, position)

            if win_check(the_board, player1_marker):
                display_board(the_board)
                print("Player1 has won!!!")
                game_on = False

            else:
                if full_boardcheck(the_board):
                    display_board(the_board)
                    print("The game is tied!")
                else:
                    turn = 'Player2'


        else:
            display_board(the_board)

            position = player_choice(the_board)

            place_marker(the_board, player2_marker, position)

            if win_check(the_board, player2_marker):
                display_board(the_board)
                print("Player2 has won!!!")
                gmae_on = False

            else:
                if full_boardcheck(the_board):
                    display_board(the_board)
                    print("The game is tied!")
                else:
                    turn = 'Player1'

    if not replay():
        break'''
#######################################################################################################################

'''class Book():

    def __init__(self, author, title, pages):
        self.author = author
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"{self.author} has written {self.title}"

    def __len__(self):
        return self.pages'''



'''class Cylinder():

    #Class Object Atribute
    pi=3.14
    def __init__(self, radius,height):

        self.radius = radius
        self.height = height



    def volume(self):
        return "Volume=" , self.radius * self.radius * self.height * Cylinder.pi

    def surface_area(self):
        return "Surface Area=", 2 * self.radius * self.height * Cylinder.pi

my_cylinder=Cylinder(2,3)

V=my_cylinder.volume()
print(V)

S=my_cylinder.surface_area()
print(S)'''


'''class Line():
    
    def __init__(self,x1,y1,x2,y2):

        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def distance(self):
        return ((self.x2-self.x1)**2+(self.y2-self.y1)**2)**0.5

    def slope(self):
        return ((self.y2-self.y1)/(self.x2-self.x1))

my_Line=Line(4,6,8,10)

D=my_Line.distance()
print(D)

S=my_Line.slope()
print(S)'''

                             ###OR###

'''class Line():

    def __init__(self,coor1,coor2):

        self.coor1 = coor1
        self.coor2 = coor2


    def distance(self):

        x1, y1 = self.coor1        #Preferably use Tuple unpacking everytime
        x2, y2 = self.coor2

        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def slope(self):

        x1, y1 = self.coor1
        x2, y2 = self.coor2

        return ((y2-y1)/(x2-x1))


c1 = (3,5)
c2 = (5,10)
my_line = Line(c1,c2)


D =  my_line.distance()
print(D)

S = my_line.slope()
print(S)'''






'''class Account():

    def __init__(self,owner,balance):

        self.owner = owner
        self.balance = balance

    def deposit(self,amount):

        self.balance = self.balance + amount
        print("Amount {} has been deposited to your Account!".format(amount))

    def withdraw(self,amount):

        if amount > self.balance :
            print("Insufficient Funds!")

        else:
            self.balance = self.balance - amount
            print("Amount {} has been withdrawn from your Account!".format(amount))


my_acc = Account('Aditya',1000)

o = my_acc.owner
print(o)

b = my_acc.balance
print(b)

d = my_acc.deposit(500)
print(d)

b = my_acc.balance
print(b)

s = my_acc.withdraw(250)
print(s)

b = my_acc.balance
print(b)'''




'''try:
    for i in ['a', 'b', 'c']:
        result = print(i ** 2)

except TypeError:
    print("Please enter numbers only!")'''

'''x = 5
y = 0



try:
    result = z = x/y

except ZeroDivisionError :
    print("Cannot divide by Zero!")'''


'''def ask():
    a = int(input("Enter any number:"))
    return a**2


while True:
    try:
        a = int(input("Enter any number:"))
        result = a ** 2
    except:
        print("Please enter only integers!")
        continue
    else:
        print(result)
        break
    finally:
        print("Thank You!")'''


'''Create a Pets class that holds instances of dogs; this class is completely separate from the Dog class. 
In other words, the Dog class does not inherit from the Pets class.
 Then assign three dog instances to an instance of the Pets class. 
 Start with the following code below. 
 Save the file as pets_class.py. Your output should look like this:

I have 3 dogs. 
Tom is 6. 
Fletcher is 7. 
Larry is 9. 
And they're all mammals, of course.'''

class Pets():

    species = 'mammals'
    count = 3

    def __init__(self,name,age):

         self.name = name
         self.age = age
         self.is_hungry = True



    def info1(self):
        return(f"{self.name} is {self.age}.")

    def info2(self):
        return(f"{self.name} is {self.age}.")

    def info3(self):
        return (f"{self.name} is {self.age}.")

    def eat(self):
        self.hungry = False


print(f"I have {Pets.count} dogs.")

mydogs = Pets('Tom',6)

t = mydogs.info1()
print(t)

mydogs = Pets('Fletcher',7)

w = mydogs.info2()
print(w)

mydogs = Pets('Larry',9)

q = mydogs.info3()
print(q)

e = mydogs.species
print("And they are all",e)

are_my_dogs_hungry = False

if are_my_dogs_hungry == True:
    are_my_dogs_hungry = False

if are_my_dogs_hungry:
    print("The dogs are hungry!")

else:
    print("The dogs are not hungry!")

