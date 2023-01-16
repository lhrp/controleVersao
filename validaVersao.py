import json

from tkinter import messagebox

comparaVersaoInstalada = ''
comparaVersaoAtual     = ''

def downloadVersao(url, end):

    limpaPasta()

    import requests

    res = requests.get(url)

    with open(end, 'wb') as novoArquivo:
        novoArquivo.write(res.content)
        print('\nArquivo salvo em {}'.format(end))
        novoArquivo.close()

def limpaPasta():

    import os

    pasta = 'versao/'
    arquivos = os.listdir(pasta)

    if len(arquivos) != 0:
        print("\nArquivos apagados: ")
        for arquivo in arquivos:
            os.remove(pasta + arquivo)
            print('\n' + pasta + arquivo)


def atualizaVersao():
    global comparaVersaoInstalada
    global comparaVersaoAtual

    with open("arquivoVersaoInstalada.json", encoding='utf-8') as meu_json:
        versaoInstalada = json.load(meu_json)
        meu_json.close()

    comparaVersaoInstalada = versaoInstalada["versao"]

    with open("versao/VersaoAtual.json", encoding='utf-8') as meu_json:
        versaoAtual = json.load(meu_json)
        meu_json.close()

    comparaVersaoAtual = versaoAtual["versao"]


    if comparaVersaoInstalada != comparaVersaoAtual:
        opcao = messagebox.askquestion("Deseja atualizar a versão?",  'teste')
        if opcao == 'yes':
            atualizaVersaoInstalada = comparaVersaoAtual
            with open('arquivoVersaoInstalada.json', 'w', encoding='utf-8') as atualizaArquivoVersao:
                versaoInstalada["versao"] = atualizaVersaoInstalada
                json.dump(versaoInstalada, atualizaArquivoVersao,ensure_ascii=False,sort_keys=True, indent=4, separators=(',',':'))
                atualizaArquivoVersao.close()



def validaVersao():
    if comparaVersaoInstalada == comparaVersaoAtual:
        print('\n\nVersão mais recente já instalada')
        print("\nVersão Instalada = {}".format(comparaVersaoInstalada))
        print("\nVersão Servidor = {}".format(comparaVersaoAtual))    
    else:
        print('\n\nVersão desatualizada, por favor baixe a versão mais recente')
        print("\nVersão Instalada = {}".format(comparaVersaoInstalada))
        print("\nVersão Servidor = {}".format(comparaVersaoAtual))


downloadVersao(
    'https://lhrp.com.br/app/versaoAtual.json',
    'versao/versaoAtual.json'
)
atualizaVersao()
print(comparaVersaoInstalada)
print(comparaVersaoAtual)

##validaVersao()