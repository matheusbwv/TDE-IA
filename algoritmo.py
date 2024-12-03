import random
from deap import creator, base, tools

# Dados do novo problema: lista de estudos
TOPICOS = ["Matemática", "Física", "Química", "Biologia", "História", 
           "Geografia", "Literatura", "Inglês", "Programação", "Artes"]
TEMPO_TOPICOS = [4, 3, 2, 5, 2, 3, 4, 2, 6, 3]  # Tempo necessário para cada tópico
PONTOS_IMPACTO = [8, 7, 5, 6, 4, 5, 7, 9, 10, 3]  # Impacto no aprendizado
HORAS_DISPONIVEIS = 15  # Horas totais disponíveis
QUANTIDADE_TOPICOS = len(TEMPO_TOPICOS)

# Função de aptidão: maximizar o impacto respeitando o limite de horas
def funcao_de_aptidao(individual):
    impacto_total = 0
    tempo_total = 0
    for i in range(QUANTIDADE_TOPICOS):
        if individual[i] == 1:
            impacto_total += PONTOS_IMPACTO[i]
            tempo_total += TEMPO_TOPICOS[i]

    if tempo_total > HORAS_DISPONIVEIS:
        return 0,  # Penalização para soluções inválidas
    else:
        return impacto_total,  # Retorna o impacto total como aptidão

# Função para criar um cromossomo (indivíduo)
def cromossomo():
    return random.randint(0, 1)

# Função para formatar o cromossomo como emojis
def formatar_cromossomo(cromossomo):
    return ''.join('📚' if gene == 1 else '🤓' for gene in cromossomo)

# Algoritmo genético
def encontra_solucao():
    # Configurações do algoritmo genético
    TAXA_CRUZAMENTO, TAXA_MUTACAO = 0.5, 0.2
    populacao = toolBox.population(n=150)  # População inicial
    aptidao = list(map(toolBox.evaluate, populacao))  # Avaliação inicial dos indivíduos

    for individuo, valor in zip(populacao, aptidao):
        individuo.fitness.values = valor

    geracao = 0
    while geracao < 50:  # Número de gerações
        geracao += 1

        # Seleção
        filhos = toolBox.select(populacao, len(populacao))
        filhos = list(map(toolBox.clone, filhos))

        # Cruzamento
        for filho1, filho2 in zip(filhos[::2], filhos[1::2]):
            if random.random() < TAXA_CRUZAMENTO:
                toolBox.mate(filho1, filho2)
                del filho1.fitness.values
                del filho2.fitness.values

        # Mutação
        for mutante in filhos:
            if random.random() < TAXA_MUTACAO:
                toolBox.mutate(mutante)
                del mutante.fitness.values

        # Avaliação da nova geração
        aptidao = list(map(toolBox.evaluate, filhos))
        for individuo, valor in zip(filhos, aptidao):
            individuo.fitness.values = valor

        # Substituição da população
        populacao[:] = filhos

    # Identifica o melhor indivíduo
    melhor_individuo = tools.selBest(populacao, 1)[0]
    print("\nPlano de Estudos - Melhor Solução Encontrada:")
    for i in range(QUANTIDADE_TOPICOS):
        if melhor_individuo[i] == 1:
            print(f'Tópico: {TOPICOS[i]} | Impacto: {PONTOS_IMPACTO[i]} | Tempo: {TEMPO_TOPICOS[i]} horas')
    print("\nCromossomo Representado com Emojis:")
    print(formatar_cromossomo(melhor_individuo))

# Configuração do DEAP
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

toolBox = base.Toolbox()
toolBox.register("cromossomo", cromossomo)
toolBox.register("individual", tools.initRepeat, creator.Individual, toolBox.cromossomo, QUANTIDADE_TOPICOS)
toolBox.register("population", tools.initRepeat, list, toolBox.individual)
toolBox.register("evaluate", funcao_de_aptidao)
toolBox.register("mate", tools.cxTwoPoint)
toolBox.register("mutate", tools.mutFlipBit, indpb=0.1)
toolBox.register("select", tools.selTournament, tournsize=3)

# Executa o algoritmo genético
encontra_solucao()
