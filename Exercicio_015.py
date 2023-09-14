"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês.
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
1) salário bruto.
2) quanto pagou ao INSS.
3) quanto pagou ao sindicato.
4) o salário líquido.
Calcule os descontos e o salário líquido, conforme a tabela abaixo:
            + Salário Bruto : R$
            - IR (11%) : R$
            - INSS (8%) : R$
            - Sindicato ( 5%) : R$
            = Salário Liquido : R$
"""
# Outro desafio... 

salario_hora = float(input("Quanto você ganha por hora?")) # input variavel quanto se ganha por hora
salaraio_bruto = round(salario_hora * 220, 2) # valor total sem descontos, bruto
#A legislação brasileira reconhece que o mês comercial tem cinco semanas. Isso significa que o trabalhador com jornada de 44 horas semanais soma 220 ao final de cada mês.

text = "+ Salário Bruto: R$:" #texto explicatorio
print(text, salaraio_bruto) #primeira saida

ir = round(salaraio_bruto * 0.11, 2) #calculo do Imposto de Renda, ir
text = "- IR (11%): R$ " #texto explicatorio
print(text, ir) #segunda saida


inss = round(salaraio_bruto * 0.08, 2) #calculo do valor do INSS
text = "- INSS (8%): R$ "#texto explicatorio
print(text, inss) #terceira saida

sind = round(salaraio_bruto * 0.05, 2) #calculo do valor do sindicato
text ="- Sindicato (5%): R$ " #texto explicatorio
print(text, sind) #quarta saida

liquido = round(salaraio_bruto - ir - inss - sind, 2) #calculo do Salario liquido, debitado os valores: INSS, sindicato e IR
text = "= Sálario liquido: R$ " #texto explicatorio
print(text, liquido) #quinta saida

"""
Obitive a seguinte saida para um valor de 5.71:

Quanto você ganha por hora?5.71
+ Salário Bruto: R$: 1256.2
- IR (11%): R$  138.18
- INSS (8%): R$  100.5
- Sindicato (5%): R$  62.81
= Sálario liquido: R$  954.71

Conforme pode-se notar o quesito apresenta muito texto mas consegui resolver de forma até simples.
"""
