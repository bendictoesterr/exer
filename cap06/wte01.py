texto_para_gravar = "testando!"
# A linha abaixo cria um objeto que representa o nosso arquivo.
# Ele está sendo aberto no modo de escrita, usando a codificação UTF-8
arquivo = open("testando.txt", "w", encoding="utf-8") 
# A instrução write escreve um conteúdo dentro do arquivo
arquivo.write(texto_para_gravar)
# Ao final da manipulação, devemos fechar o arquivo
arquivo.close()