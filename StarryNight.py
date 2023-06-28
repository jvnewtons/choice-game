print("Iniciar jogo?")
print("0. Sim")
print("1. Não")
print("")
jogo = int(input("Digite sua escolha:"))

while jogo == 0:

    NewPoints = 0
    NomeUsuario = input("Qual é seu nome?")
    IdadeUsuario = int(input("Quantos anos você tem?"))
    print("Certo,", NomeUsuario+", vamos começar.")

    if(IdadeUsuario >= 18):
        print("É uma noite chuvosa, você está voltando de sua faculdade, hoje terminou mais tarde por causa de um trabalho,")
    elif(IdadeUsuario < 18):
        print("É um dia chuvoso e nublado, você está voltando de sua escola.")
    print("como se isso não bastasse, você também não possui um guarda-chuva, então você fica a mercê da chuva, apenas se")
    print("protegendo com sua mochila apoiada em cima da sua cabeça. Na metade do caminho, no entanto, você vê um vulto,")
    print("então esse mesmo vulto aparece em sua frente, embaixo do feixe de luz do poste na calçada, assim que a figura é revelada,")
    print("seu arrependimento é nítido... É uma criatura enorme, no mínimo 2 metros e meio, com escamas vermelhas por todo o corpo,")
    print("seus olhos completamente vazios, só uma imensa escuridão. Não há cabelo na cabeça dessa criatura, somente dois")
    print("pequenos, porém aterrorizantes, chifres, por último, no lugar de suas unhas, há garras.")
    print("Você paralisa, a entidade se aproxima, cada vez mais perto, até que-")

    print("...")

    print("Algo para o avanço da criatura, quando você se dá por perceber, a criatura está partida em dois, no chão, e")
    print("então começa a se desintegrar. Ao se acalmar, você nota o que foi o algo que parou a criatura.")
    print("É um homem de estatura baixa, possui no máximo 1.70, o cabelo dele é castanho escuro, bagunçado, e")
    print("parece que não foi cortado há meses, quem sabe anos. Veste um sobretudo preto e a cor de sua íris é vermelha,")
    print("porém, o que mais te chama atenção, é a katana que ele carrega em sua cintura.")

    print("")

    print("???: Você está bem?")

    print("")

    print("1. -Estou...")
    print("2. -N-Não mesmo!")

    print("")

    escolha1 = int(input("Digite 1 ou 2 para realizar sua escolha, elas afetarão alguns aspectos:"))

    print("")

    if(escolha1 == 1):
        print("???: Que bom... Deve ter sido assustador, fico feliz que esteja bem.")

    elif(escolha1 == 2):
        print("???: Sinto muito por você ter visto isso, eu fui lento... Imagino que eu lhe deva explicações.")

    print("Meu nome é Urimash, o que você viu foi um demônio, eu os mato, é tão simples quanto parece. Qual seu nome?")


    print("")

    print("1. -Meu nome é", NomeUsuario+".")
    print("2. -Você vem sempre aqu...-Quer dizer, er...", NomeUsuario, ", meu nome é", NomeUsuario+".")
    print("3. -Não vou dizer meu nome pra um maluco que carrega uma... KATANA por aí!")

    print("")

    escolha2 = int(input("Já sabes como funciona, vá em frente:"))

    print("")

    if(NomeUsuario == "Newton" and escolha2 != 3):
            print("Urimash: Você... Está brincando comigo?")

    elif(NomeUsuario == "newton" and escolha2 != 3):
        print("Urimash: Você... Está brincando comigo?")

    else:
        if(escolha2 == 1):
            print("Urimash: É um prazer,", NomeUsuario+", eu irei lhe acompanhar até sua casa, por algum motivo, hoje há mais demônios")
            print("por essa região.")

        elif(escolha2 == 2):
            print("Ele arqueia a sobrancelha em estranhamento, porém acaba ignorando.")
            print("Urimash: Tudo bem,", NomeUsuario+", vou te acompanhar pelo resto do caminho.")
            NewPoints = NewPoints + 1

        else:
            print("Ele sorri de boca fechada, mas não de alegria, é um sorriso melancólico.")
            print("Urimash: Certo, é justo... Ao menos deixe-me lhe acompanhar até sua casa, essas criaturas são")
            print("perigosas.")

    print("")

    print("Você deixa o homem misterioso te deixar em casa, o resto do caminho é tranquilo e ele não fala uma palavra sequer, ")
    print("seus passos são tão silenciosos que, se não fosse por toda a situação, você provavelmente se esqueceria de sua pre-")
    print("sença. Então vocês finalmente chegam em sua casa.")

    print("")

    print("Urimash: Bem, aqui nós despedimos, ainda vamos nos ver já que agora você sabe da existência desses demônios. Tam-")
    print("bém peço que não fale sobre isso pra ninguém... É sério. Seria péssimo para todos se isso se espalha-")

    print("")

    print("Antes dele terminar sua fala, algo o atinge rapidamente, seus olhos mal conseguem acompanhar o vulto preto, quando")
    print("a fumaça que o estrondo causou é dissipada, você vê uma criatura alta, quase 3 metros de altura, estranhamente, usa")
    print("um terno, toda a pele da criatura é extremamente pálida e não possui face alguma. A pior parte, é que de suas costas")
    print("saem 6 tentáculos negros, finos e afiados. Então você nota Dália caído no chão com vários arranhões, o demônio se ")
    print("aproxima cada vez mais de Urimash e seus tentáculos atacam, porém, em um piscar de olhos, seu salvador se levanta e se")
    print("defende com sua lâmina, é uma velocidade tão alta que você nem sabia que humanos podiam chegar, mesmo assim, pouco a pouco, a")
    print("criatura fica mais perto de acertar seus ataques, então um tentáculo pega de raspão em Urimash, depois mais outro, cada")
    print("vez mais ferimentos surgem nele ainda mais profundos que os anteriores. Você chega a conclusão de que: ele certamente")
    print("perderá... O que você faz?")

    print("")

    if(NewPoints >= 1 or NomeUsuario == "Newton"):
        print("0. ???")

    elif(NomeUsuario == "newton"):
        print("0. ???")

    print("1. Correr")
    print("2. Lutar.")
    print("3. Gritar por ajuda.")

    print("")

    escolha3 = int(input("Digite sua escolha:"))

    print("")

    if (escolha3 == 0):
            print("Você vê a pessoa que acabou de te salvar prestes a morrer, ou no melhor dos casos, ficar em estado grave, mesmo")
            print("não o conhecendo há muito tempo, você sente algo... Você não pode deixá-lo morrer... De. Jeito. Nenhum....")
            print("Seu lado racional é jogado de lado, você avança, a criatura nota sua aproximação e dois tentáculos lhe atacam,")
            print("porém, eles estão... Lentos?! Eles estão lentos comparados à você! Você desvia de ambos, então em sua mão surge")
            print("uma energia roxa brilhante, você não perde tempo e ataca!")
            print("")
            print("A energia púrpura envolve todo o corpo da criatura e em um pisca de olhos, onde você atingiu o demônio, há")
            print("apenas um buraco... A criatura cai e seu corpo começa a evaporar em uma fumaça negra.")
            print("")
            print("Final: Assassino de Demônio.")

    elif(escolha3 == 1):
            print("Você corre o mais rápido que seu corpo te permite pra longe, então você escuta um grito de dor, com certeza não")
            print("da criatura, quando você olha para trás... Newton está caído no chão, morto... E você percebe que é o próximo")
            print("quando o demônio se teletranporta em sua frente, em um piscar de olhos, você é perfurado e vai perdendo seus")
            print("sentidos... Até morrer.")
            print("")
            print("Final: Não Há Pra Onde Escapar.")

    elif(escolha3 == 2):
        print("Você sabe que não pode deixar na mão o homem que te salvou, ele está arriscando sua vida por você, você sente")
        print("que precisa ajudá-lo, então é feito seu avanço, reunindo o máximo de coragem que você pode no momento, mas...")
        print("Antes de você se dar conta, seu abdômen é perfurado por dois tentáculos negros, você escuta o homem gritar e")
        print("então a espada dele corta os outros quatro tentáculos do demônio, você percebe que apesar de ter falhado, criou")
        print("a oportunidade perfeita para Urimash, e ele não perde tempo, sua lâmina dança no ar e o corpo da criatura é cor-")
        print("tado em dois. Então ele vai até você o mais rápido possível e te segura nos braços, você está perdendo a cons-")
        print("ciência, não consegue ouvir o que ele está falando, a única coisa agora que você pode ver são flashes, então")
        print("seus olhos se fecham...")
        print("")
        print("MAS, você está vivo, seus olhos se abrem e você se vê num quarto de hospital...")
        print("")
        print("Final: Ato Heroico.")

    else:
        print("Você grita por ajuda tão alto quanto sua voz e seus pulmões permitem, de novo e de novo... Porém além de vocês")
        print("três, nada nem ninguém te ouve... Porém, você vê os olhos de Newton determinados quando nota seu desespero, ele")
        print("maneja sua espada mais rápido, é nítido que ele está se esforçando ao máximo, usando cada parte de seu corpo pra")
        print("se defender e procurar brechas pra atacar. Ele luta ferozmente sem parar, parece que se passou uma eternidade,")
        print("mas você sabe que no máximo se passaram alguns segundos... Então, com seu corpo cheio de ferimentos, ele diz...")
        print("")
        print("Urimash: CORRA! E não pare! Eu não deixarei ele te alcançar.")
        print("")

        print("1. Correr.")
        print("2. Ficar e lutar.")

        print("")

        EscolhaAlternativa = int(input("Digite sua escolha:"))

        if(EscolhaAlternativa == 1):
            print("Por um momento, você paralisa, ele está dando cada parte de si pra te proteger, mesmo nem te conhecendo...")
            print("Se antes você tinha alguma dúvida sobre a índole desse cara misterioso, agora não há mais nenhuma... Você")
            print("não pode deixar que o esforço dele seja em vão, então faz de acordo e corre, como se sua vida dependesse")
            print("disso... E realmente depende. Você corre até suas pernas não te responderem mais, nem mesmo sabe onde está,")
            print("então você perde a consciência por exaustão, quando acorda, está numa cama de hospital, as lembranças de sua")
            print("noite surgem novamente, porém sua atenção se volta para o noticiário... Aparentemente, um homem foi encontrado")
            print("morto, em frente a sua casa, seu corpo cheio de buracos e cortes, com uma espada ao seu lado... Você tem cer-")
            print("teza, foi o mesmo que salvou sua vida, duas vezes contando com essa, e se sacrificou por isso...")
            print("")
            print("Final: Nobre Sacrifício.")

        else:
            print("Mesmo ele gritando para que você corra, mesmo cada centímetro do seu corpo se debatendo para fugir, você")
            print("Não cede. Você não consegue suportar a ideia de alguém tão bondoso lutar e sacrificar sua vida por você,")
            print("além disso, ele mata esses demônios, se ele morrer por você, quem vai conseguir ocupar o cargo dele? Quantas")
            print("vidas serão perdidas porque ele não vai estar lutando contra essas coisas...? Você não pode deixar isso")
            print("assim, então decides investir na criatura, mas não de forma impensada, você sabe que o demônio te atacará")
            print("na primeira opoturnidade, então se prepara para um rolamento para impedir ser atingido pela criatura,")
            print("assim que você nota um dos tentáculos indo em sua direção, como você já estava pronto, você rola no chão,")
            print("porém mesmo assim, o tentáculo é rápido demais para você acompanhar, então você sai do seu rolamento com")
            print("um corte de raspão em suas costas. No entanto, você continua na direção do demônio e pula, a criatura")
            print("percebendo que você conseguiu desviar de dois tentáculos, envia três dessa vez, como você já está no ar,")
            print("tudo que você pode fazer é se defender com seus braços. Um deles perfura seu braço esquerdo, outro perfura")
            print("seu abdômen, porém o terceiro atinge diretamente seu coração, entra pelo seu peito e sai pelas suas costas.")
            print("Você escuta Urimash gritar por você. O demônio com 3 tentáculos ocupados rapidamente é subjulgado por Urimash")
            print("e cortado furiosamente em 5 partes diferentes. Você sente que conseguiu retribuir o favor do homem que te")
            print("salvou, mesmo à beira da morte, você está satisfeito, então você faz um último esforço para falar.")
            print("")
            if(escolha2 == 3):
                print("-Meu nome... É...", NomeUsuario +".")
                print("")
                print("Urimash: Por que...? Eu falhei... De novo... Eu sinto muito...")

            else:
                print("-Obrigado... De verdade.")
                print("")
                print("Urimash: Me desculpe... Eu não consegui te proteger...")
                print("")
                print("Final: Um Último Esforço.")



    print("")
    print("")
    print("Fim da versão Alpha.")
    print(":)")
    print("")
    print("")
    print("Deseja finalizar o jogo ou reiniciar?")
    print("1. Reiniciar")
    print("2. Sair do jogo")
    print("")
    fim = int(input("Digite sua escolha:"))

    if fim == 2:
        jogo = 1



























      



