# Spreadsheet Analyst Crew

Este projeto utiliza o framework [crewAI](https://crewai.com) para orquestrar múltiplos agentes de IA em tarefas de análise e processamento de planilhas. O objetivo é automatizar a leitura, padronização e consolidação de dados de arquivos Excel, gerando um relatório final de forma colaborativa entre agentes.

## Estrutura do Projeto

- **src/analyst_crew/config/**: Configurações dos agentes e tarefas (YAML).
- **src/analyst_crew/tools/**: Ferramentas customizadas para manipulação das planilhas.
- **src/analyst_crew/crew.py**: Configuração da Crew.
- **src/analyst_crew/main.py**: Arquivo principal para a execução.
- **data/input/**: Arquivos `.xlsx` de entrada.
- **data/output/**: Relatórios gerados serão salvos aqui.

### Diagrama

![Diagrama](images\diagrama.png)

## Como Executar

**Pré-requisitos**
   - Python >=3.10 and <3.13
   
   - Criar um arquivo `.env` na raiz do projeto e adicionar sua chave de API no arquivo:
     ```
     MODEL=groq/llama-3.3-70b-versatile
     GROQ_API_KEY=sua_api_key
     ```

**Instalar as ferramentas**
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

- [crewAI](https://docs.crewai.com/installation)

**Executar**
```
python main.py 
```
ou
```
crewai run
```

## Demonstração do Funcionamento e Resultado
[Link YouTube](https://youtu.be/2r4s7-X1u-U)

## Funcionalidades

- **Leitura de Planilhas**: Resume colunas e amostras dos arquivos de entrada.
- **Padronização**: Renomeia e seleciona colunas conforme mapeamento fornecido.
- **Consolidação**: Junta dados de múltiplos arquivos em um único relatório.

## Melhorias Futuras
- Adicionar interface web para subir os arquivos e exibir o resultado, com a opção de download.
- Suporte a múltiplos formatos de entrada (CSV, XLSX, JSON).
- Funções para treinamento, replay de task específica e testes.

## Referências 

- [CrewAI](https://docs.crewai.com/introduction) – Orquestração de agentes de IA.
- [Pandas](https://pandas.pydata.org/) – Manipulação e análise de dados tabulares.
- [Groq](https://console.groq.com/docs/overview) – LLM utilizada.