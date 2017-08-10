valor = input('Digite um Valor Qualquer: ')

if valor.isnumeric():
    print('É um Número')

if valor.isalpha():
    print('É Letra')

if valor.isalnum():
    print('É Alfanumerico')

if valor.isdecimal():
    print('É Decimal')

if valor.islower():
    print('Está em minusculo')

if valor.isupper():
    print('Está em maiusculo')

print('Pode implementar outras verificações com base no exemplo...')