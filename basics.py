# type() is just like typeof operator in JS
# in python we have a native stdin that we can call as input() 
# bools are represented with capitals --> True, False
# AND, OR and NOT syntax --> and, or, not
# if ((age > 20 and age < 21) or age == 0): dosomething
# Checking for pointers/references is easy, just use 'is'

# in python, for 'in' is just like a regular forEach. No JS keys bullcrap. 
# To use regular for loops, use range: for iterable in range(1, 8):
# or more commonly if I want ]0,y] --> for iterable in range(y):
# We can also control the for loop skip with the third param like: for iterable in range(0, y, 2):
# while --> while (variable != condition): 
# break can be used normally 


# I can use len() to check the array length
# Negative indicies can be used to access the last element of the array
# Easy way to check if a list contains some value --> "whatever" in myList --> will return bool
# .append() one val end of list, .extend() multiple vals, .insert(pos, element) val at given pos
# .clear() removes all items, .pop(index) removes from list and returns it, if no index is given removes the last
# .remove(x) removes first element that matches x 
# .index(element) returns the index of the element --> can also have ranges --> .index(element, start, end)
# .count(x) returns the count of x on the list
# .reverse() --> yeah pretty much what it says
# .sort() --> yeah no JS tricks here, it really sorts numerically 
# .join() --> .join() --> str method but can be concatenated with lists like --> 'hey'.join(strList)
# --> join will combine the base string with each element of the list and returns a new str
# slice --> list[start:end:step] --> myList = [1,2,3] --> myList[2:] will return new list with [3]
# myList[1::1] --> returns [2,3]
# with slice we can also modify portions of lists like --> myList[0:1] = 'wut', will insert 'wut' into first pos of the list
# quick list reverse --> myList[::-1] --> slices the entire list starting from the back-end and returns a new str
# swapping values with comma syntax --> myName = ['bruno','giannotti']; myName[0], myName[1] = myName[1], myName[0];


# List comprehension is really cool, pretty much like filter, map, reduce all combined in one syntax
# --> [x*2 for x in myNumberList]
# --> [char.upper() for char in namesList]
# --> [person[0].upper() for person in personList] --> Makes the first char upper! Coolio!
# --> [num*100 for num in range(6)]
# --> [bool(value) for value in [0, '', [], 1]] --> False, False, False, True --> Please remember that [] is Falsy, different from JS!
# --> stringList = [str(num) for num in numbersList];
# --> odds = [num for num in numbersList if num % 2 == 0]
# --> cool = [num*2 if num % 2 == 0 else num/2 for num in numbersList]
# --> coolStringWithoutVowels = ''.join(char for char in strList if char not in 'aeiou')
# Hard coded 2d arrays --> nested = [[1,2,3], [1,2,1]]
# maze = [[num for num in range(0,2)] for value in range(0,2)]

# Dictionaries/Maps can be used just like in JS. something = {"hey": True}
# Can be used with 'dict' --> map = dict(name="myId") --> {"name": "myId"}
# Can be accessed like in JS with dynamic key --> map['name'] --> "myId"
# for myVal in map.values():
# for k in map.keys():
# for k,v in map.items(): 

import random

def printer():
    myList = [1,2,3, 'hey']
    strList = str(myList)
    myOptList = []

    dec = 12321312
    integer = int(dec)


    color = input()
    if (color == 'blue'):
        print('nice I guess')
    elif (color == 'black'):
        print('yeah why not')
    elif (not color):
        print('null?')    
    else:
        print('wut')

    if (color):
        for char in color:
            print(char)

    if (len(myList) > 0):
        for item in myList:
            if (isinstance(item, str)):
                print(item)
                myOptList.append(item)

    print(type(color))        
    print(myOptList)
  
def dicts():
    myObj = {}
    limit = 100
    counter = 0
    while (counter < limit):
        counter += 1
        myObj["prop%s"%(counter)] = [{"internal%s"%(counter+1): random.randint(0, 100)}]

    return myObj 

def lists():
    myList = []
    limit = random.randint(50,100)
    counter = 0    
    while (counter < limit):
        myList.append({"prop": random.randint(0,1000)})
        counter += 1
    return myList    

def separatePairs(arr):
    "separate pairs and odds from a weird tuple"
    arg = str(type(arr))
    pairs = []
    odds = []
    if "list" in arg:
        print('TYPE_OK')
        for i in arr:
            if i["prop"] and (i["prop"] % 2) == 0:
                pairs.append(i)
            else: odds.append(i)
        return {"odds": odds, "pairs": pairs}

    else: print('TYPE_NOT_OK')    
    return None


myList = lists()
result = separatePairs(myList)
print(len(result["pairs"]), len(result["odds"]))


