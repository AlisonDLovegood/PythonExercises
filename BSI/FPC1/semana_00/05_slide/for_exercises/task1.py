"""
    Uma fábrica tem 10 representantes. Cada um recebe uma comissão calculada a partir do número de itens de um pedido, segundo os seguintes critérios:
        – para até 19 itens vendidos, a comissão é de 10% do valor total do pedido;
        – para pedidos de 20 e 49 itens, a comissão é de 15% do valor total do pedido;
        – para pedidos de 50 a 74 itens, a comissão é de 20% do valor total do pedido;
        – para pedidos iguais ou superiores, a 75 itens a comissão é de 25%.
    Faça um programa que lê a quantidade de itens de pedidos de cada representante e imprime o percentual de comissão de cadaum.
"""


def comissao(q_pro_v, q_por_v):
    for i in range(len(q_pro_v)):
        if q_pro_v[i] <= 19:
            q_por_v.append('10%')
        elif q_pro_v[i] <= 49:
            q_por_v.append('15%')
        elif q_pro_v[i] <= 74:
            q_por_v.append('20%')
        else:
            q_por_v.append('25%')
    return q_por_v


qtd_pro_vend, qtd_por_vend = [], []
print('=================================================')
for i in range(10):
    qtd_pro_vend.append(
        int(input(f'Quantidade de produtos vendidos pelo vendedor {i+1}: ')))

qtd_por_vend = comissao(qtd_pro_vend, qtd_por_vend)

print('-------------------------------------------------')
for i in range(len(qtd_por_vend)):
    print(
        f'Porcentagem de comissão do vendedor {i+1}: {qtd_por_vend[i]}')
