import os
import time

class Processar:
    def __init__(self, nome):
        self.nomeArquivoParaTransferencia = nome

    def clonarArquivo(self):
        nome = self.nomeArquivoParaTransferencia
        #aqui vai filtrar a extensao
        extensao = nome[ nome.find('.'): ]
        novoNome = nome.replace(extensao, " (copy)"+extensao)
        print(novoNome)

        arquivo = open(nome, 'r')
        nomeArquivoCopiado = open(novoNome, "w")

        for linha in arquivo:
            nomeArquivoCopiado.write(linha+"\n")

    
        arquivo.close()
        nomeArquivoCopiado.close()

        self.arquivoCopiado = novoNome

        #para remover o arquivo já criado
        #os.remove(novoNome)

    def abrirConexao(self):
        os.system("python -m http.server")
        time.sleep(20)
        os._exit()


