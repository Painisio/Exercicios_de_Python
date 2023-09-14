"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para controlar o rendimento diário de seu trabalho.
Toda vez que ele traz um peso de peixes maior que o estabelecido pelo regulamento de pesca do estado de São Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. 
João precisa que você faça um programa que leia a variável peso (peso de peixes) e calcule o excesso.
Gravar na variável excesso a quantidade de quilos além do limite e na variável multa o valor da multa que João deverá pagar. 
Imprima os dados do programa com as mensagens adequadas.
"""

# Essa questão me foi apresentada como um desafio.

peso = float(input("Pesagem dos Pescados:")) # input da primeira variavel
txt1 = "Reais" # Texto, moeda corrente
txt2 = "Quilos" # Texto, peso

# Usando de uma condicional (If) resolvi a questão da seguinte forma:

if peso > 50: # Verificando exceente
  excedente = 50 - peso # calculando excedente
  multa = round(-excedente * 4.00, 2) # calculando multa aplicavel
  
  txt3 = "A pesca excedeu em: " # textinho 3
  print(txt3, -excedente, txt2) # saída
  
  txt4 = "A Multa foi avaliada em: " # textinho 4
  print(txt4, multa, txt1) # saida
else:
  print("Não ouve pesca excedente!")

"""
Quando respondi a questão, no ano passado, eu não consderei uns pontos:
1) A existencia de ser "inputado" um valor inferior ou igual a 50, não correndo o resto do código e
consequentemente não existindo saída a ser apresentada. Dai atualizei o código e adicionei o "else", surgindo assim
uma resposta caso não exista excedente!

2) Na versão original na linha 21 e na linha 24 tinham a mesma variavel: "txt", consequencia o valor era atualizado perdendo-se o 
conteudo da linha 21. Resolvi tornando cada varivel das linhas supracitdas independentes, no caso: "txt3" e "txt4". Assim caso precise
pode-se reutilizar seus vaores a vontade!
"""
