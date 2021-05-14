decimal = int(input("Digite um número decimal: "))
choice = int(input("Deseja fazer qual conversão? \n (1) Binário \n (2) Hexadecimal \n (3) Octal \n Escolha: "))
hex = [0,1,2,3,4,5,6,7,8,9,"A","B","C","D","E","F"]
result = []
index = 1
value = 0

if choice == 1:
  if decimal == 00:
    print("Não é possivel fazer a conversão")
  else:
  # Decimal to binary
    binario = ''
    while (decimal > 1):
      resto = decimal % 2
      decimal = int(decimal / 2)
      print(binario)
      binario += str(resto)
    binario += '1'
    print("O resultado da conversão é: ", binario[-1::-1])

elif choice == 2: 
  # Decimal to hexadecimal
  if decimal == 00:
    print("Não é possivel fazer a conversão")
  else:
    while decimal > 0:
      result.append(hex[(decimal % 16)])
      decimal = decimal // 16
    for i in range(len(result)-1,-1,-1):
      print(result[i],end="")

elif choice == 3:
  # Decimal to octal
  if decimal == 00:
    print("Não é possivel fazer a conversão")
  else:
    while decimal > 0:
      value += (decimal % 8) * index
      decimal = int(decimal / 8)
      index = index * 10
    print("O resultado da conversão é: ", value)

else:
  print("Opção inválida")
