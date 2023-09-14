"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada.
Considere que a cobertura da tinta é de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00.
Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
Obs.: somente são vendidos um número inteiro de latas.
"""

# DESAFIO
import math # para cumprir com o desafio com eficacia importei a biblioteca matemática do python.
m2 = float(input("Quantos mestros quadrados pretende pintar?")) # input da variavel, em float, da metragem da parede

litro = m2/3 # calculo de litros necessários
q_latas = math.ceil(litro/18) # calculo de latas necessárias
c_paint = round(80.00 * q_latas, 2) # calculo do custo

#respectivos textos a serem apresentados:
t_latas = "Você precisará de: "
latas = "lata(s)."
t_reais = "Irá custar: R$: "

# respectivas saidas a serem apresentadas compilando as informações:
print(t_latas, q_latas, latas)
print(t_reais, c_paint)

"""
Obitive o seguinet resultado:

Quantos mestros quadrados pretende pintar?70
Você precisará de:  2 lata(s).
Irá custar: R$:  160.0
"""
