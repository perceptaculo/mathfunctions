import PySimpleGUI as sg #inicialização da IDE
import windows #inicialização da GUI
import pandas as pd #Banco de Dados
import mathgraph #Gráfico 
from time import sleep #Loading

#userlist
df = pd.read_excel('dados.xlsx') 
user_list = list()
user_info = dict()
nome_list = list()

for c in range(0,len(df)):
    user_info[df['user'][c]] = df['pass'][c]

#Definindo o estado das janelas
janela1, janela2, janela3, janela_cadastro = windows.janela_usuario(), None, None, None

while True: #iniciando o loop da janela
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Cancelar':
        break


    if window == janela1:
        for k, v in user_info.items():
            nome_list.append(k)

        if event == 'Confirmar': 
            if values['user'] in nome_list:
                for i in range(10000):
                    janela1['progress_1'].UpdateBar(i + 1) #update dos valores da barra
                sg.popup(f'O {values["user"]} foi identificado pelo sistema!')
                senha = user_info[values['user']]
                janela1.hide()
                janela2 = windows.janela_senha()
                window = janela2    
            else:
                sg.popup('Seu usuário não foi identificado pelo sistema!')

        if event == 'Cadastrar':
            janela1.hide()
            janela_cadastro = windows.janela_cadastro()
            window = janela_cadastro


    if window == janela_cadastro:
        if event == 'Login':
            if values['new_user'] in nome_list:
                sg.popup('Já existe esse usuário no sistema!')
            else:
                dfnew = df.append( {'user':f'{values["new_user"]}','pass':f'{values["new_pass"]}'}, ignore_index=True )
                dfnew_2 = dfnew.dropna(how='any')
                dfnew_2.to_excel('dados.xlsx', index=False)
                janela_cadastro.hide()
                janela3 = windows.programa_principal()
                window = janela3

        if event == 'Retornar':
            janela_cadastro.hide()
            janela1 = windows.janela_usuario()
            window = janela1


    if window == janela2:
        if event == 'Login':
            if str(values['pass']) == str(senha):
                janela2.hide()
                janela3 = windows.programa_principal()
                window = janela3
            else:
                sg.popup('Você digitou uma senha incorreta!') 


    if window == janela3:
        if event == 'Confirmar' and values['function_give'] != '':
            mathgraph.mathgraph(values['c'], values['l'], values['function_give'], values['around'], values['line_g'], 
            values['color_graph'], values['x_label'], values['y_label'], values['geral_lable'], values['x_rangemax'],
            values['x_rangemin'])

        if event ==  'Confirmar' and values['function_give'] == '' and values['function_give'] == 0:
            sg.popup('Digite alguma função válida!')

    #params: c,l,function_give,around, line_g, color_graph, x_label, y_label, geral_label, x_rangemax, x_rangemin

    #Updates:
    # -> Aprimoramento de Design
    # -> Só usar os dados da nuvem

    

                    
                    
                
