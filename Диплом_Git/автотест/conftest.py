import requests
import configuration
import data
import pytest

# Пеннер Иван, 10й поток, Дипломный проект.
@pytest.fixture
def created_order():
    response = requests.post(configuration.URL_SERVICE + configuration.NEW_ORDER, json=data.order_body)
    return response.json()


