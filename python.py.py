nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
nota4 = float(input('Quarta nota: '))
faltas = float(input('Números de Faltas: '))

media = float(nota1+nota2+nota3+nota4) / 4

if faltas >= 3:
    print('O aluno está REPROVADO por faltas.')
else:
    if media >= 7:
        print('O aluno está APROVADO.')
    elif 5 <= media < 7:
        print('O aluno está em RECUPERAÇÃO.')
    else:
        print('O aluno está REPROVADO.')
