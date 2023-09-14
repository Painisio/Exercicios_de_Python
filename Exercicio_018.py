"""
Faça um programa que peça o tamanho de um arquivo para download (em MB) e a velocidade de um link de Internet (em Mbps),
calcule e informe o tempo aproximado de download do arquivo usando este link (em minutos).
"""

MB = int(input("Informe o Tamanho do Arquivo em MB: ")) #input variavel tamanho do arquivo
net = int(input("Qual a velocidade da sua Internet em Mbps: ")) #input variavel tamanho da "banda" de internet

mb = MB * 8 #conversão de medidas MB pra mb
tempo_donwload = round((mb/net)//60) #calculo do tempo necessário

#respectivos textos necessários
txt = "tempo de donwload:"
txt1 = "minutos, aproximadamente."

#saída
print(txt, tempo_donwload, txt1)

"""
Obtive as seguintes saidas deste código:

Informe o Tamanho do Arquivo em MB: 10000
Qual a velocidade da sua Internet em Mbps: 300
tempo de donwload: 4 minutos, aproximadamente.
"""
