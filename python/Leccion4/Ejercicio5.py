'''Calcular el factorial de im mi,erp ,ayor o igual a 0'''

num = int()
i = int()
factorial = int()
while True:
    print("digite un numero: ")
    num = int(input())
    if num >= 0:
        break
i = 1
factorial = 1
while i <= num:
    factorial = factorial * i
    i = i + 1
print("factorial: ", factorial)