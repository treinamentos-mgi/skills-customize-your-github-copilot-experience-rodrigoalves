# 📘 Assignment: Hangman Game

## 🎯 Objective

Pratique strings, loops, condicionais, entrada de dados e seleção aleatória em Python ao criar um jogo da Forca.

## 📝 Tasks

### 🛠️ Selecionar a Palavra e Revelar Letras

#### Descrição
Implemente a preparação da partida: escolha uma palavra aleatória da lista fornecida e permita que o jogador descubra suas letras.

Exemplo: para a palavra `python`, após acertar `p` e `t`, exiba `p _ t _ _ _`.

#### Requisitos
O programa concluído deve:

- Selecionar aleatoriamente uma palavra da lista predefinida.
- Exibir cada letra ainda não descoberta como `_` e revelar as letras adivinhadas nas posições correspondentes.
- Solicitar palpites de uma letra e registrar as letras já tentadas.

### 🛠️ Controlar Tentativas e Encerrar a Partida

#### Descrição
Complete o loop principal do jogo para atualizar as tentativas e encerrar a partida quando o jogador vencer ou ficar sem tentativas.

#### Requisitos
O programa concluído deve:

- Definir e atualizar o número de tentativas incorretas restantes.
- Diminuir as tentativas restantes quando o palpite não estiver na palavra.
- Continuar a partida enquanto houver letras a descobrir e tentativas restantes.
- Exibir uma mensagem de vitória quando a palavra for descoberta.
- Exibir uma mensagem de derrota e revelar a palavra quando as tentativas acabarem.

---
