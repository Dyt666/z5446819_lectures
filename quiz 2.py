print('some text'.strip(None))

print('some text'.strip)
print('some text'.strip(''))

print('some text'.strip('some text'))

print('some text'.strip())

w = "What"
i = "IS"
c = "CamelCase?"
print('{}{}{}'.format(w, i.lower(),c))
print('{}{}{}'.format(w, i.lower,c))
print('{}{}{}'.format(w,i,c).lower())

asx_value =7111.4
print(type(asx_value))

date = "2021-01-25"
print(type(date))

units = 1
print(type(units))

currency = "AUD"
print(type(currency))

print(f"The closing value of {units} unit of the All Ordinaries on {date} was {asx_value} {currency}.")

import yfinance as yf
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yf.download(tic, start, end)
print(df)
df.to_csv('qan_stk_prc.csv')

import yfinance
tic = "QAN.AX"
start = '2020-01-01'
end = None
df = yfinance.download(tic, start, end)
print(df)
df.to_csv('qan_stk_prc.csv')

import yfinance
tic = "QAN.AX"
start = '2020-01-01'
df = yfinance.download(tic, start, None)
print(df)
df.to_csv('qan_stk_prc.csv')

import yfinance as df
df.download("QAN.AX", '2020-01-01', None).to_csv('qan_stk_prc.csv')

b = 'problem'
a = f'this is called {b}'
a =f'{a} Parsons {b}'
b = print
b(a)

list = [1,1,2,3,4,4]
print(list)

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(l[2:10])
print(l[2:])
print(l[2:11])

t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(t[-8:])
print(t[-8:12])
print(t[-8:10])

l = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
print(l[1:4])
print(l[-9:-6])
print(l[-9:-7])

t =('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j')
print(t[:5])
print(t[:-5])
print(t[:-6])

dic0 = {'a': 1, 'b': 2, 'c': 3}
dic1 = dic0.update({'a': 0, 'd': 4})
number_of_keys = len(dic0)
print(f"dic1 has {number_of_keys} keys")

print(dic0['a'])
dic0[0]
pring(dic0[0])


dic = { ('a', 'b'): 1, 'c': 2, }
print(dic)

tup = (1, 2, ('a', 'b'))
dic = {tup: 'value'}
print(dic)

