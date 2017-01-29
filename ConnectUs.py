import dropbox
import os
import time
from dropbox.files import WriteMode
#------------------------------------Início do programa------------------------#
client = dropbox.Dropbox('071tkC7_q5AAAAAAAAAAFjafxfQXYwu9SRhfH1vSMeyTICenpYLhm8z5G8j52pVS')#token do cliente
nomeUser = input('Digite o seu nome:  ')
os.system('clear')
while True:

    alt = input('-------------------------------------------- \n'\
                '1. Para fazer download da ultima atualização.\n'\
                '2. Para publicar suas alterações.\n'\
                '3. Para ler as ultimas notas.\n'\
                'Escreva "sair" para fechar.\n'\
                '---------------------------------------------\n'\
                'Digite: ')
    if alt == '1':
        nome = input('Escreva o nome do arquivo: ')
        try:
            nomeDBox = ('/%s'%nome)#nome do arquivo no dropbox
            nomeLocal = ('/home/user208/ConnectUs/Downloads/%s'%nome) #local do arquivo no computador
            client.files_download_to_file(nomeLocal,nomeDBox)#Recuperando arquivo do dropbox
            notaDB = ('/nota')
            client.files_download_to_file('/home/user208/ConnectUs/nota',notaDB)#Recuperando a ultima nota
            print('Download feito.')
            time.sleep(2)
            os.system('clear')
        except:
            os.system('clear')
            print('Ops! Você deve ter digitado o nome do arquivo errado.')
            time.sleep(2)
            os.system('clear')
    if alt == '2':
        nome = input('Escreva o nome do arquivo: ')
        try:

            nomeDBox = ('/%s'%nome)#nome do arquivo no dropbox
#----------------Início da criação da nota.------------------------------------#
            nota = input('Digite sua nota sobre a atualização: ')
            arquivo = open('nota','r')
            arquivoaux = arquivo.readlines()
##-------------------Atribuindo a hora de submissão---------------------------##
            #-----------------------------------#
            hora = time.ctime().split(' ')[3]   #
            dia = time.ctime().split(' ')[2]    #
            mes = time.ctime().split(' ')[1]    #
            #-----------------------------------#
##-----------------------Fim da atribuição------------------------------------##
            arquivoaux.append('#%s %s/%s às %s, mudou %s \n%s\n\n'%(nomeUser,dia,mes,hora,nome,nota))
            arquivo = open('nota','w')
            arquivo.writelines(arquivoaux)
            arquivo.close()
            arquivo = open('nota','rb')
            client.files_upload(arquivo,'/nota',mode=WriteMode('overwrite'))#(arquivo aberto,lugar no dropbox,modo de sobrescrever)
#-----------------Término da criação e envio da nota.--------------------------#

#-----------------Início do envio do arquivo.----------------------------------#
            f = ('/home/user208/ConnectUs/%s'%nome)
            fx = open(f, 'rb')#abre o arquivo
            client.files_upload(fx,nomeDBox,mode=WriteMode('overwrite'))
            print('Arquivo publicado.')
            time.sleep(2)
            os.system('clear')
#---------------------------Fim do envio---------------------------------------#
        except:
            os.system('clear')
            print('Ops! Você deve ter digitado o nome do arquivo errado.')
            time.sleep(3)
            os.system('clear')
    if alt == '3':
        os.system('clear')
        arquivo = open('nota','r')
        notes = arquivo.read()
        arquivo.close()
        print(notes)
        notes = input('Aperte enter para sair das notas...')
        os.system('clear')


    if alt.lower() == 'sair':
        print('Saindo.')
        time.sleep(1)
        os.system('clear')
        break

    else:
        os.system('clear')


#-----------------------------Fim do programa----------------------------------#
