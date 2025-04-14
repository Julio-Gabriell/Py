fim = int(input("Digite o ultimo numero da repetição: "))

x = 1

while x <= fim:
    if x % 2 == 0:
        print(x)
        x += 1
    else: 
        x += 1

print("acabou")