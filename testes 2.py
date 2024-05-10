Nome = input('Olá ! Qual seu nome?')
print('Parabéns', Nome,'você ganhará um prêmio se acertar tudo! ')
print('Vamos Começar Logo !!')
a = input('Digite algo numérico:')
print(a.isnumeric())
b = input('Digite algo alfa númerico:')
print(b.isalnum())
c = input('Digite apenas letras:')
print(c.isalpha())
d = input('Escreva somente com letras maiúsculas:')
print(d.isupper())
e = input('Apenas espaço em branco...')
print(e.isspace())
print('PARABÉNS AGORA PEÇA PARA MEU SUBORDINADO'
      + 'CONFERIR AS RESPOSTAS E LHE DAR O PRÊMIO !')

fim = input('Fim');

a = input('Digite algo: ')
print('O tipo primitivo desse valor é ', type(a))
print('Só tem espaços? ', a.isspace())
print('É um número? ',a.isnumeric())
print('É alfabético? ',a.isalpha())
print('É alfanumérico? ',a.isalnum())
print('Está em maiúsculas? ',a.isupper())
print('Está em minúsculas? ',a.islower())
print('Está capitalizada /maiusc. e minusc./ ? ',a.istitle())

fim = input('Fim');
