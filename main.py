# Código principal, onde recebe o arquivo e trabalha com ele
from clonar import Processar

#arquivo = open("arquivo.txt", "r")

#clonar.clonarArquivo("arquivo.txt")


processarArquivo = Processar("arquivo.txt")
processarArquivo.clonarArquivo()
processarArquivo.abrirConexao()
