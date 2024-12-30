# Sistema de Recomendação por Imagens

## 📜 Objetivo do Projeto
Desenvolver um sistema de recomendação baseado na similaridade de imagens. O sistema permite o upload de uma imagem por um usuário e retorna as 5 imagens mais semelhantes de um dataset pré-definido, utilizando embeddings gerados por um modelo CLIP pré-treinado.

## ⛏️ Ferramentas e Tecnologias Utilizadas
- Python
- Google Colab
- Bibliotecas:
  - torch, transformers: Para o modelo CLIP.
  - tensorflow.keras.datasets: Para carregar o dataset Fashion MNIST.
  - Pillow: Para manipulação de imagens.
  - scikit-learn: Para calcular similaridades.
  - matplotlib: Para visualização de resultados.

 ## 🚩 Etapas do Projeto
 ### 1. Carregar o Modelo CLIP
- Utilizamos o modelo CLIP pré-treinado da OpenAI, que já possui embeddings treinados para capturar as características visuais das imagens.
- O processador CLIP é responsável por normalizar e preparar as imagens para o modelo.
### 2. Carregar o Dataset Fashion MNIST
- O dataset Fashion MNIST é carregado diretamente do TensorFlow.
- Utilizamos apenas um subset com 1000 imagens para reduzir o tempo de processamento.
### 3. Gerar Embeddings das Imagens do Dataset
- As imagens do Fashion MNIST são convertidas para o formato RGB.
- As embeddings são geradas utilizando o modelo CLIP e armazenadas para comparação futura.
### 4. Fazer Upload da Imagem do Usuário
- O usuário faz o upload de uma imagem em formato compatível (JPEG, PNG, etc.).
- A imagem é preprocessada e transformada em embeddings pelo modelo CLIP.
### 5. Calcular Similaridades
- As embeddings da imagem do usuário são comparadas com as embeddings do dataset usando similaridade de cosseno.
- As 5 imagens mais semelhantes são selecionadas com base nas maiores pontuações de similaridade.
### 6. Exibir Resultados
- A imagem do usuário é exibida ao lado das 5 imagens mais semelhantes do dataset, com suas respectivas pontuações de similaridade.

## 🖥️ Script Geral
O script está dividido em funções principais:
### 1. Carregar Modelo e Dataset
- Modelo CLIP e embeddings do Fashion MNIST.
### 2. Processar Imagem do Usuário
- Fazer upload, preprocessar e gerar embeddings.
### 3. Encontrar Imagens Semelhantes
- Calcular similaridades e selecionar as mais próximas.
### 4. Visualizar Resultados
- Exibir a imagem do usuário ao lado das semelhantes.
### 5. Visualizar Scripts:
- [Aqui](./scripts)

## ⚙️ Como Executar
### 1. Configure o Ambiente:
- Use o Google Colab para executar o código.
- Instale as dependências necessárias:
`!pip install torch torchvision clip-by-openai
!pip install tensorflow`
### 2. Carregue e Prepare o Dataset:
- O Fashion MNIST será carregado automaticamente pelo script.
### 3. Faça o Upload da Imagem:
- Execute o código e envie uma imagem do tipo:
  - Tênis, camiseta, bolsa ou vestido.
### 4. Visualize os Resultados:
- A imagem original será exibida ao lado das 5 imagens mais semelhantes, com as pontuações de similaridade.
### 5. Visualize a Execução:
- [Aqui](./notebooks/recommendation_view.ipynb)

## 📁 Estrutura de Pastas
```
recommendation/
│
├── scripts/
│   ├── main.py       # Script principal para executar o sistema
│   ├── preprocess.py # Funções para pré-processamento de imagens
│   ├── utils.py      # Utilitários gerais
│
├── notebooks/
│   └── recommendation.ipynb # Notebook para desenvolvimento e testes
│   └── recommendation_view.ipynb # Notebook para desenvolvimento e testes
│
│── README.md     # Documentação geral do projeto
│── .gitigonore
└── requirements.txt  # Dependências do projeto

```
## 🚀 Tempo de Execução Estimado
- Carregamento do Modelo e Dataset: ~2 minutos.
- Processamento da Imagem: ~1 minuto.
- Cálculo e Exibição: ~1 minuto.

## 📊 Limitações e Considerações
- O subset de 1000 imagens foi escolhido para manter o desempenho no Colab.
- Para datasets maiores, é recomendável salvar embeddings pré-processados para reduzir o tempo.
- O modelo CLIP é treinado em dados gerais e pode ter limitações em domínios específicos.

## 🤝 Possíveis Melhorias

- Usar embeddings pré-calculados e salvos.
- Expandir o dataset para mais classes e imagens.
- Criar uma interface gráfica amigável para uploads e resultados.

