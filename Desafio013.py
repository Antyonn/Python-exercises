f = str(input('Digite o nome do funcionário: '))
n = float(input('Digite o salário: '))
r = n+(n*15/100)
print(f'O salário do funcionario {f} que era de R${n:.2f} foi aumentado para R${r:.2f}')