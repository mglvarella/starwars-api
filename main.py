import functions_framework
from app.main import app
from fastapi.testclient import TestClient
import uvicorn
import os

@functions_framework.http
def starwars_api(request):
    # Debug: vamos ver o que está acontecendo (Isso só aparece no Log Explorer do GCP)
    configured_key = os.getenv("API_KEY", "power-of-data-star-wars-2024")
    received_key = request.headers.get("x-api-token")
    
    print(f"DEBUG: Path recebido: {request.path}")
    print(f"DEBUG: Chave configurada no ambiente (Tamanho): {len(configured_key) if configured_key else 0}")
    print(f"DEBUG: Chave recebida no Header (Tamanho): {len(received_key) if received_key else 0}")
    
    if configured_key == received_key:
        print("DEBUG: AS CHAVES COMBINAM!")
    else:
        print("DEBUG: AS CHAVES NÃO COMBINAM!")

    client = TestClient(app, follow_redirects=True)
    
    path = request.path if request.path else "/"
    
    print(f"DEBUG: Método={request.method}, Path={path}, Query={request.args}")

    try:
        response = client.request(
            method=request.method,
            url=path,
            headers=dict(request.headers),
            params=dict(request.args),
            content=request.get_data()
        )
        
        if response.status_code == 404:
            print(f"DEBUG: FastAPI retornou 404 para o path: {path}")
            
        return (response.content, response.status_code, response.headers.items())
    except Exception as e:
        print(f"ERROR: Erro interno no adaptador: {str(e)}")
        return (str(e), 500)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
