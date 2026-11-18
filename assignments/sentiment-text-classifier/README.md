# 📘 Assignment: Classificação de Texto com IA

## 🎯 Objective

Use Python e um modelo simples de aprendizado de máquina para classificar frases como positivas ou negativas. Você vai preparar exemplos rotulados, treinar o modelo e testar previsões com frases novas.

Antes de executar o código, instale a biblioteca necessária com `python -m pip install scikit-learn`.

## 📝 Tasks

### 🛠️ Preparar os Exemplos e Separar os Dados

#### Descrição

Use os exemplos do código inicial para criar duas listas: frases e seus sentimentos. Separe uma parte dos exemplos para testar o modelo, sem usá-los durante o treinamento.

#### Requisitos

O programa concluído deve:

- Ter pelo menos 12 frases com rótulos correspondentes (`positive` ou `negative`).
- Separar os dados de treino e de teste usando `train_test_split`, com `test_size=0.25` e `random_state=42`.
- Manter a mesma quantidade de frases e rótulos.

### 🛠️ Transformar as Frases e Treinar o Modelo

#### Descrição

Computadores precisam de números para trabalhar com texto. Use `CountVectorizer` para transformar as frases em contagens de palavras e treine um classificador `MultinomialNB` com os exemplos de treino.

#### Requisitos

O programa concluído deve:

- Ajustar o vetorizador somente com as frases de treino e usá-lo para transformar os dados de teste.
- Treinar o modelo com os dados de treino.
- Exibir a acurácia do modelo nos dados de teste como uma porcentagem.
- Lembrar que, com poucos exemplos, a acurácia é apenas uma indicação inicial e não garante bons resultados em outros textos.

### 🛠️ Classificar Novas Frases

#### Descrição

Peça ao usuário uma frase e use o modelo treinado para prever se o sentimento é positivo ou negativo. Experimente frases diferentes e observe quando o modelo pode errar.

#### Requisitos

O programa concluído deve:

- Aceitar uma frase digitada pelo usuário.
- Transformar a frase usando o mesmo vetorizador treinado.
- Exibir a previsão (`positive` ou `negative`).
- Explicar, com um exemplo, por que uma previsão pode estar errada ou ser injusta; o modelo aprende padrões dos exemplos e não entende sentimentos como uma pessoa.
