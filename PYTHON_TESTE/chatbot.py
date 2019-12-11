#  -*- coding: iso-8859-1 -*-
# comando para adicionar UTF-8 no meu codigo em python   no inicio do arquivo adiciono

# importo o chatterBot
from chatterbot import ChatBot
# listTrainer para aprendizado
from chatterbot.trainers import ListTrainer

# importo OS para utilizar lista em pasta para treino 27/11/2019 elias
import os

# elias import CHatterBottrainer
from chatterbot.trainers import ChatterBotCorpusTrainer  # não estava no tutorial original 28/11/2019

# import yaml para ler arquivo do tipo yaml treinamento portugues
import yaml

# instancio a classe chatbot e crio um bot chamado irineu
bot = ChatBot('Irineu')

# treinar bot
conversa = ChatterBotCorpusTrainer(bot)  # trainer = conversa, no  exemplo  original 28/11/2019
# ListTrainer 27/11/2019 elias
conversa = ListTrainer(bot)
conversa.train('chatterbot.corpus.portuguese')  # elias adicionou essa linha 27/11/2019
conversa.train([
    'oi',
    'olá',
    'Tudo bem?',
    'Estou bem!',
    'O que você gosta de fazer?',
    'Gosto de estudar Python !',
    'Qual o seu nome?',
    'Irineu e qual é o seu?',
    'sim',
    'ok',
    'obrigado',
    'de nada',
    'vamos lá',
    'vamos aonde?',
    'boa tarde',
    'Boa tarde tudo bem com você?',
])

# treinar via arquivo txt 28/11/2019 elias
arquivo = open("C:/Users/Livre Tech/Desktop/PYTHON_TESTE/treino/legenda.txt", 'r').readlines()
conversa.train('chatterbot.corpus.portugues')  # adicionado para teste essa linha
conversa.train(arquivo)
print('treinamento concluido!')

# ERRO DE PERMISSÃO OLHA DEPOIS  29/11/2019
# yaml = open("C:/Users/Livre Tech/Desktop/PYTHON_TESTE/data/portuguese", 'r')
# conversa.train(yaml)  # teste reinar duas vezes! 29/11/2019


# setamos caminho da aplicação
dir_path = os.getcwd()

# configurando o Adaptador de armazenamento (banco de dados)
bot = ChatBot(
    'Irineu',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    input_adapter='chatterbot.input.TeminalAdapter',
    output_adapter='chatterbot.output.TerminalAdapter',
    database='./database.sqlite3'
)
while True:
    try:
        resposta = bot.get_response(input("Usuario: ").strip().lower())#.strip()) 06/12/2019 retirei spaço do inicio ou fiim da palavra e coloquei tudo em maisculo  !
        if float(resposta.confidence) > 0.5:
            # transforma em string a resposta
            resposta = str(resposta)
            print("Irineu:", resposta.lower())
        else:
            nomeBot = "Irineu: "
            print(nomeBot,"Eu não entendi :( ")  # para adicionar ("Eu não entendi :( ", resposta) na resposta tenho que limpar variavel mensagem
    except(KeyboardInterrupt, EOFError, SystemExit):
        break  # exception exclusivo para poder parar bot com CTR+C  segundo esse Tutorial 27/11/2019

# ListTrainer 27/11/2019 elias
conversa = ListTrainer(bot)
conversa.train('chatterbot.corpus.portugues')  # elias adicionou essa linha 27/11/2019
conversa.train(['oi',
                'olá',
                'Tudo bem?',
                'Estou bem!',
                'O que você gosta de fazer?',
                'Gosto de estudar Python !',
                'Qual o seu nome?',
                'Irineu e qual é o seu?',
                'Boa tarde',
                'Boa tarde tudo bem com você?', ])

# ******************************************************************************************oi*********************************


#    def test_load_corpus_portuguese(self):
# files = ChatterBotCorpusTrainer.train('PYTHON_TESTE/data/portuguese')  # C:\Users\Livre Tech\Desktop\PYTHON_TESTE\data
# corpus_data = list(ChatterBotCorpusTrainer.load_corpus(*files))

# assertTrue(len(corpus_data))
# *******************************************************************************************************


# esta funcionando tudo porem sua base de dados de dicionario é muito pequena    27/11/2019
