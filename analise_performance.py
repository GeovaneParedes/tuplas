#!/usr/bin/env python3
import csv
import os  # Novo módulo para operações de sistema de arquivos
from typing import List, Tuple, Dict
import pandas as pd
import matplotlib.pyplot as plt

# Configurações explícitas
NOME_ARQUIVO_DADOS = 'app_performance.csv'
DIRETORIO_OUTPUT = 'imagens_analise'  # Nome da pasta de saída
NOME_ARQUIVO_GRAFICO = 'distribuicao_servicos.png'

def garantir_diretorio(caminho_diretorio: str):
    """
    Verifica se o diretório existe e o cria caso não exista.
    
    Usa 'os.makedirs' com 'exist_ok=True' para garantir que não haja
    erros caso a pasta já esteja presente, seguindo uma prática robusta.
    """
    try:
        os.makedirs(caminho_diretorio, exist_ok=True)
        print(f"\nDiretório de saída '{caminho_diretorio}' garantido.")
    except Exception as e:
        # Tratamento de erro robusto
        print("ERRO CRÍTICO: Não foi possível criar o diretório " 
              f"'{caminho_diretorio}'. Detalhe: {e}")
        raise

def ler_dados_como_tuplas(caminho_arquivo: str) -> List[Tuple]:
    """
    Lê um arquivo CSV e retorna os dados como uma lista de tuplas.
    [Docstring mantido para funções complexas, conforme diretriz 4]
    """
    dados_tuplas: List[Tuple] = []
    try:
        # ... (restante da função ler_dados_como_tuplas permanece inalterada)
        with open(caminho_arquivo, mode='r', newline='', encoding='utf-8') as arquivo:
            leitor_csv = csv.reader(arquivo)
            next(leitor_csv) 
            
            for linha in leitor_csv:
                try:
                    registro = (
                        linha[0],
                        linha[1],
                        int(linha[2]),
                        float(linha[3])
                    )
                    dados_tuplas.append(registro)
                except (ValueError, IndexError) as e:
                    print(f"ATENÇÃO: Linha corrompida ignorada. Detalhe: {e} | Linha: {linha}")
                    continue

    except FileNotFoundError:
        print(f"ERRO CRÍTICO: Arquivo '{caminho_arquivo}' não encontrado.")
        raise
    
    return dados_tuplas

def analisar_dados(dados_tuplas: List[Tuple]) -> pd.DataFrame:
    """
    Transforma a lista de tuplas em um DataFrame do Pandas e realiza análises estatísticas.
    [Docstring mantido para funções complexas, conforme diretriz 4]
    """
    colunas = ['id_transacao', 'nome_servico', 'status_http', 'tempo_resposta_ms']
    df = pd.DataFrame(dados_tuplas, columns=colunas)
    
    df_sucesso = df[df['status_http'].astype(str).str.startswith('2')]
    
    metricas = {
        'total_transacoes': len(df),
        'total_sucesso': len(df_sucesso),
        'tempo_resposta_medio_ms': df_sucesso['tempo_resposta_ms'].mean(),
        'tempo_resposta_mediana_ms': df_sucesso['tempo_resposta_ms'].median(),
        'tempo_resposta_std_ms': df_sucesso['tempo_resposta_ms'].std()
    }
    
    print("\n--- Métricas Estatísticas Chave ---")
    for chave, valor in metricas.items():
        print(f"{chave.replace('_', ' ').title()}: {valor:.2f}")

    return df_sucesso

def plotar_distribuicao(df: pd.DataFrame, dir_saida: str, nome_arquivo: str):
    """
    Gera um gráfico de barras, salva a imagem no diretório especificado
    e exibe o gráfico na tela.
    
    Adiciona a lógica de salvamento da imagem.
    """
    plt.figure(figsize=(10, 6))
    
    contagem_servico = df['nome_servico'].value_counts()
    contagem_servico.plot(kind='bar', color='skyblue')
    
    plt.title('Distribuição de Transações de Sucesso por Serviço')
    plt.xlabel('Nome do Serviço')
    plt.ylabel('Número de Transações')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--')
    plt.tight_layout()
    
    # 1. Salvar o arquivo
    caminho_completo = os.path.join(dir_saida, nome_arquivo)
    
    try:
        # Salva o gráfico como PNG de alta resolução
        plt.savefig(caminho_completo, dpi=300, bbox_inches='tight')
        print(f"Sucesso: Gráfico salvo em: '{caminho_completo}'")
    except Exception as e:
        print(f"ERRO: Não foi possível salvar o gráfico. Detalhe: {e}")

    # 2. Exibir (opcional)
    plt.show()

def main():
    """
    Função principal que orquestra o fluxo de análise de dados.
    """
    print(f"Iniciando análise a partir de '{NOME_ARQUIVO_DADOS}'...")
    
    # Passo 1: Leitura e conversão inicial para tuplas
    dados_lidos = ler_dados_como_tuplas(NOME_ARQUIVO_DADOS)
    
    # Teste Básico
    assert len(dados_lidos) == 10, "Erro: O número de registros lidos não é o esperado (10)."
    print(f"Sucesso: {len(dados_lidos)} registros lidos como Tuplas.")
    
    # Passo 2: Garantir que o diretório de saída exista
    garantir_diretorio(DIRETORIO_OUTPUT)
    
    # Passo 3: Análise estatística com Pandas
    df_analise = analisar_dados(dados_lidos)
    
    # Passo 4: Visualização e salvamento com Matplotlib
    plotar_distribuicao(df_analise, DIRETORIO_OUTPUT, NOME_ARQUIVO_GRAFICO)
    
    print("\nAnálise concluída.")

if __name__ == '__main__':
    main()
