

String1 ='''John said:"Let's learn Python together"'''
print(String1)

f = 0.2 + 0.2 +0.2
print (f)
print(f==0.6) # False if print(f==0.6)

# Comparison of numerical values
# Try it!
i = 1
test = i == 1   # --> True
print(test)

print ("1" + "1" + "1")

x = 1
print(x)

x = str.upper('abc')
print(x)            # --> 'ABC'
y = 'abc'.upper()
print(y)            # --> 'ABC'


import yfinance                                           # (1)
tic = "QAN.AX"                                            # (2)
start = '2020-01-01'                                      # (3)
end = None                                                # (4)
df = yfinance.download(tic, start, end, ignore_tz=True)   # (5)
print(df)                                                 # (6)
df.to_csv('qan_stk_prc.csv')                              # (7)

x = str(5)
print(x) # --> '5'


# Create a variable called "str", overwriting the built-in method
str_1 = "very bad idea!"

# Trying to use the function `str` again will raise an exception
x = str(5)

width = 33
length = 56
height = 30.5
volume = width * length *height
print (volume)
print(f"The volume is {volume} cm  ")

list = [2,3,4]



lst = [1,"string", True, None, True]
# if remove the True, in python, True is denoted as 1, hence the value of True = 1
# so if remove the True, we remove a value of 1
# special case should be aware of

lst = ["From", "firstname.surname","@","unsw.edu.au","Time", "year"]
print(f"The domain name is {lst[3]}")

#In class exercise 3
line = 'From nickname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'
domain = line.split()[1].split('@')[1]
print(domain)


# tuples and list is different in bracket
# Create a tuple with two elements
tup = (1, 2)

# unpack the tuple into two variables:
(a, b) = tup

# print
print(f"`a` is {a} and `b` is {b}")