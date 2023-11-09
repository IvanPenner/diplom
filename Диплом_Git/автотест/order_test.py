import configuration
import requests

def test_track_order(created_order):
    # Получаем номер трека заказа
    track = created_order["track"]
    response = requests.get(configuration.URL_SERVICE + configuration.ORDER_TRACK + str(track))
    assert response.status_code == 200