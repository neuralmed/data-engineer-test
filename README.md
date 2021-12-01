# Neuralmed - Desafio para engenharia de dados

Aqui na Neuralmed trabalhamos com grande quantidade de dados relativos a exames e 
laudos médicos. Esses dados precisam ser organizados em um `datalake` para serem utilizados para alguns propósitos:

1. Todos os usuários do datalake devem enxergar onde estão os dados e conseguem consumi-los de maneira fácil
2. Cientistas de dados precisam dos dados de exames, laudos e seus arquivos originais (imagens ou pdfs) para treinamento de modelos
3. Analista de dados precisam analisar a execução de cada modelo para medir uso da plataforma e gerar novos insights
4. Cada exame possui múltiplos labels e eles são usados como filtro para treinamento e algumas análises

Dado esse resumo super simplificado, no diretório "data", você encontrará uma amostra de dados, sendo:
- "exam": Diretório com exames que foram enviados para o datalake 
- "medical_report": Diretório com laudos
- "images: Diretório com imagens do exame

Todas as tarefas abaixo serão usadas para discussão na entrevista e para entendermos a experiência que possui com datalakes, ingestão e consumo de dados. Para esse desafio queremos:

1. Uma modelagem desses dados no datalake da maneira que achar mais interessante. Como armazenar, como transformar os dados e como consultar. 
Pode fazer um desenho da arquitetura e não precisa implementar nada dessa parte. 

2. Usando a linguagem que achar mais interessante e sua arquitetura desenhada acima, transforme os dados JSON de entrada no formato mais adequado, pensando em escalabilidade e na manutenção do código.

3. Descreva como podemos acessar a quantidade de exames com label = 'Covid' e sem label 'Pneumonia' no mês de 12/2021. 

4. Descreva como podemos acessar uma amostra de exames e suas imagens com body_part = 'Chest' e com mais de 5 labels informados.

Importante: 

- Não existe certo e errado na solução acima. Vamos analisar desempenho, escalabilidade, manutenção de código, clareza de código, testes e documentação. O README deve estar explicando como rodar com clareza e preferencialmente dockerizável.
Se precisar instalar uma biblioteca como pydantic ou poetry (somente exemplos), explique o que fez usá-la.

- Por mais que isso será útil no trabalho, não queremos um ambiente na GCP ou AWS. A análise é sobre o seu código e tudo deve funcionado desacoplado de bancos de dados e ambientes em nuvem.
