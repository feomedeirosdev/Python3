# Ex015 - Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.

print("")
km = float(input("Quantos quilômetros foram percorridos? "))
dias = float(input("Quantos dias o carro ficou alugado? "))
print("")
print(f"O custo por {dias:.0f} dias de aluguel é de R$ {(dias * 60):.2f}")
print(f"O custo por {km} quilômetros rodados é {(km * 0.15):.2f}")
print(f"Logo o valor total a ser cobrado será de R$ {((dias * 60) + (km * 0.15)):.2f}\n")