import PySimpleGUI as sg
theme = sg.theme('Reddit')

def janela_usuario():
    global theme
    layout=[
        [sg.Text('Usuario',size=(8,1)), sg.Input(key='user', size=(16,1), do_not_clear=False)],
        [sg.Button('Confirmar',size=(7,1)),sg.Button('Cancelar',size=(6,1), button_color='red'), sg.Button('Cadastrar',size=(7,1), button_color='green')],
        [sg.ProgressBar(max_value=10000, orientation='h', size=(15.8, 16), key='progress_1')]
    ]
    return sg.Window('Painel de Usuario', layout=layout, finalize=True)

def janela_senha():
    global theme
    layout = [
        [sg.Text('Senha',size=(8,1)), sg.Input(key='pass',size=(8,1))],
        [sg.Button('Login',size=(8,1)), sg.Button('Cancelar',size=(8,1), button_color='red')]
    ]
    return sg.Window('Painel de Usuario', layout=layout, finalize=True)

def programa_principal():
    global theme
    frame_geral = [
        [sg.Text('Titulo Geral: ', size= (10,1)),sg.Input(key='geral_lable')],
        [sg.Text('Função: ' , size= (10,1)),sg.Input('x',key='function_give')],
        [sg.Text('Largura: ', size=(15,0)),sg.Slider(range=(1,16), default_value=6, orientation='horizontal', key='c')],
        [sg.Text('Altura: ', size=(15,0)),sg.Slider(range=(1,16),default_value=6, orientation='horizontal', key='l')]
    ]

    frame_eixos = [
        [sg.Text('Titulo (Y): '), sg.Input(key='y_label')],
        [sg.Text('Titulo (X): '), sg.Input(key='x_label')],
        [sg.Text('X(inicial): ', size=(15,0)),sg.Slider(range=(-30,30), default_value=0, orientation='horizontal',key='x_rangemin')],
        [sg.Text('X(final): ', size=(15,0)),sg.Slider(range=(-30,30),default_value=10, orientation='horizontal',key='x_rangemax')]
        ]

    frame_extras = [
        [sg.Checkbox('Arredondada', default=False, key='around')],
        [sg.Slider(range=(0,4), resolution=.5, default_value=2, orientation='horizontal', key='line_g')],
        [sg.ColorChooserButton('Escolha a sua cor',target='color_graph'),sg.Input('',key='color_graph', visible=False)]
    ]

    frame_final=[
        [sg.Button('Confirmar', size=(18,0)), sg.Button('Cancelar', size=(18,0))]
    ]

    layout=[
        [sg.Frame('Configurações Gerais', frame_geral, font='Any 12', title_color='black', element_justification='center')],
        [sg.Frame('Configurações do Eixo X', frame_eixos, font='Any 10', title_color='blue', element_justification='center')],
        [sg.Frame('Configurações Adicionais', frame_extras, font='Any 10', title_color='red', element_justification='center')],
        [sg.Frame('', frame_final, element_justification='c')]
    ]
    return sg.Window('Painel de Configuração', layout=layout, element_justification='center',  finalize=True)

def janela_cadastro():
    global theme
    layout=[
        [sg.Text('Usuario: ',size=(8,1)), sg.Input('',size=(8,1),key='new_user')],
        [sg.Text('Senha: ',size=(8,1)), sg.Input('',size=(8,1), key='new_pass')],
        [sg.Button('Login'), sg.Button('Retornar'), sg.Button('Cancelar')]
    ]
    return sg.Window('Painel de Cadastro', layout=layout, element_justification='center',  finalize=True)
