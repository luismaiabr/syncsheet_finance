import requests
from datetime import datetime
from schemas.financial_record import AssetSchema,FinancialCategory

# Definição do Enum e do Schema


# Função para consultar o ativo WING25 na API da Polygon.io
def get_future():
    # Substitua 'YOUR_API_KEY' pela sua chave de API da Polygon.io
    api_key = "YOUR_API_KEY"
    url = f"https://api.polygon.io/v2/aggs/ticker/I:WING25/prev?apiKey={api_key}"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Lança um erro para respostas HTTP inválidas (4xx, 5xx)
        data = response.json()

        # Verifica se os resultados estão disponíveis na resposta da API
        if 'results' in data and data['results']:
            asset_data = data['results'][0]  # Obtém o primeiro resultado

            # Cria uma instância de AssetSchema com os dados retornados pela API
            asset = AssetSchema(
                id=1,  # ID arbitrário ou gerado dinamicamente conforme necessário
                financial_category=FinancialCategory.FUTURES,
                asset_code='WING25',
                asset_full_name='Mini-Índice',
                currency='BRL',  # Supondo que a moeda seja Real Brasileiro
                open=asset_data['o'],
                close=asset_data['c'],
                high=asset_data['h'],
                low=asset_data['l'],
                timestamp=asset_data['t'],
                date_and_time=datetime.fromtimestamp(asset_data['t'] / 1000)  # Converte timestamp Unix para datetime
            )
            return asset.json()
        else:
            return {'error': 'No results found', 'data': data}
    
    except requests.exceptions.RequestException as e:
        return {'error': 'Request failed', 'message': str(e)}

# Exemplo de chamada da função e exibição do resultado
if __name__ == "__main__":
    print(get_future())
