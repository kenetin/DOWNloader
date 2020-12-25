import pytube

lista_qualidades = []

link = input('Coloque o link do seu vídeo abaixo: ')
video = pytube.YouTube(link)

if video.streams.get_by_itag(18) and video.streams.get_by_itag(22):
    lista_qualidades.append(video.streams.get_by_itag(18))
    lista_qualidades.append(video.streams.get_by_itag(22))
    escolha = input("O seu vídeo tem duas qualidades: 360p e 720. Digite [1] para download em 360 ou [2] para 720p. -> ")
    if escolha == "1" or escolha == "[1]" or escolha == "[1" or escolha == "1]":
        stream = video.streams.get_by_itag(18)
        print("Baixando em 360p " + video.title + "...")
        stream.download()
        print("Baixado!")
        
    elif escolha == "2" or escolha == "[2]" or escolha == "[2" or escolha == "2]":
        stream = video.streams.get_by_itag(22)
        print("Baixando em 720p " + video.title + "...")
        stream.download()
        print("Baixado!")
    else:
        print("Comando inválido!")

elif video.streams.get_by_itag(18):
    lista_qualidades.append(video.streams.get_by_itag(18))
    escolha = input("O seu vídeo tem apenas em 360p. Digite [1] para baixar. -> ")
    if escolha == "1" or escolha == "[1]" or escolha == "[1" or escolha == "1]":
        stream = video.streams.get_by_itag(18)
        print("Baixando em [360p] " + video.title + "...")
        stream.download()
        print("Baixado!")
    else:
        print('Não foi baixado.')
else:
    print("Não tem qualidade compativel :(")
