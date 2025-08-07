import allure
import requests
from handle import Handle
from urls import Urls
from generator import register_new_courier as gen
from generator import register_new_courier_without_login as gen_without_login
from generator import register_new_courier_without_password as gen_without_password


class TestCreateCourier:

    @allure.title('Создание курьера')
    def test_create_courier(self):
        valid_data = gen()

        with allure.step("Отправка POST-запроса на создание нового курьера"):
            response = requests.post(f"{Urls.URL}{Handle.CREATE_COURIER}", valid_data)

        with allure.step("Проверка статуса ответа и тела ответа"):
            expected_response_body = {"ok": True}
            assert response.status_code == 201
            assert response.json() == expected_response_body

    @allure.title('Нельзя создать двух одинаковых курьеров с одинаковыми логинами')
    def test_courier_duplicate_login(self):
        valid_data = gen()

        # Отправляем первый раз запрос успешно
        response_1 = requests.post(f"{Urls.URL}{Handle.CREATE_COURIER}", valid_data)
        assert response_1.status_code == 201

        # Отправляем второй раз тот же запрос, проверяем ошибку
        with allure.step("Отправка повторного POST-запроса с теми же данными"):
            response_2 = requests.post(f"{Urls.URL}{Handle.CREATE_COURIER}", valid_data)

        with allure.step("Проверка наличия конфликта уникальных логинов"):
            assert response_2.status_code == 409
            assert 'Этот логин уже используется' in response_2.text

    @allure.title('Нельзя создать курьера без логина')
    def test_create_courier_without_login(self):
        # Получаем некорректные данные без логина
        invalid_data = gen_without_login()

        with allure.step("Отправка POST-запроса без логина"):
            response = requests.post(f"{Urls.URL}{Handle.CREATE_COURIER}", invalid_data)

        with allure.step("Проверка валидности ошибок при отсутствии логина"):
            assert response.status_code == 400
            assert 'Недостаточно данных для создания учетной записи' in response.text

    @allure.title('Нельзя создать курьера без пароля')
    def test_create_courier_without_password(self):
        # Получаем некорректные данные без пароля
        invalid_data = gen_without_password()

        with allure.step("Отправка POST-запроса без пароля"):
            response = requests.post(f"{Urls.URL}{Handle.CREATE_COURIER}", invalid_data)

        with allure.step("Проверка валидности ошибок при отсутствии пароля"):
            assert response.status_code == 400
            assert 'Недостаточно данных для создания учетной записи' in response.text