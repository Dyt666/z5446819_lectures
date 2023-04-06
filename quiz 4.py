# Code 1

def process_string(s):
    lst = list(s.lower().split(" "))
    return lst

print(process_string("This is my test String"))



def process_string(s):
    Lst = s.split()
    for i, word in enumerate(Lst):
        Lst[i] = word.lower()
    return Lst

print(process_string("This is my test String"))






# Code 2

def process_string(s):
    lst = s.split()
    for i, word in enumerate(lst):
        if i % 2 ==0:
            lst[i] = word.lower()
        else:
            lst[i] = word.upper()
    return lst

print(process_string("This is my test String"))


def process_string(s):
    l = []
    for n, word in enumerate(s.split()):
        if n % 2 == 0:
            l.append(word.lower())
        else:
            l.append(word.upper())
    return l
print(process_string("This is my test String"))


# Code 3
def fizz_buzz_sumz(i):
    sum = 0
    for x in range (1, i+1):
        if x%3==0 and x%5==0:
            continue
        elif x%3 == 0:
            sum += 3 * x
        elif x%5 == 0:
            sum += 5 * x
        else:
            sum += x
    return sum

i = 10
print(fizz_buzz_sumz(i))

def my_function(x):
    x = x + 1
    return x

x = 3
my_function(x)
print(x)
print(my_function(x))

def my_function(x):
    x = x + 1
    return x

x = 3
x = my_function(x)
print(x)

def my_function(y):
    y = y + x
    x = 2
    y = y + x
    return y

x = 3
y = 10
y = my_function(x)
print(y)



