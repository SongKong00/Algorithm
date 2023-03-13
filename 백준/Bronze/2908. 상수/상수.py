num1, num2 = (input().split())
num1_list = list(num1)
num2_list = list(num2)

num1_list = int("".join(num1_list[::-1]))
num2_list = int("".join(num2_list[::-1]))

print(max(num1_list, num2_list))