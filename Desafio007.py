n1 = float(input('Digite a nota do aluno: '))
n2 = float(input('Digite a segunda nota do aluno: '))
m = (n1+n2)/2
if m < 7:
    print(f'A nota média deste aluno é de \33[1:31:107m{m:.2f}\33[m')
else:
    print(f'A nota média deste aluno é de \33[1:32:107m{m:.2f}\33[m')