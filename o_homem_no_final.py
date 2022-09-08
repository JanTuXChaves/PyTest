name = input("Escreva o nome: ")
print("E aí", name, ", seu prego!!!")

answer = input(
    "Vim Aqui para te ajudar em relação as tuas escolhas, me fala ai, qual é a coisa que você mais quer da vida? Ser (dev ou fisico)?").lower()

if answer == "fisico":
    answer = input(
        "Tu tá ligado aqui isso é doido né? Você sabia que isso não é para você né? (sim/não) ")

    if answer == "não":
        print("Então não me faz perder tempo e vai emmpora, falou!!!")
    elif answer == "sim":
        print("Mano, você ama computador, por que vai para isso? Nem fala mais comigo.")
    else:
        print('Não entendi o que você escreveu.')

elif answer == "dev":
    answer = input(
        "Você sabe que vai ter que estudar pra caramba, né? (sim/não)")

    if answer == "sim":
        print("Então está no caminho certo!!")
    elif answer == "não":
        answer = input(
            "Realmente acredita que não vai ser preciso abdicar de algumas coisas para alcançar isso? (sim/não)")

        if answer == "não":
            print("Então acho que você não vai para lugar algum!")
        elif answer == "Sim":
            print("Ai sim meu garoto, continue em frente! Vai dar tudo certo no final!!")
        else:
            print('Não entendi o que você escreveu.')
    else:
        print('Não entendi o que você escreveu.')

else:
    print('Não entendi o que você escreveu.')

print("Uma hora voltamos a nos falar.", name)
