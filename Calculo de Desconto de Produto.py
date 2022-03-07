n = float(input('Digite o preço: '))
liq = n - (n * 5 / 100)
print(f'O preço digitado é R${n:.2f}. O novo preço deste produto com desconto é de R${liq:.2f}')
