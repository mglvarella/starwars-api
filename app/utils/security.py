from fastapi import Security, HTTPException, status
from fastapi.security.api_key import APIKeyHeader
import os

API_KEY_NAME = "access_token"

API_KEY = os.getenv("API_KEY", "power-of-data-star-wars-2024")

api_key_header = APIKeyHeader(name=API_KEY_NAME, auto_error=False)

async def get_api_key(api_key_header: str = Security(api_key_header)):
    # .strip() remove espaços em branco e quebras de linha acidentais
    if api_key_header and API_KEY and api_key_header.strip() == API_KEY.strip():
        return api_key_header
    else:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Acesso negado: Chave de API inválida ou ausente."
        )
