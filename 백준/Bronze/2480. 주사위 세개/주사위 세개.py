num1, num2, num3 = input().split()
num1 = int(num1)
num2 = int(num2)
num3 = int(num3)
prize = 0
high = 0

if(num1 == num2 == num3) : prize = 10000 + (num1 * 1000)
elif(num1 == num2 or num1 == num3) : prize = 1000 + (num1 * 100)
elif(num2 == num3) : prize = 1000 + (num2 * 100)
else : 
    if(num1 >= num2 and num1 >= num3) : prize = num1 * 100
    elif(num2 >= num1 and num2 >= num3) : prize = num2 * 100
    else : prize = num3 * 100
       
print(prize)