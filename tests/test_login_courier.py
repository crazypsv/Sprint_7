import allure
import requests
import pytest
from handle import Handle
from urls import Urls
from data import Users


class TestLoginCourier:

    @allure.title('Авторизация под курьером выдает id')
    def test_courier_log_in(self):
        with allure.step("Отправка POST-запроса на авторизацию"):
            response = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}',
                data=Users.data_current)

        with allure.step("Проверка успешного входа и наличия поля 'id'"):
            assert response.status_code == 200
            assert 'id' in response.text

    @allure.title('Ошибка при авторизации если логин или пароль не корректные')
    def test_courier_log_negative(self):
        with allure.step("Отправка POST-запроса на авторизацию с неверными данными"):
            response = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}',
                data=Users.data_negative)

        with allure.step("Проверка ошибки авторизации"):
            assert response.status_code == 404
            assert 'Учетная запись не найдена' in response.text

    @pytest.mark.parametrize('data_without_login_or_password', [Users.data_without_login, Users.data_without_password])
    @allure.title('Ошибка при авторизации если не заполнить логин или пароль')
    def test_courier_log_not_all_data(self, data_without_login_or_password):
        with allure.step("Отправка POST-запроса на авторизацию с отсутствующими данными"):
            response = requests.post(f'{Urls.URL}{Handle.LOGIN_COURIER}',
                data=data_without_login_or_password)

        with allure.step("Проверка ошибки при недостаточных данных"):
            assert response.status_code == 400
            assert 'Недостаточно данных для входа' in response.text