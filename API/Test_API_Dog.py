import allure
import pytest
import requests


class TestAPIDogs:

    url = 'https://dog.ceo/api/'

    def test_get_random_dog_image(self):
        res = requests.get(f'{self.url}breeds/image/random')
        with allure.step("Проверяем код ответа"):
            assert res.status_code == 200, f'Не верный код ответаб получен ответ {res.status_code}'
        with allure.step("Проверяем что получили изображение"):
            res_json = res.json()
            #првоеряю только .jpg, так как по документации только такие извображения в базе
            assert '.jpg' and 'images.dog.ceo' in res_json['message'], 'Не получили изображение в ответе'

    @pytest.mark.parametrize("breed", [
        "akita",
        "boxer",
        "entlebucher",
        "elkhound"
    ])
    def test_get_certain_breed_image(self, breed):
        res = requests.get(f'{self.url}breed/{breed}/images/random')
        with allure.step("Проверяем код ответа"):
            assert res.status_code == 200, f'Не верный код ответаб получен ответ {res.status_code}'
        with allure.step("Проверяем что получили изображение по конкретнйо пароде"):
            res_json = res.json()
            assert breed in res_json['message'], f'Получили изображение другйо породы не {breed}'
