dados_questoes = [
    {"texto": "O sangue de uma lesma é verde.", "resposta": "Verdade"},
    {"texto": "O animal mais barulhento é o elefante africano.", "resposta": "Falso"},
    {"texto": "Aproximadamente, um quarto dos ossos humanos estão nos pés.", "resposta": "Verdade"},
    {"texto": "A área de superfície total de um pulmão humano é do tamanho de um campo de futebol.",
     "resposta": "Verdade"},
    {"texto": "Na Virginia do Oeste, EUA, se você acidentalmente bater em um animal com seu carro, você pode levá-lo "
              "casa e comer.", "resposta": "Verdade"},
    {"texto": "Em Londres, Reino Unido, se você morrer na Câmara do Parlamento, você tem direito a um funeral de "
              "Estado.", "resposta": "Falso"},
    {"texto": "É ilegal fazer xixi no oceano em Portugal.", "resposta": "Verdade"},
    {"texto": "Você pode levar uma vaca escada abaixo, mas não subir.", "resposta": "Falso"},
    {"texto": "O Google originalmente chamado de 'Backrub'.", "resposta": "Verdade"},
    {"texto": "O nome de solteira da mãe de Buzz Aldrin era 'Moon'.", "resposta": "Verdade"},
    {"texto": "Nenhum pedaço de papel quadrado seco pode ser dobrado ao meio mais de 7 vezes.", "resposta": "Falso"},
    {"texto": "Algumas gramas de chocolate podem matar um cachorro pequeno.", "resposta": "Verdade"}
]

# Podemos criar um questionario usando a API do Open Trivia DB(opentdb.com/api_config.php), e gerar um questionario todinho.
questoes_TriviaDB = [
    {
        "questao": "Linus Torvalds criou Linux e Git.",
        "resposta_correta": "Verdade"
    },
    {
        "questao": "O logo do Snapchat é um sino.",
        "resposta_correta": "Falso"
    },
    {
        "questao": "Ponteiros não são usados no C original; eles foram adicionados depois no C++.",
        "resposta_correta": "Falso"
    },
    {
        "questao": "Ada Lovelace é considerada como o primeiro programador computacional.",
        "resposta_correta": "Verdade"
    },
    {
        "questao": "Na maioria das linguagens, o operador ++ é equivalente ao '+='.",
        "resposta_correta": "Verdade"
    },
    {
        "questao": "Tempo nos computadores são medidos pelo EPOX System.",
        "resposta_correta": "Falso"
    },
    {
        "questao": "O Windows 7 SO tem seis edições principais.",
        "resposta_correta": "Verdade"
    },
    {
        "questao": "O Windows ME SO foi lançado no ano 2000.",
        "resposta_correta": "Verdade"
    },
    {
        "questao": "Linux foi criado como uma alternativa para Windows XP.",
        "resposta_correta": "Falso"
    },
    {
        "questao": "A linguagem de programação, Python, tem esse nome em homenagem ao grupo de comédia britânico "
                   "'Monty Python'.",
        "resposta_correta": "Verdade"
    }
]

# Opção com multiplas escolhas
questoes_opcionais = [
    {
        "pergunta": "Quando a declaração de Indepêndecia dos EUA foi aprovado pelo Segundo Congresso Continental?",
        "resposta_certa": "4 Julho, 1776",
        "respostas_erradas": [
            "4 de Maio, 1776",
            "4 de Junho, 1776",
            "2 de Julho, 1776"
        ]
    },
    {
        "pergunta": "Após quantos anos é celebrado o 'Aniversário de Cristal'?",
        "resposta_certa": "15 anos",
        "respostas_erradas": [
            "20 anos",
            "10 anos",
            "25 anos"
        ]
    },
    {
        "pergunta": "Qual a palavra sueca para 'janela'?",
        "resposta_certa": "F'nster",
        "respostas_erradas": [
            "Haringl",
            "Skaumlrm",
            "Ruta"
        ]
    },
    {
        "pergunta": "Qual falácia lógica significa atacar o caráter de seu oponente em vez de seus argumentos?",
        "resposta_certa": "Ad hominem",
        "respostas_erradas": [
            "Post hoc ergo propter hoc",
            "Tu quoque",
            "Argumentum ad populum"
        ]
    },
    {
        "pergunta": "Frank Lloyd Wright foi o arquiteto por trás de qual edifício famoso?",
        "resposta_certa": "The Guggenheim",
        "respostas_erradas": [
            "Villa Savoye",
            "Sydney Opera House",
            "The Space Needle"
        ]
    }
]
