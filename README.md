# 📈 Análise de Performance de Aplicações com Tuplas em Python

[cite_start]Este projeto demonstra uma abordagem sênior para a ingestão, processamento e análise de dados usando o Python 3.11+[cite: 2], focando em **tuplas** como estrutura de dados primária para garantir imutabilidade e integridade durante a leitura inicial. [cite_start]A solução é modular, utiliza tratamento robusto de erros [cite: 3] [cite_start]e adere aos princípios de Clean Code[cite: 6].

---

## 🇧🇷 Seção em Português (PT-BR)

### 🚀 Objetivo

Simular um pipeline de dados onde registros de performance de aplicações (tempo de resposta, status HTTP) são lidos de um arquivo CSV, processados como **tuplas** e, em seguida, analisados estatisticamente e visualizados usando as bibliotecas `pandas` e `matplotlib`.

### ✨ Destaques Técnicos (Padrão Sênior)

* [cite_start]**Modularidade e Clean Code:** Código dividido em funções específicas (`ler_dados_como_tuplas`, `analisar_dados`, `plotar_distribuicao`, `garantir_diretorio`) seguindo o princípio SRP (Single Responsibility Principle)[cite: 6].
* **Manipulação de Tuplas:** Utilização do módulo nativo `csv` para ler cada linha diretamente como uma tupla (`(str, str, int, float)`) antes de carregá-las no DataFrame, garantindo a imutabilidade do registro original.
* [cite_start]**Tratamento de Erros:** Implementação de `try/except` para lidar com `FileNotFoundError` (arquivo de dados ausente) e exceções internas (`ValueError`, `IndexError`) para ignorar linhas corrompidas no CSV, evitando *crashes* (fail-fast / fail-safe)[cite: 3].
* [cite_start]**Gestão de I/O:** O gráfico de saída é salvo em um diretório dedicado (`imagens_analise`), que é verificado e criado programaticamente, mantendo o diretório raiz limpo[cite: 3].
* **Testes Básicos:** Uso de `asserts` para validação rápida da integridade dos dados lidos.

### ⚙️ Como Executar

#### Pré-requisitos
* [cite_start]Python **≥ 3.11** [cite: 2]
* Instalar as dependências:
    ```bash
    pip install pandas matplotlib
    ```

#### Estrutura do Projeto
O repositório deve conter os seguintes arquivos:

├── app_performance.csv # Dados de exemplo └── analise_performance.py # Script de análise principal └── README.md

#### Execução
1.  Garanta que o arquivo `app_performance.csv` esteja presente.
2.  Execute o script principal:
    ```bash
    python analise_performance.py
    ```

### ➡️ Saída Esperada
O script irá imprimir as métricas estatísticas no console e salvar um gráfico de distribuição de serviços em um diretório novo ou existente: `imagens_analise/distribuicao_servicos.png`.

(imagens_analise/distribuicao_servicos.png)

---

## 🇺🇸 English Section (EN-US)

### 🚀 Objective

To simulate a data pipeline where application performance records (response time, HTTP status) are read from a CSV file, processed as **tuples**, and then statistically analyzed and visualized using the `pandas` and `matplotlib` libraries.

### ✨ Technical Highlights (Senior Standard)

* **Modularity and Clean Code:** Code is segmented into specific functions (`ler_dados_como_tuplas`, `analisar_dados`, `plotar_distribuicao`, `garantir_diretorio`) following the Single Responsibility Principle (SRP)[cite: 6].
* **Tuple Handling:** Utilizes the native `csv` module to read each line directly as a tuple (`(str, str, int, float)`) before loading it into the DataFrame, ensuring the immutability of the original record.
* **Robust Error Handling:** Implementation of `try/except` to manage `FileNotFoundError` (missing data file) and internal exceptions (`ValueError`, `IndexError`) to safely skip corrupted lines in the CSV[cite: 3].
* **I/O Management:** The output chart is saved in a dedicated directory (`imagens_analise`), which is checked and created programmatically, keeping the root directory clean[cite: 3].
* **Basic Tests:** Use of `asserts` for quick validation of data integrity after reading.

### ⚙️ How to Run

#### Prerequisites
* Python **≥ 3.11** [cite: 2]
* Install dependencies:
    ```bash
    pip install pandas matplotlib
    ```

#### Project Structure
The repository should contain the following files:

├── app_performance.csv # Sample data └── analise_performance.py # Main analysis script └── README.md

#### Execution
1.  Ensure the `app_performance.csv` file is present.
2.  Run the main script:
    ```bash
    python analise_performance.py
    ```

### ➡️ Expected Output
The script will print key statistical metrics to the console and save a service distribution chart to a new or existing directory: `imagens_analise/distribuicao_servicos.png`.
