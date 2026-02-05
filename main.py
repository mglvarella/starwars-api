import functions_framework
from app.main import app
import uvicorn
import os

@functions_framework.http
def starwars_api(request):
    from fastapi.testclient import TestClient
    
    client = TestClient(app)
    
    method = request.method
    path = request.path
    headers = dict(request.headers)
    params = dict(request.args)
    data = request.get_data()
    
    response = client.request(
        method=method,
        url=path,
        headers=headers,
        params=params,
        content=data
    )
    
    # Retorna o resultado para o GCP
    return (response.content, response.status_code, response.headers.items())

# 2. Configuração para rodar localmente (python main.py)
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    uvicorn.run(app, host="0.0.0.0", port=port)
