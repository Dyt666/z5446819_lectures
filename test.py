numbers = [3,9,1,5,7,2,11,0,3,12,3,15]

max=numbers[0]
for i in range(0,len(numbers)):
  if numbers[i]>=max:
    max=numbers[i]
print(max)

print(f'The largest number is {max}')

# Nested for loop
for i in range(1,4):
   for j in range(1,4):
       if i <= j:
        print(i,j)


for odd in range(1, 10, 2):
    print(odd)

for odd in range(1, 10, 2):
    for even in range(0, 10, 2):
        if even > 2:  #will always stop at 4
            break
    print(even, odd)


for even in range(0,10,2):
    print(even)
    if even>2:
        break # 0 2 4

for even in range(0,10,2):
    print(even)
    if even>2: # 0 2 4 6 8
        continue
print(even)

for even in range(0, 10, 2):
    if even > 2:
        continue
print(even)

