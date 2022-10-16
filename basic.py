#variables
number_ = 5  #number
print(number_)
string_ = 'This is a string' #string
print(string_)

#multivariables
#this variables have different content
a , b , c = 'First variable', 'Second Variable', 'Third Variable'
print(a, b, c)
#this variables have the same content
a = b = c = 'Example'
print(a, b, c)

#concatenation
#when we use a comma, print like this 'Hello World'
one = 'Hello'
two = 'World'
print(one, two)
#but when we use a plus symbol, print like this 'HelloWorld'

#type numbers
first = 20 #integer
second = 20.0 #float
third = 1j #complex
print(first, second, third)

#list
list = ['Manchester City', 'Liverpool', 'Manchester United', 'Chelsea']
#add element to list
list.append('Brentford')
#copy list
list2 = list.copy()
list2.append('Leicester')
#delete all elements in the list
#list.clear()
#count how many 'Leicester' are in the list
print(list.count('Leicester'))
print(list)
#count how many 'Manchester City' are in the list
print(list2.count('Manchester City'))
print(list2)
#len = how many elements have the list
print(len(list), len(list2))
#print specific element
print(list[0])
#delete the last element in the list
#list.pop()
#delete specific element
#list.remove('Liverpool')
#reverse list
list.reverse()
print(list)
#sort list (you cant sort a list with different variables ['Manchester City', 4])
list.sort()
print(list)

#tuples (you cant modify them)
tuple_ = ('Manchester City', 'Manchester United', 'Brentford')
print(tuple_)
#how many 'Brentford' exists in the list
print(tuple_.count('Brentford'))
#how position is 'Manchester United'
print(tuple_.index('Manchester United'))

#range
range_ = range(6)
print(range_)

#dictionaries 
dictionarie_ = {
    'name': 'Manchester City',
    'score': 20,
    'goals scored': 26
}
print(dictionarie_)
#specific element in the dictionarie
print(dictionarie_['name'])
#or
print(dictionarie_.get('name'))
#change values in the dictionarie
dictionarie_['name'] = 'Chelsea'
print(dictionarie_)
#how many elements have in the dictionarie
print(len(dictionarie_))
#add value
dictionarie_['Red Cards'] = 0
print(dictionarie_)
#delete value
dictionarie_.pop('Red Cards')
print(dictionarie_)
#copy dictionarie
dictionarie_copy = dictionarie_.copy()
print(dictionarie_copy)
#delete last value
dictionarie_.popitem()
print(dictionarie_)
#delete all values
dictionarie_.clear()
print(dictionarie_)

#nested dictionaries
songs = {
    "Honey": {
        "artist": 'Jesse Baez',
        "release_year": 2022,
        "album": 'Amor En Español'
    },
    "Fancy Shoes": {
        "artist": 'The Walters',
        "release_year": 2014,
        "album": 'Songs for Dads - EP'
    }
}
print(songs)

#dict associates keys to values
songs = dict(name = 'Remember When', release_year = 2019, album = 'Nothing Happens')
print(songs)

#boolean
boolean_ = True
boolean__ = False
print(boolean_, boolean__)

#if and conditions
if 2 < 5:
    print('2 is minor than 5')
if 5 > 2:
    print('5 is bigger than 2')
if 2 == 2:
    print('2 is equal to 2')
if 2 != 5:
    print('2 is different than 5')
if 2 <= 5:
    print('2 is minor or equal to 5')
if 5 >= 2:
    print('5 is bigger or equal to 2')

if 2 > 5:
    print('2 is bigger than 5')
#if the previous condition is false, elif enter to the game
elif 2 < 5:
    print('2 is minor than 5')
#if the previous conditions are false, else enter to the game
else:
    print('error')
#ternary operator
print('example') if 5 > 2 else print('another_example')
# and
if 2 < 5 and 5 > 2:
    print('each conditions are true')
#or 
if 1 < 0 or 1 > 0:
    print('one of the conditions are true')




