class Cerebro:
    def __init__(self, q_lista):
        self.questao_numero = 0
        self.questao_lista = q_lista
        self.pontos = 0

    def ainda_tem_questoes(self):
        return self.questao_numero < len(self.questao_lista)

    def proxima_pergunta(self):
        questao_agora = self.questao_lista[self.questao_numero]
        resposta_usuario = input(f"Q. {self.questao_numero + 1}:{questao_agora.texto} (Verdade/Falso)?: ")
        self.verificar_resposta(resposta_usuario, questao_agora.resposta)
        self.questao_numero += 1

    def verificar_resposta(self, resposta_usuario, resposta_certa):
        if resposta_usuario.lower() == resposta_certa.lower():
            print("Você está certo!")
            self.pontos += 1
        else:
            print("Está errado.")
        print(f"A resposta certa é: {resposta_certa}.")
        print(f"Sua pontuação atual é: {self.pontos}/{self.questao_numero + 1}\n")
