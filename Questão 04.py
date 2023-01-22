import os
os.system("cls")

print("••• Q U E S T Ã O   0 4 •••\n")

sair=False
def recebe_parametros(parm_1, parm_2):
    resultado = parm_1 + "," + parm_2    
    return resultado

def entrada_de_parametros():
    global sair
    
    parm_1 = input("► Digite o 1º parâmetro (\033[93m<Enter>\033[m para sair\033[m): ")
    parm_2 = input("► Digite o 2º parâmetro (\033[93m<Enter>\033[m para sair\033[m): ")
    
    if parm_1 == "" or parm_2 =="": 
        print("Fim\n")
        sair=True
        return

    resultado=recebe_parametros(parm_1, parm_2)
    print (F"\033[93m \n> Resultado da concatenação: {resultado} \033[m \n")

while not sair:
    entrada_de_parametros()
