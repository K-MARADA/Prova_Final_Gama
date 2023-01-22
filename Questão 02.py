import os
os.system("cls")

print("••• Q U E S T Ã O   0 2 •••\n")
while True:
        numero=input("► Digite um nÚmero (\033[93m<Enter>\033[m para sair\033[m): ")
        if not numero.isnumeric():
            print("Fim\n")
            break
        numero=int(numero)
        print("")

        if numero < 10:
            print("\033[93m> O número é menor do que 10.\033[m")
        if (numero % 2)==0:
            print("\033[93m> O número é par.\033[m")
        if numero >=8 and numero <= 16:
            print("\033[93m> O número está entre 8 e 16.\033[m")
        if numero ==51 or numero ==80:
            print("\033[93m> O número é 51 ou 80.\033[m")
        if numero ==101:
            print("")
        
        print("")