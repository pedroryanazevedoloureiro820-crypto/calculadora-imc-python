#recebimento de informações
altura=float(input('Digite sua altura em metro:'))
peso=float(input('Digite seu peso em kilos:'))

#Calculo da informação
imc=peso/(altura**2)

#Redistribuição de resultados
if imc<18.5:
    print('{}Você está abaixo do peso esperado{}'.format('\033[4;31m','\033[m'))
elif imc>18.4 and imc<25:
    print('{}Você está no peso ideal!{}'.format('\033[0;32m','\033[m'))
elif imc>24 and imc<30:
    print('{}Você está com sobrepeso.{}'.format('\033[1;33m','\033[m'))
elif imc>29 and imc<41:
    print('{}Você está com obesidade{}'.format('\033[1;31m','\033[m'))
else:
    print('{}Você está com obesidade mórbida{}'.format('\033[4;31m','\033[m'))