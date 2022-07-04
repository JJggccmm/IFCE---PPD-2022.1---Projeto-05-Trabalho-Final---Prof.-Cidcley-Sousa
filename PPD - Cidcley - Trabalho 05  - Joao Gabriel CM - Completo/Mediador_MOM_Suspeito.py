"""
*
********************************************************************************************************************************
* Mediador_MOM_Suspeito.py 02/03/2022 a 04/07/2022                                                                             *
*                                                                                                                              *
*   ( )[][]                                                                                                                    *
*   [][]                                                                                                                       *
*   [][][]                                                                                                                     *
*   [][]   - Programação Paralela e Distribuida(PPD) - 2022.1 - Prof.Cidcley                                                   *
*                                                                                                                              *
* Copyright 2022 - João Gabriel Carneiro Medeiros,                                                                             *                                                                                                                            
* Instituto Federal de Educação, Ciência e Tecnologia do Ceará - IFCE                                                          *
* Todos os direitos reservados                                                                                                 *
******************************************************************************************************************************************************
*                                                                                                                                                    *
*  {SOBRE O TRABALHO} -  O código é a implementação da parte do MEDIADOR (MOM) do 5° Trabalho da cadeira de PPD do curso de Eng. Computação          s* 
*                        do IFCE. O trabalho do aluno implementa uma comunicação 'Client - Subscribe' utilizado da tecnologia MOM no código          *
*                        que irá constante mente verificar por mensagens no tópico e exibilas nas sua interface.                                     *
*                                                                                                                                                    *
*                                                                                                                                                    *
*  !!!ATENÇÃO!!! - É preferível que o código seja executado em qualquer versão mais atual do Windows(Mas também funciona em Linux)!                  * 
*                                                                                                                                                    *
*  !!!ATENÇÃO!!! - Lembre que foi disponibilizado um arquivo executável! Basta procurar na pasta por ele! Use-o caso o código não rode               *
*                  apropriadamente e você queira ver o funcionamento da aplicação mesmo assim.                                                       *
*                                                                                                                                                    *
*  !!!ATENÇÃO!!! - Pode ser que ao executar todos os códigos ao mesmo tempo,  a aplicação apresente travamentos ou bugs                              *
*                  o aluno otimizou o código o máximo que pôde no tempo dado e pede desculpas por quaisquer incovenientes. Se possível rode          *
*                  os códigos e os .exe em uma máquina com configurações relativamente boas!                                                         *
*                                                                                                                                                    *
******************************************************************************************************************************************************
*
"""

"""
*
*       *******************
*  ~~~ Bibliotecas utilizada ~~~
*       *******************
*
"""

import paho.mqtt.client as mqtt # <---- Principal tecnologia do código! (MOM)
from queue import Queue # Usada para se criar uma estrutura de dados que amazene as msgs pegues dos tópicos assinados
import threading

#Bibliotecas para manipulação dos arquivos de imagem utilizados no código para poder compactá-los no arquivo .exe quando for construido:
import sys
import os

#Bibliotecas para manipulação e construção da interface gráfica no Tkinter:
from tkinter import *
from tkinter.scrolledtext import ScrolledText
import tkinter.font as font

"""Principais variáveis (GLOBAIS) utilizadas"""
endereco_Broker = "mqtt.eclipseprojects.io" # Broker online para testes
mensagens_recebidas = Queue() # Armazena as mensagens numa 'Queue' que é 'thread safe' já que usamos muitas threads nesse projeto

"""
*
*       ******************************************************
*  ~~~ Funções Auxiliares para algumas 'funcionalidades extras' ~~~
*       v*****************************************************
*
"""

# Método que éc hamado quando o Cliente recebe uma mensagem do seu tópico inscrito
def on_message(client, userdata, message):
    global mensagens_recebidas
    print(str(mensagens_recebidas))
    mensagens_recebidas.put(str(message.payload.decode("utf-8")) + "\n--------------------------------------------------------------\n*Tópico: " + str(message.topic))

# usada para a criação do .EXE
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

# ABAIXO, AS TELAS DO MEDIADOR - MOM:
path_img_bg_mediador_MOM_asset = resource_path('recursos/bg_mediador_MOM.png')
img_bg_mediador_MOM_asset = PhotoImage(file=path_img_bg_mediador_MOM_asset, master=root)

def fecha_APLICACAO(Toplevel):
    Toplevel.destroy()      
    Toplevel.quit()
    root. destroy()
    os._exit(1) 

def janela_Mediador():
    global endereco_Broker
    
    newWindow = Toplevel(root)
    newWindow.title("MOM: Mediador")
    icone_asset_url = resource_path('recursos/icone.ico')
    newWindow.iconbitmap(icone_asset_url)
    newWindow.geometry("375x426")

    newWindow.protocol("WM_DELETE_WINDOW", lambda:fecha_APLICACAO(newWindow))

    bg_label = Label(newWindow,image = img_bg_mediador_MOM_asset, width=371, height=425)
    bg_label.place(x=0, y=0)

    text_area = ScrolledText(newWindow,wrap = WORD, width = 39,height = 13,font = ("Callibri",9))
    text_area.place(x=37, y=174)
    text_area.focus()

    text_area.insert(INSERT,"[ ! ] Mediador conectado!\n\n", 'dados__entrada_mediador')
    text_area.insert(INSERT,"--------------------------------------------------------------\n\n ...\n\n", 'dados__entrada_mediador')
    text_area.tag_config('dados__entrada_mediador', foreground='green')

    # *Parte que usa MQTT
    client_subscriber_Mediador = mqtt.Client("Mediador")
    client_subscriber_Mediador.connect(endereco_Broker)
    client_subscriber_Mediador.subscribe("guarda_mensagens/Suspeitas") # <---- Tópico exclusivo para armazenar as mensagens enviadas pelo espião
    client_subscriber_Mediador.loop_start()
    client_subscriber_Mediador.on_message=on_message

    threading.Thread(target=checa_Recebidos_no_Topico, args=(text_area,)).start() #<---- THREAD 'checa_Recebidos_no_Topico' *****

# Checa se há mensagens no Tópico assinado
def checa_Recebidos_no_Topico(text_area):
    global mensagens_recebidas
    while True:                                   
        if mensagens_recebidas.empty() == True:
            continue
        else:
            text_area.insert(INSERT,"[ ! ]MENSAGEM RECEBIDA DO ESPIÃO:\n--------------------------------------------------------------\n", 'dados_recebidos_tipicos')
            text_area.insert(INSERT,mensagens_recebidas.get(), 'dados_recebidos_tipicos')
            text_area.insert(INSERT,"\n\n--------------------------------------------------------------\n\n", 'dados_recebidos_tipicos')
            text_area.tag_config('dados_recebidos_tipicos', background='black',foreground='lime')

"""
*
*       ***********************************
*  ~~~ Inicializando a aplicação do Mediador ~~~
*       ***********************************
*
"""

if __name__ == "__main__":
    janela_Mediador()
    root.mainloop()

