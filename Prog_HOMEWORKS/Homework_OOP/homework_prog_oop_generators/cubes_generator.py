
num = int(input('Number: '))
expression = (item ** 3 for item in range(2, num))
res = list(expression)
