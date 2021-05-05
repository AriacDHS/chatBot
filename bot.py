import os

def processar_resposta(resposta,nome):
    if resposta == "1":
        print(f"{os.linesep}{nome}, prazer, sou Leonardo Candido Barbosa, estudante do curso Design de Games na Universidade Anhembi Morumbi, atualmente cursando o sétimo semestre. {os.linesep}")
    elif resposta == "2":
        print(f"{os.linesep}Meu objetivo é ingressar no mercado de jogos, desenvolver minhas habilidades individuais e de equipe e consequentemente fazer a diferença no meu local de trabalho.{os.linesep}")
    elif resposta == "3":
        print(f"{os.linesep}Realizei um curso de Marketing, Logística e Comunicação pela ESDP em 2016, concluí o ensino médio em 2017, iniciei a graduação em Design de Games na Universidade Anhembi Morumbi em 2018 com previsão para conclusão em Dezembro de 2021.{os.linesep}")
    elif resposta == "4":
        print(f"{os.linesep}Durante o curso realizei vários projetos acadêmicos, dentre eles Sookha, um jogo feito em Unity3D que conta a história da lenda da cidade de Fatehpur (pode ser visto em: https://youtu.be/R0eAHRWbTrA) e o Despertar da Meia Noite, também feito em Unity3D que é uma narrativa Transmídia do filme À Meia-Noite Levarei Sua Alma(pode ser visto em: https://youtu.be/Nzl9K36cCeE). Em ambos os projetos trabalhei como Desenvolvedor Unity(C#).{os.linesep}")
    elif resposta == "5":
        print(f"{os.linesep}Atualmente meu projeto atual é o meu TCC. Trata-se de um jogo plataforma 3D desenvolvido em Unity controlado unicamente por comandos de voz. O jogo está sendo desenvolvido em equipe e estou encarregado de parte da programação e sonorização do projeto. Ainda não existem versões jogáveis disponíveis para o público, mas em breve o link de acesso será disponibilizado.{os.linesep}")
    elif resposta == "6":
        print(f"{os.linesep}No momento, meu foco de estudo está na linguagem Python, com foco em automações e seu uso para áreas como Data Science.{os.linesep}")
    elif resposta == "7":
        print(f"{os.linesep}Meus projetos podem ser encontrados em https://github.com/AriacDHS e https://itch.io/profile/oxys .{os.linesep}")
    else:
        print("Por favor, digite apenas os números da lista de perguntas: 1, 2, 3, 4, 5, 6, ou 7")



def start():
    #apresentação
    print("Olá, seja bem vindo a minha carta de apresentação.")
    #recebe o nome do usuário
    nome = input("Qual o seu nome?")
    #oferece o menu de opções
    while True:
        resposta = input(f'O que gostaria de saber sobre mim?{os.linesep}[1] - Quem eu sou?{os.linesep}[2] - Qual é o meu objetivo atual?{os.linesep}[3] - Quais são minhas formações?{os.linesep}[4] - Quais são minhas experiências?{os.linesep}[5] - Qual é o meu projeto atual?{os.linesep}[6] - O que estou estudando no momento?{os.linesep}[7] - Onde meus projetos podem serencontrados?{os.linesep}')
        #processa a resposta enviada pelo usuário
        processar_resposta(resposta,nome)



if __name__ == '__main__':
    start()
