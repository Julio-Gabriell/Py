palavra = str(input("Digite uma palavra: "))

quantidade = 0

for letra in palavra:
  if letra == "a":
    quantidade += 1

print(f"A quantidade de a é igual a: {quantidade}")