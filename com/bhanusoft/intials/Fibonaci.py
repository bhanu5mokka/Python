num1=0
num2=1
print(num1,num2,end=',')
for i in range(10):
  num3=num1+num2
  num1=num2
  num2=num3
  if i==9:

      print(num3, end='.')

  else:
      print(num3, end=',')


