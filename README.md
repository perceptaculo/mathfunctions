# mathfunctions

Meu maior projeto até então, conta com um sistema de login com a base de dados em excel e que possui função de cadastro e login, ao passar pelo sistema de login, o usuário é retornado ao programa principal, onde ele escreve e retorna todas as informações de seu gráfico. Obs: Esse software foi totalmente desenvolvido para a otimização na criação de gráficos matemáticos genéricos e a personalização do gerador por estes, não é necessário nenhum conhecimento em python para utiliza-lo.

Elementos dinâmicos na hora de gerar o gráfico:

1. Tamanho da janela que irá ser gerada concomitantemente ao gráfico.
2. Lei de função, possui tratamento minucioso na entrada de dados, então a escrita da função é totalmente simples e usual - contendo as funções trigonométricas e outras.
3. Espessura da função, isto é, a espessura da linha que irá ser gerada como representação dessa função.
4. Cor do gráfico, isto é, a cor da linha.
5. Titulo do Eixo X -> Titulo que segue o eixo das abcissas
6. Titulo do Eixo Y -> Titulo que segue o eixo das ordenadas
7. Titulo Geral -> Titulo geral do gráfico
8. Range do x -> É possível escolher o domínio de visualização do eixo x, ou seja, de onde iniciará o gráfico no eixo x e até onde irá, com isso gerar o gráfico da função em qualquer domínio de x.
9. Arredondamento -> É possível fazer uma linearização de qualquer função, se esta função for desmarcada, para fins didáticos e outros.

## Para programadores:
1. Sistema de login com acesso ao bando de dados em excell -> Extração dos dados de usuário em um dict() utilizando a biblioteca pandas.
2. Sistema de Interface GUI -> Criação das janelas utilizando a biblioteca PySampleGui e seus recursos, como: ProgressBar e Slider
3. Sistema de tratamento de entrada -> Tratamento minucioso da função recebida pela key='function_give', de forma que o python interprete a função como algebra e não como str. (utilização da função eval())
4. Sistema de gerador de gráficos -> Gerador do gráfico da função com integração ao matplotlib.pyplot, foi optado por permanecer a janela do gráfico ao exterior da GUI, por limitações da própria biblioteca PySampleGUI.
5. Sistema de Otimização Algébrica -> Os valores dos eixos são armazenados em listas e estas listas são tratadas via numpy e spicy, de modo que o y gerado seja curvilíneo e siga com fidelidade o seu comportamento.
6. Sistema dinâmico de funções -> Possibilidade da adesão de outros tipos de função, como funções hiperbólicas e outras - foi optado por manter apenas as clássicas por
motivos pessoais.
7. Sistema Switch Theme -> Possibilidade da troca de tema do GUI a qualquer momento, de padrão vem sg.theme = 'Reddit', entretanto mudando a única variável str todas as funções se alteram, por consequências do escopo do global theme inserido em todos objetos de janela.

## Futuros Updates:
1. Acesso a um banco de dados via github e googlesdk;
2. Integração do GUI Pyplot ao GUI interno;
3. Aceitação de Funções Tridimensionais;
4. Inteligência artificial na adesão das funções.
