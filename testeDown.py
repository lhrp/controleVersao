

def limpaPasta():

    import os

    pasta = 'versao/'
    arquivos = os.listdir(pasta)

    if len(arquivos) != 0:
        print("\nArquivos apagados: ")
        for arquivo in arquivos:
            os.remove(pasta + arquivo)
            print('\n' + pasta + arquivo)

def downloadVersao(url, end):

    import requests
    
    res = requests.get(url)

    with open(end, 'wb') as novoArquivo:
        novoArquivo.write(res.content)
        print('\nArquivo salvo em {}'.format(end))
        novoArquivo.close()


downloadVersao(
    'C:/Users/leonardopaulino-mtz/Pictures/testeRequest/versaoAtual.json',
    'versao/versaoAtual.json'
)
