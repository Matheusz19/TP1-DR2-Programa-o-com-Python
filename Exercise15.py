def historia():
    print("Bem-vindo à uma aventura na floresta")
    print("Você se encontra na entrada de uma floresta desconhecida.")
    
    escolha1 = input("Você deseja entrar na floresta (1) ou voltar para casa (2)? Digite 1 ou 2: ")
    
    if escolha1 == '1':
        print("\nVocê entrou na floresta e ouviu o canto de pássaros ao longe.")
        
        escolha2 = input("Você pode seguir o som dos pássaros (1) ou explorar uma trilha à esquerda (2)? Digite 1 ou 2: ")
        
        if escolha2 == '1':
            print("\nVocê seguiu o som dos pássaros e encontrou um lindo lago.")
            print("Você decide descansar à beira do lago e aproveitar a beleza da natureza.")
            print("Fim.")
        elif escolha2 == '2':
            print("\nVocê explorou a trilha e encontrou uma cabana abandonada.")
            print("Dentro da cabana, você descobriu um mapa do tesouro.")
            print("Fim.")
        else:
            print("Escolha inválida. O caminho desapareceu.")
    
    elif escolha1 == '2':
        print("\nVocê decidiu voltar para casa e relaxar.")
        print("Fim.")
    else:
        print("Escolha inválida. Você ficou preso na entrada da floresta.")
        
historia()
