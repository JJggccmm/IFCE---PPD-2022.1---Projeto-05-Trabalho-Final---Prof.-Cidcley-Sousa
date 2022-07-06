#Bibliotecas para manipulação dos arquivos de imagem utilizados no código para poder compactá-los no arquivo .exe quando for construido:
import sys
import os

#Bibliotecas para manipulação e construção da interface gráfica no Tkinter:
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font
from AnimatedGIF import *

def resource_path(relative_path):
    try:
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

"""
*
*       ******************************************************
*  ~~~ Construção de Interface Gráfica com a biblioteca Tkinter ~~~
*       ******************************************************
*
"""

root = Tk()
root.withdraw()

# ABAIXO, AS TELAS DO CHAT DE TUPLAS:

path_img_botao_Entrar_asset = resource_path('recursos/botao_Entrar.png')
img_botao_Entrar_asset = PhotoImage(file=path_img_botao_Entrar_asset, master=root)

path_img_botao_Conversar_asset = resource_path('recursos/botao_Conversar.png')
img_botao_Conversar_asset = PhotoImage(file=path_img_botao_Conversar_asset, master=root)

path_img_botao_mandar_msg_asset = resource_path('recursos/botao_mandar_msg.png')
img_botao_mandar_msg_asset = PhotoImage(file=path_img_botao_mandar_msg_asset, master=root)

path_img_bg_usuario_lobby_asset = resource_path('recursos/bg_usuario_lobby.png')
img_bg_usuario_lobby_asset = PhotoImage(file=path_img_bg_usuario_lobby_asset, master=root)

path_img_bg_usuario_Chat_asset = resource_path('recursos/bg_usuario_Chat.png')
img_bg_usuario_Chat_asset = PhotoImage(file=path_img_bg_usuario_Chat_asset, master=root)

path_img_bg_configurar_Usuario_asset = resource_path('recursos/bg_configurar_Usuario.png')
img_bg_configurar_Usuario_asset = PhotoImage(file=path_img_bg_configurar_Usuario_asset, master=root)

path_img_botao_Conversar_privado_asset = resource_path('recursos/botao_Conversar_privado.png')
img_botao_Conversar_privado_asset = PhotoImage(file=path_img_botao_Conversar_privado_asset, master=root)

path_img_bg_Gera_Usuario_asset = resource_path('recursos/bg_Gera_Usuario.png')
img_bg_Gera_Usuario_asset = PhotoImage(file=path_img_bg_Gera_Usuario_asset, master=root)

path_img_botao_gerar_Usuario_asset = resource_path('recursos/botao_gerar_Usuario.png')
img_botao_gerar_Usuario_asset = PhotoImage(file=path_img_botao_gerar_Usuario_asset, master=root)

path_img_bg_nome_repetido_warning_asset = resource_path('recursos/bg_nome_repetido_warning.png')
img_bg_nome_repetido_warning_asset = PhotoImage(file=path_img_bg_nome_repetido_warning_asset, master=root)

path_img_bg_nome_repetido_sala_warning_asset = resource_path('recursos/bg_nome_repetido_sala_warning.png')
img_bg_nome_repetido_sala_warning_asset = PhotoImage(file=path_img_bg_nome_repetido_sala_warning_asset, master=root)

path_img_botao_Ok_asset = resource_path('recursos/botao_Ok.png')
img_botao_Ok_asset = PhotoImage(file=path_img_botao_Ok_asset, master=root)

path_img_chat_bubble_asset = resource_path('recursos/chat_bubble_ICON.png')
img_chat_bubble_asset = PhotoImage(file=path_img_chat_bubble_asset, master=root)

def janela_Erro_Nome_Repetido_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("**Espaco de Tuplas: Erro!")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("334x178")

    bg_label = Label(newWindow,image = img_bg_nome_repetido_warning_asset, width=334, height=178)
    bg_label.place(x=0, y=0)

    ok_button = Button(newWindow, image=img_botao_Ok_asset,command=lambda:fecha_janela_TOPLEVEL(newWindow))
    ok_button.place(x=107, y=127)

def janela_Erro_Nome_Repetido_Sala():
    newWindow = Toplevel(root)
    newWindow.title("**Espaco de Tuplas: Erro!")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("334x178")

    bg_label = Label(newWindow,image = img_bg_nome_repetido_sala_warning_asset, width=334, height=178)
    bg_label.place(x=0, y=0)

    ok_button = Button(newWindow, image=img_botao_Ok_asset,command=lambda:fecha_janela_TOPLEVEL(newWindow))
    ok_button.place(x=107, y=127)

