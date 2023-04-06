# In-class Exercise1

def evennumber(list):
    list1=[]
    for i in list:
        if i%2==0:
            list1.append(i)

    return list1
list2=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 20, 22, 23, 25, 29, 30, 31]
print(evennumber(list2))

test_list = [0,1,2,3,4,5,6,7,8,9,10,20,22,23,25,29,30,31]

def evennumber(lis):
    list1 = []
    for i in lis:
        if 1%2==0:
            list1.append()
    return list1
evennumber(test_list)


# In-class exercise 2.1: List comprehension
# please use list comprehension to construct a list from the squares of each element in the following list
# only if the value of the square is greater than 150
lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
newlst = [x**2 for x in lst if x**2>150]
print(newlst)


lst = [2, 3, 10, 14, 20, 21, 25, 13, 15]
squares = [x**2 for x in lst if x**2 > 150]
print(squares)


# In-class exercise 2.2: Set comprehension
numbers = [0,1,1,2,5,6,8,2,4,6,8]
# Use a comprehension to create a list of unique integers that exist in numbers and are divisible by 2:
result = list({i for i in numbers if i%2 == 0})
result = [i for i in set(numbers) if i%2 == 0]

result.sort()
print(result)


#同学attempt1
numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
evens = set([num for num in numbers if num % 2 == 0])
print(evens)

#同学attempt2
numbers = [0, 1, 1, 2, 5, 6, 8, 2, 4, 6, 8]
result = list(set(num for num in numbers if num % 2 == 0))
print(result)

footballers_goals = {'Eusebio': 120, 'Cruyff': 104, 'Pele': 150, 'Ronaldo': 132, 'Messi': 125}

sorted_footballers_by_goals = sorted(footballers_goals.items(), key=lambda x:x[1])
print(sorted_footballers_by_goals)





