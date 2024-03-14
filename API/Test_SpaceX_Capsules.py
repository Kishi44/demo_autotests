import allure
import pytest
import requests


class TestSpaseX:

    url = 'https://api.spacexdata.com/v3/capsules'

    @pytest.mark.parametrize('capsule, result', [
        ("C101", {
                    "capsule_serial": "C101",
                    "capsule_id": "dragon1",
                    "status": "retired",
                    "original_launch": "2010-12-08T15:43:00.000Z",
                    "original_launch_unix": 1291822980,
                    "missions": [
                      {
                        "name": "COTS 1",
                        "flight": 7
                      }
                    ],
                    "landings": 1,
                    "type": "Dragon 1.0",
                    "details": "Reentered after three weeks in orbit",
                    "reuse_count": 0
                  }),
        ("C103", {
                    "capsule_serial": "C103",
                    "capsule_id": "dragon1",
                    "status": "unknown",
                    "original_launch": "2012-10-08T00:35:00.000Z",
                    "original_launch_unix": 1349656500,
                    "missions": [
                      {
                        "name": "CRS-1",
                        "flight": 9
                      }
                    ],
                    "landings": 1,
                    "type": "Dragon 1.0",
                    "details": "First of twenty missions flown under the CRS1 contract",
                    "reuse_count": 0
                  })
    ])
    def test_capsules_inf(self, capsule, result):
        params = {'capsule_serial': capsule}
        res = requests.get(self.url, params=params)
        with allure.step("Сравнваем данные в ответе с эталоном"):
            assert result == res.json()[0], "Ответ не совпадает с эталоном"