def janela_Gerar_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("Espaco de Tuplas")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("329x307")

    bg_label = Label(newWindow,image = img_bg_Gera_Usuario_asset, width=324, height=305)
    bg_label.place(x=0, y=0)
    
    gif_bg_asset_url = resource_path('recursos/gifs/icone_inicio.gif') 
    lbl_with_my_gif = AnimatedGif(newWindow, gif_bg_asset_url,0.30)
    lbl_with_my_gif.config(bg='#181a1b')
    lbl_with_my_gif.place(x=118, y=32)
    lbl_with_my_gif.start()

    cria_usuario_button = Button(newWindow, image=img_botao_gerar_Usuario_asset)
    cria_usuario_button.place(x=86, y=223)

def janela_Config_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("Espaco de Tuplas: Usuario")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("457x422")

    bg_label = Label(newWindow,image = img_bg_configurar_Usuario_asset, width=453, height=417)
    bg_label.place(x=0, y=0)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 50,height = 5,font = ("Callibri",9))
    text_area.place(x=40, y=220)
    text_area.focus()

    nome_usuario_text_input = Entry(newWindow)
    nome_usuario_text_input.place(x=33, y=127,width = 385,height = 25)

    sala_de_ENTRADA_text_input = Entry(newWindow)
    sala_de_ENTRADA_text_input.place(x=35, y=359,width = 325,height = 25)

    entrar_button = Button(newWindow, image=img_botao_Entrar_asset)
    entrar_button.place(x=259, y=37)

def janela_Lobby_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("Espaco de Tuplas: Usuario")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("371x362")

    bg_label = Label(newWindow,image = img_bg_usuario_lobby_asset, width=371, height=362)
    bg_label.place(x=0, y=0)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 39,height = 6.5,font = ("Callibri",9))
    text_area.place(x=36, y=140)
    text_area.focus()

    conversa_privada_text_input = Entry(newWindow)
    conversa_privada_text_input.place(x=36, y=295,width = 296,height = 25)

    conversar_button = Button(newWindow, image=img_botao_Conversar_asset)
    conversar_button.place(x=19, y=24)

def janela_Chat_Geral_Usuario():
    newWindow = Toplevel(root)
    newWindow.title("Espaco de Tuplas: Usuario")
    icone_asset_url = resource_path('recursos/icone.ico')
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("371x469")

    bg_label = Label(newWindow,image = img_bg_usuario_Chat_asset, width=371, height=469)
    bg_label.place(x=0, y=0)

    bg_label_nome_cliente = Label(newWindow, text = "Usuario",font = ("Callibri",18, 'bold'))
    bg_label_nome_cliente.config(bg='black')
    bg_label_nome_cliente.place(x=161, y=48)

    chat_bubble_icon_label = Label(newWindow, image=img_chat_bubble_asset)
    chat_bubble_icon_label.config(bg='black')
    chat_bubble_icon_label.place(x=86, y=24)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 39,height = 14,font = ("Callibri",9))
    text_area.place(x=37, y=144)
    text_area.focus()

    msg_text_input = Entry(newWindow)
    msg_text_input.place(x=122, y=403,width = 205,height = 26)

    chat_privado_button = Button(newWindow, image=img_botao_Conversar_privado_asset)
    chat_privado_button.place(x=292, y=103)

    envia_msg_button = Button(newWindow, image=img_botao_mandar_msg_asset)
    envia_msg_button.place(x=42, y=388)

# ABAIXO, AS TELAS DO ESPIÃO:

path_img_bg_espiao_asset = resource_path('recursos/bg_espiao.png')
img_bg_espiao_asset = PhotoImage(file=path_img_bg_espiao_asset, master=root)

path_img_botao_espiao_asset = resource_path('recursos/botao_espiao.png')
img_botao_espiao_asset = PhotoImage(file=path_img_botao_espiao_asset, master=root)

path_img_bg_Insere_Dados_ServidorRPCRMI_asset = resource_path('recursos/bg_Insere_Dados_ServidorRPCRMI.png')
img_bg_Insere_Dados_ServidorRPCRMI_asset = PhotoImage(file=path_img_bg_Insere_Dados_ServidorRPCRMI_asset, master=root)

path_img_botao_abre_Janela_Dados_Servidor_asset = resource_path('recursos/botao_abre_Janela_Dados_Servidor.png')
img_botao_abre_Janela_Dados_Servidor_asset = PhotoImage(file=path_img_botao_abre_Janela_Dados_Servidor_asset, master=root)

path_img_botao_Conectar_asset = resource_path('recursos/botao_Conectar.png')
img_botao_Conectar_asset = PhotoImage(file=path_img_botao_Conectar_asset, master=root)

path_img_bg_IP_SERVIDOR_RPC_INVALIDO_warning_asset = resource_path('recursos/bg_IP_SERVIDOR_RPC_INVALIDO_warning.png')
img_bg_IP_SERVIDOR_RPC_INVALIDO_warning_asset = PhotoImage(file=path_img_bg_IP_SERVIDOR_RPC_INVALIDO_warning_asset, master=root)

