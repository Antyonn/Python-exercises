comb = str(input('O combustível é Etanol ou Gasolina? '))
if (comb == 'Gasolina') or (comb == 'Etanol'):
    fuel = int(input('Digite a quilometragem do último abastecimento: '))
    fuel2 = int(input('Digite a quilometragem do novo abastecimento: '))
    litros = float(input('Quantos litros foram abastecidos? '))
    media = (fuel2 - fuel) / litros
    print(f'Você abasteceu o seu veículo com {comb} e a média conforme o último abastecimento foi de {media:.2f}Km/L')
else:
    print('Por favor, digite o combustível Etanol ou Gasolina')
