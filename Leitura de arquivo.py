with open("Arquivo.txt", "w") as arquivo:
       arquivo.write("Ola mundo!\n")
       arquivo.write("Estou aqui!\n")
       linhas = ["Proxima linha", "Outra linha"]
       arquivo.writelines(linhas)

with open("Arquivo.txt", "r") as arquivo: 
        for linhas in arquivo:
                print(linhas)


texto = "Mesagem"
with open("Arquivo.txt", "w") as arquivo:
       arquivo.write(texto)

arquivo = open("test2.txt", "w")

arquivo.write(texto)
arquivo.write("\nOutraLinha\n")
arquivo.write("fim do arquivo")
arquivo.close()