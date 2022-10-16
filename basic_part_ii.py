#while loop
i = 0
while i < 5:
    print(i)
    i += 1

#break
i = 0
while i < 5:
    print(i)
    if i == 3:
        break #when i equals to 3 stop the count!
    i += 1

#continue
# while i < 5:
#     print(i)
#     if i == 3:
#         continue #this will print 3 to infinite
#     i += 1

#for loop
teams = ['Manchester City', 'Manchester United', 'Chelsea']
for team in teams: #for each teams in the list, i will run the following code
    print('Club:',team)

#another for example
team = 'Manchester City'
for c in team:
    print(c) #you will see each character in the string

#and another for example
teams = ['Manchester City', 'Manchester United', 'Chelsea']
for team in teams: 
    if team == 'Chelsea':
        break #doesnt print 'Chelsea'
    print('Club:',team)

#and another for example
teams = ['Manchester City', 'Manchester United', 'Chelsea']
for team in teams: 
    if team == 'Manchester United':
        continue #skip 'Manchester United'
    print('Club:',team)

#do i have say it again? c:
for x in range(10):
    print(x)
#do you want print 1 to 10?
for x in range(1, 11):
    print(x)
#do you want to print from 1 to 10 but in pairs?
for x in range(2, 11, 2):
    print(x)
else:
    print('Done.')

#functions
def myFunction():
    print('My first function')

myFunction()
#2
def printData(name, surname):
    print('Full name:', name, surname)

printData('Joseph', 'Cash')
#3
def printData_(*teams):
    print('Team:', teams)

printData_('Manchester City', 'Manchester United', 'Chelsea')

#4
def fullName(surname, name):
    print('Full name:',name, surname)

fullName(name = 'Joseph', surname = 'Cash')

#5
def fullName2(**kwargs): #kwargs allow the access to arguments with dictionaries syntax
    print(kwargs['name'], kwargs['surname'])

fullName2(name = 'Joseph', surname = 'Cash')

#more functions
def myFunction2(argument = 'Manchester United'):
    print(argument)
myFunction2()

#list function
def myListFunction(list):
    for t in list:
        print(t)
myListFunction(['Manchester City', 'Manchester United', 'Chelsea'])

#concatenate name
def concatenateName(list1):
    i = ''
    for na in list1:
        i = i + na + ' '
    return i 
fullName3 = concatenateName(['Joseph', 'Cash'])
print(fullName3)
#recursion
def recursion(i):
    if(i < 1):
        return i
    print(i)
    recursion(i - 1)
recursion(10)