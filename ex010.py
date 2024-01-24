# Crei um programa que leia quanto de dinheiro uma pessoa
# tem na carteira e mostre quantos dolares ela pode comprar.
#considere US$ 1,00 = R$ 3,27
n1 = float(input('Digite o valor em real: R$ '))
d = n1 / 3.27
print('Tenho na carteira R$ {:.2f}, vale \033[4;34mUS$ {:.2f}\033[m em dolar.' .format(n1 , d))
