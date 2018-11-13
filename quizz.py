#coding=utf-8

frases_lacunas_respostas = {
    "fácil": {
        "frase": "Água __0__, __1__ dura, tanto __2__ até que __3__.",
        "lacunas": ["__0__", "__1__", "__2__", "__3__"],
        "respostas": ["mole", "pedra", "bate", "fura"]
    },
    "médio": {
        "frase": "Olha que __0__ mais linda mais __1__ de __2__. É ela menina que __3__ e que passa...",
        "lacunas": ["__0__", "__1__", "__2__", "__3__"],
        "respostas": ["coisa", "cheia", "graça", "vem"]
    },
    "difícil": {
        "frase": "O __0__ da hipotenusa é igual à __1__ dos __2__ dos __3__",
        "lacunas": ["__0__", "__1__", "__2__", "__3__"],
        "respostas": ["quadrado", "soma", "quadrados", "catetos"]
    }
}
niveis = ["fácil", "médio", "difícil"]

opcoes_de_quantidade_de_chances = range(1,11)

ultima_chance = 1

def apresentacao():
    """
    Apresenta o jogo
    """
    print "\nSeja bem vindo!!!"
    print "Nesse jogo, será exibida uma frase com quatro lacunas, que serão completadas por você."
    print "Escolha o nível de dificuldade e a quantidade de tentativas para concluí-lo\n"


def selecionar_nivel():
    """
    Pergunta ao usuário qual o nível desejado, verifica de a resposta
    é válida e, caso não seja, informa ao usuário e pergunta novamente.
    Returns:
        (string) nivel "fácil", "médio", "difícil"
    """
    nivel = raw_input("\nEscolha um nível de dificuldade: ( fácil | médio | difícil): ").lower()
    while  nivel not in niveis:
            nivel = raw_input("\nO nível não foi digitado corretamente. Escolha entre ( fácil | médio | difícil): ").lower()
    print "\nO nível selecionado foi o nível: " + nivel + "\n"
    return nivel

def selecionar_quantidade_de_chances():
    """
    Pergunta ao usuário qual o número de chances desejado, verifica de a resposta
    é válida e, caso não seja, informa ao usuário e pergunta novamente.
    Returns:
        (int) chances "1", "2", "3", "4", "5", "6", "7", "8", "9", "10"
    """

    while True:
        try:
            chances = int(raw_input("Digite o número de chances(entre 1 e 10) que deseja ter: "))
            if chances not in opcoes_de_quantidade_de_chances:
                raise ValueError
        except ValueError:
            print("Você não digitou um número ou o número não está entre dentro do intervalo de 1 à 10\n")
        else:
            break

    return chances

def carregar_frase_lacunas_resposta(nivel):
    """
    Carrega a frase, as lacunas e respostas para um nível.
    Args:
        nivel (string): nível "fácil", "médio", "difícil".
    Returns:
        (string) Frase com lacunas
        (lista) Lista com as lacunas.
        (lista) Lista com as respostas.
    """
    frase = frases_lacunas_respostas[nivel]["frase"]
    lacunas = frases_lacunas_respostas[nivel]["lacunas"]
    respostas = frases_lacunas_respostas[nivel]["respostas"]
    return frase, lacunas, respostas

def jogar(chances, frase, lacunas, respostas):
    """
    Mostra a frase para o usuário, pede a resposta referente a uma lacuna e
    compara com a resposta correta.
    Se a resposta estiver errada, diminui o número de chances, exibe mensagem de
    erro e pergunta novamente até que as chances acabam.
    Se a resposta estiver correta, a função imprime a frase novamente, mas com a lacuna
    respondida preenchida, vai para a próxima lacuna e assim por
    diante até acabarem as lacunas.
    Args:
        chances (int): a critério do usuário.
        frases (string)
        lacunas (list)
        respostas (list)
    Returns:
        (string) "perdeu", "ganhou"
    """
    chance_restante = chances
    for index, lacuna in enumerate(lacunas):
        print "\nA frase é: " + frase
        resposta_usuario = raw_input("Digite a resposta para a lacuna " + lacuna + " : ")
        while resposta_usuario != respostas[index]:
            chance_restante -= 1
            if chance_restante > ultima_chance:
                resposta_usuario = raw_input("\nNão exatamente, você ainda tem " + str(chance_restante) +
                                             " chances. Tente mais uma vez a resposta para a lacuna: " + lacuna + " : ")
            if chance_restante == ultima_chance:
                resposta_usuario = raw_input("\nNão exatamente, essa é a última chance. Tente mais uma vez a resposta para a lacuna: " + lacuna + " : ")
            if chance_restante < ultima_chance:
                return "perdeu"
                break
        print "\nMuito bem!\n"
        frase = frase.replace(lacunas[index], resposta_usuario)
    return "ganhou"

def mensagem_final(resultado):
    """
    Mostra uma mensagem de vitória ou derrota
    Args:
        Resultado(string): "perdeu", "ganhou"
    Returns:
        (string)"PARABÉNS!!! VOCÊ TERMINOU O JOGO!!!", "QUE PENA!!! ACABARAM AS CHANCES. VAMOS TENTAR MAIS UMA VEZ?"
    """
    if resultado == "ganhou":
        print "\nPARABÉNS!!! VOCÊ TERMINOU O JOGO!!!\n"
    if resultado == "perdeu":
        print "\nQUE PENA!!! ACABARAM AS CHANCES. VAMOS TENTAR MAIS UMA VEZ?\n"


def inicia_jogo():
    """
    Esqueleto do jogo
    """
    apresentacao()
    nivel = selecionar_nivel()
    chances = selecionar_quantidade_de_chances()
    frase, lacunas, respostas = carregar_frase_lacunas_resposta(nivel)
    resultado = jogar(chances, frase, lacunas, respostas)
    mensagem_final(resultado)


inicia_jogo()
