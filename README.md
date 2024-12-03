# Exercício algoritmo genético

Este projeto utiliza um algoritmo genético para resolver o problema de planejamento de estudos, otimizando a seleção de tópicos a serem estudados dentro de um limite de horas disponíveis, com o objetivo de maximizar o impacto no aprendizado.

## Equipe:
- Matheus Barros Wenes Vieira
- Wesley kelvy
- Daricrys Ferreira Belem
- Rian landim

## Contexto Aplicação

O objetivo deste projeto é aplicar um algoritmo genético para resolver um problema de otimização relacionado ao planejamento de estudos. O desafio consiste em selecionar tópicos de estudo que maximizem o impacto no aprendizado (medido por uma pontuação) sem ultrapassar o limite de tempo disponível para estudo.

Essa abordagem é útil em cenários onde é necessário priorizar tarefas ou recursos limitados para obter o melhor resultado possível.

## Como é representado o indivíduo ?
Um indivíduo no contexto do algoritmo genético representa um plano de estudo, ou seja, uma lista de tópicos que devem ou não ser estudados.

# Estrutura do Cromossomo
 - Cada gene no cromossomo é representado por um número binário:
  - 1 (📚): O tópico será incluído no plano de estudo.
  - 0 (🤓): O tópico será ignorado.

## Como funciona a função de aptidão ?

### A função de aptidão avalia cada indivíduo com base nos seguintes critérios:

- 1 . Impacto no Aprendizado: Soma dos pontos de impacto dos tópicos incluídos no plano de estudo.
- 2 . Tempo Total: Soma do tempo necessário para estudar os tópicos selecionados.

## Penalização
  Se o tempo total exceder o limite disponível, a aptidão é automaticamente definida como 0. Isso garante que soluções inválidas (com excesso de horas) não sejam priorizadas.
## Objetivo
  O objetivo do algoritmo é maximizar o impacto no aprendizado enquanto respeita o limite de tempo disponível.

## Apresente um exemplo de saída do algortimo

``` Plano de Estudos - Melhor Solução Encontrada:
Tópico: Matemática  | Impacto: 8 | Tempo: 4 horas
Tópico: Física      | Impacto: 7 | Tempo: 3 horas
Tópico: Programação | Impacto: 10 | Tempo: 6 horas

Cromossomo Representado com Emojis:
📚📚🤓🤓🤓🤓🤓🤓📚🤓 ```