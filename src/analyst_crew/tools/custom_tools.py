from crewai.tools import tool
from functools import reduce
import pandas as pd
import os


@tool("Read Spreadsheet Tool")
def read_spreadsheet_tool() -> dict:
    """ 
    Lê a pasta ./data/input.
    Retorna um dicionário com o resumo dos dados.
    """
    
    folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../data/input'))

    summary = {}

    for file_name in os.listdir(folder):
        if file_name.endswith('.xlsx'):
            path = os.path.join(folder, file_name)
            df = pd.read_excel(path)

            summary[file_name] = {
                'columns': list(df.columns),
                'sample_rows': df.head(2).to_dict(orient='records')
            }
                
    return summary

@tool("Process Spreadsheet Tool")
def process_spreadsheet_tool(sheets: list) -> None:
    """
    Recebe as informações padronizados, faz as manipulações necessárias e salva o resultado.
    input esperado:
    [
        {
            'file_name': 'Nome do arquivo.xlsx',
            'columns': {
                'nome_antigo_da_coluna': 'nome_novo_padronizado',
                'outra_coluna_antiga': 'outra_coluna_nova_padronizada',
                ...
            }
        },
        ...
    ]
    """

    normallized_dfs = []
    
    input_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../data/input'))
    output_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../../data/output')) 

    for sheet in sheets:
        file_name = sheet['file_name']
        columns_mapping = sheet['columns']

        path = os.path.join(input_folder, file_name)
        df = pd.read_excel(path)

        columns_to_keep = list(columns_mapping.keys())

        df = df[columns_to_keep] 
        df = df.rename(columns=columns_mapping)

        normallized_dfs.append(df)     
    
    df_merged = reduce(lambda left, right: pd.merge(left, right, on=['nome_colaborador', 'ID_colaborador'], how='left'), normallized_dfs)

    fixed_columns = ['nome_colaborador', 'ID_colaborador', 'departamento']
    df_merged['valor_total'] = df_merged.drop(columns=fixed_columns).sum(axis=1)

    df_merged.columns = df_merged.columns.str.replace('_', ' ').str.title()
    
    os.makedirs(output_folder, exist_ok=True)

    output_file = os.path.join(output_folder, 'relatorio_custos.xlsx')
    df_merged.to_excel(output_file, index=False)
    
    print(f"Dados processados e salvos em: {output_file}")
