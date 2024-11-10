num = [1,3,5,6]

result = [1] * len(num)

prefix = 1

for i in range(len(num)):
    result[i] = prefix
    prefix *= num[i]

postfix = 1
for i in range(len(num)-1,-1,-1):
    result[i] *= postfix
    postfix *= num[i]
print(result)