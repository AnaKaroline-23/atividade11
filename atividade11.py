# Crie um programa que receba a idade de uma pessoa e classifique-a de acordo com as seguintes faixas etárias:
# Criança (0-12 anos)
# Adolescente (13-17 anos)
# Adulto (18-59 anos)
# Idoso (60 anos ou mais)

idade = int(input("digite sua idade!:"))
if(idade<=12):
    print ("criança")

elif(idade<=17) and (idade>=13):
    print ("adolescente")

elif(idade>=18) and (idade<=59):
    print ("Adulto")

elif(idade>=60):
    print("Idoso")
    


