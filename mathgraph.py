from math import (sin, cos, tan)
import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d

def mathgraph(
    c=6,l=6,function_give=0,around=True, line_g=1, color_graph='black', x_label='Eixo X', y_label='Eixo Y',
    geral_label='Grafico', x_rangemax=100, x_rangemin=0
        ):
    """
    :param c: Comprimento
    :param l: Largura
    :param function_give: Função recebida
    :param around: Arredondamento do y
    :param line_g: Grossura da linha de y
    :param color_graph: Cor da linha de y
    :param x_label: Titulo do Eixo X
    :param y_label: Titulo do Eixo Y
    :param geral_label: Titulo do Grafico
    :param x_rangemax: X final
    :param x_rangemin: X inicial
    :return: retorna o gráfico
    """
    fig = plt.figure(figsize=(c, l))
    pointsy = []
    pointsx = []

    for x in np.arange(x_rangemin, x_rangemax+1):
        x = x
        quase_y = function_give.replace('^','**')
        for i in range(0,len(quase_y)):
            if quase_y[i].isnumeric() and quase_y[i+1].isalpha():
                quase_y = quase_y.replace(f'{quase_y[i]}{quase_y[i+1]}',f'{quase_y[i]}*{quase_y[i+1]}')
        y = eval(quase_y)

        pointsx.append(x)
        pointsy.append(y)

    if color_graph.strip() == '':
            color_graph='black'

    if around == True:
        cubic_interploation_model=interp1d(pointsx,pointsy,kind="cubic")
        xs=np.linspace(x_rangemin,x_rangemax,500)
        ys=cubic_interploation_model(xs)
        plt.plot(xs, ys, lw=line_g, color=color_graph
        )
    
    elif around == False:
        plt.plot(pointsx, pointsy, lw=line_g, color=color_graph)
    
    plt.grid(color='gray', linestyle='-', linewidth=1)
    plt.xlabel(f"{x_label}", fontsize=13)
    plt.ylabel(f"{y_label}", fontsize=13)
    plt.title(f'{geral_label}')
    fig.savefig('grafico.png')
    return plt.show()