path_img_bg_PORTA_SERVIDOR_RPC_INVALIDA_warning_asset = resource_path('recursos/bg_PORTA_SERVIDOR_RPC_INVALIDA_warning.png')
img_bg_PORTA_SERVIDOR_RPC_INVALIDA_warning_asset = PhotoImage(file=path_img_bg_PORTA_SERVIDOR_RPC_INVALIDA_warning_asset, master=root)


def janela_Espiao():
    newWindow = Toplevel(root)
    newWindow.title("Espaco de Tuplas: Espião...")
    icone_asset_url = resource_path('recursos/icone.ico')
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("375x475")

    bg_label = Label(newWindow,image = img_bg_espiao_asset, width=371, height=474)
    bg_label.place(x=0, y=0)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 39,height = 13,font = ("Callibri",9))
    text_area.place(x=37, y=144)
    text_area.focus()

    msg_text_input = Entry(newWindow)
    msg_text_input.place(x=131, y=403,width = 205,height = 26)

    entra_ServidorRPCRMI_button = Button(newWindow, image=img_botao_abre_Janela_Dados_Servidor_asset)
    entra_ServidorRPCRMI_button.place(x=211, y=78)

    config_palavras_suspeitas_button = Button(newWindow, image=img_botao_espiao_asset)
    config_palavras_suspeitas_button.place(x=27, y=376)

def janela_Erro_PORTA_INVALIDA():
    newWindow = Toplevel(root)
    newWindow.title("**Conexão: Erro!")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("338x183")

    bg_label = Label(newWindow,image = img_bg_PORTA_SERVIDOR_RPC_INVALIDA_warning_asset, width=334, height=178)
    bg_label.place(x=0, y=0)

    ok_button = Button(newWindow, image=img_botao_Ok_asset)
    ok_button.place(x=107, y=127)

def janela_Erro_IP_INVALIDO():
    newWindow = Toplevel(root)
    newWindow.title("**Conexão: Erro!")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("338x183")

    bg_label = Label(newWindow,image = img_bg_IP_SERVIDOR_RPC_INVALIDO_warning_asset, width=334, height=178)
    bg_label.place(x=0, y=0)

    ok_button = Button(newWindow, image=img_botao_Ok_asset)
    ok_button.place(x=107, y=127)

def janela_Conectar_Servidor_RPCRMI():
    newWindow = Toplevel(root)
    newWindow.title("**Conexão: Erro!")
    icone_asset_url = resource_path('recursos/icone.ico')    
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("338x183")

    bg_label = Label(newWindow,image = img_bg_Insere_Dados_ServidorRPCRMI_asset, width=334, height=178)
    bg_label.place(x=0, y=0)

    IP_input = Entry(newWindow)
    IP_input.place(x=21, y=87,width = 145,height = 26)

    PORTA_input = Entry(newWindow)
    PORTA_input.place(x=181, y=87,width = 145,height = 26)

    conectar_button = Button(newWindow, image=img_botao_Conectar_asset)
    conectar_button.place(x=107, y=127)

# ABAIXO, AS TELAS DO MEDIADOR - MOM:

path_img_bg_mediador_MOM_asset = resource_path('recursos/bg_mediador_MOM.png')
img_bg_mediador_MOM_asset = PhotoImage(file=path_img_bg_mediador_MOM_asset, master=root)

def janela_Mediador():
    newWindow = Toplevel(root)
    newWindow.title("MOM: Mediador")
    icone_asset_url = resource_path('recursos/icone.ico')
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("375x426")

    bg_label = Label(newWindow,image = img_bg_mediador_MOM_asset, width=371, height=425)
    bg_label.place(x=0, y=0)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 39,height = 13,font = ("Callibri",9))
    text_area.place(x=37, y=174)
    text_area.focus()


# ABAIXO, AS TELAS DO SERVIDOR - RMI/RPC:

path_img_bg_servidor_RPCRMI_asset = resource_path('recursos/bg_servidor_RPCRMI.png')
img_bg_servidor_RPCRMI_asset = PhotoImage(file=path_img_bg_servidor_RPCRMI_asset, master=root)

def janela_Servidor_RPC():
    newWindow = Toplevel(root)
    newWindow.title("RPC/RMI: Servidor")
    icone_asset_url = resource_path('recursos/icone.ico')
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("478x223")

    bg_label = Label(newWindow,image = img_bg_servidor_RPCRMI_asset, width=475, height=222)
    bg_label.place(x=0, y=0)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 41,height = 6,font = ("Callibri",9))
    text_area.place(x=145, y=99)
    text_area.focus()

if __name__ == "__main__":

    janela_Espiao()
    janela_Erro_PORTA_INVALIDA()
    janela_Erro_IP_INVALIDO()
    janela_Conectar_Servidor_RPCRMI()
    root.mainloop()
