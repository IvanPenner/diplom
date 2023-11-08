import requests
import configuration
import data
import pytest

# Пеннер Иван, 10й поток, Дипломный проект.
@pytest.fixture
def created_order():
    # Выполняем запрос на создание заказа
    response = requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER, json=data.order_body)
    return response.json()

def test_track_order(created_order):
    # Получаем номер трека заказа
    track = created_order["track"]

    # Выполняем запрос на получение заказа по треку
    response = requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))
    assert response.status_code == 200
