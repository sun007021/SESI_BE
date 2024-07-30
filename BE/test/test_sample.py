"""Sample test for IMFast"""
import pytest
from httpx import AsyncClient
from loguru import logger


@pytest.mark.anyio
async def test_bad_request_api(client: AsyncClient):
    """Test bad request api"""
    response = await client.put("/api/v1/sample/bad_request")
    assert response.status_code == 400


@pytest.mark.anyio
async def test_sign_up(client: AsyncClient):
    """Test sign up"""
    response = await client.post("/api/v1/users", json={
        "email": "user@example.com",
        "password": "password",
        "name": "홍길동",
        "sex": "M",
        "birth": "1990-01-01",
        "address": "서울시 강남구",
        "phone": "010-1234-5678"
    })
    assert response.status_code == 201
    assert response.json()['result'] == {
        "email": "user@example.com"
    }
