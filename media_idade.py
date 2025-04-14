print("Digite a quantidade de alunos presentes na sua sala:")
alunosQtd = int(input())

contador = 1
somaIdades = 0
idades = 0
mediaIdades = 0

while contador <= alunosQtd:
    print("Digite a idade do aluno: ")
    idades = int(input())
    contador = contador + 1
    somaIdades = idades + somaIdades

mediaIdades = somaIdades / alunosQtd

print(mediaIdades)

