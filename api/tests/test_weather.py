import pytest
import httpx
from fastapi.testclient import TestClient
from unittest.mock import AsyncMock, patch
from src.resources.weather_resource import router
from fastapi import FastAPI

app = FastAPI()
app.include_router(router)

client = TestClient(app)

@pytest.mark.asyncio
@patch("src.resources.weather_resource.weather_service")
async def test_get_current_weather_success(mock_weather_service):
    mock_response = {
        "city": "Paris",
        "country": "FR",
        "timestamp": "2026-01-14T12:00:00",
        "weather": {
            "temperature": 20.0,
            "humidity": 65,
            "wind_speed": 10.0,
            "description": "Ciel dégagé",
        }
    }
    mock_weather_service.get_current_weather = AsyncMock(return_value=mock_response)

    response = client.get("/weather/current", params={"city":"Paris"})

    assert response.status_code == 200
    assert response.json() == mock_response

@pytest.mark.asyncio
@patch("src.resources.weather_resource.weather_service")
async def test_get_current_weather_city_not_found(mock_weather_service):
    mock_weather_service.get_current_weather = AsyncMock(
        side_effect=httpx.HTTPStatusError(
            message="Ville non trouvée",
            request=httpx.Request("GET", "https://api.example.com/weather"),
            response=httpx.Response(404, request=httpx.Request("GET", "https://api.example.com/weather")),
        )
    )

    response = client.get("/weather/current?city=VilleInconnue")

    assert response.status_code == 404
    assert "Ville 'VilleInconnue' non trouvée" in response.json()["detail"]

@pytest.mark.asyncio
@patch("src.resources.weather_resource.weather_service")
async def test_get_forecast_success(mock_weather_service):
    mock_response = {
        "forecast": [
            {"day": "2026-01-14", "temperature": 18.0, "humidity": 60},
            {"day": "2026-01-15", "temperature": 19.0, "humidity": 65},
        ]
    }
    mock_weather_service.get_forecast = AsyncMock(return_value=mock_response)

    response = client.get("/weather/forecast?city=Paris")

    assert response.status_code == 200
    assert response.json() == mock_response

@pytest.mark.asyncio
@patch("src.resources.weather_resource.weather_service")
async def test_get_forecast_http_error(mock_weather_service):
    mock_weather_service.get_forecast = AsyncMock(
        side_effect=httpx.HTTPError("Erreur de connexion")
    )

    response = client.get("/weather/forecast?city=Paris")

    assert response.status_code == 500
    assert "Erreur de connexion à l'API météo" in response.json()["detail"]
