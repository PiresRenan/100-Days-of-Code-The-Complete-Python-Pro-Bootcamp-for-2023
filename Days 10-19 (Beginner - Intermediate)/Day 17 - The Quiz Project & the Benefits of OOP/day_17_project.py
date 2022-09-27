# Quiz
from cerebro_quiz import Cerebro
from dados import questoes_TriviaDB
from questoes_modelo import Questao

questoes = []
for questao in questoes_TriviaDB:
    questao_texto = questao["questao"]
    questao_reposta = questao["resposta_correta"]
    nova_questao = Questao(q_texto=questao_texto, q_resposta=questao_reposta)
    questoes.append(nova_questao)

quiz = Cerebro(questoes)
while quiz.ainda_tem_questoes():
    quiz.proxima_pergunta()

print("Você concluiu o Quiz.")
print(f"Sua pontuação final é: {quiz.pontos}/{quiz.questao_numero}")
