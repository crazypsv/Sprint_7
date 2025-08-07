import allure
import requests
from handle import Handle
from urls import Urls


class TestReturnOrderList:
    @allure.title('В тело ответа возвращается список заказов')
    def test_list_order(self):

        with allure.step("Отправка GET-запроса для получения списка заказов"):
            response = requests.get(f'{Urls.URL}{Handle.GET_ORDERS_LIST}')  # Важно убедиться, что endpoint верный!


        with allure.step("Проверка статуса ответа и содержания поля orders"):
            assert response.status_code == 200
            assert "orders" in response.json()