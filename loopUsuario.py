inicioLoop = int(input("Informe o numero que o loop ira iniciar: "))
fimLoop = int(input("Informe o numero que o loop ira terminar: "))

somaImpar = 0
somaPar = 0
soma = 0

while inicioLoop <= fimLoop:
  soma = soma + inicioLoop
  if inicioLoop % 2 == 0:
    somaPar = somaPar + inicioLoop
  else:
    somaImpar = somaImpar + inicioLoop
  inicioLoop += 1
print(f"A soma de todos os numeros pares são: {somaPar}, a soma dos numeros impares são: {somaImpar} e a soma de todos os numeros são {soma}")