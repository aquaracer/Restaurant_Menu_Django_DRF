import unittest
import requests


class TestBasic(unittest.TestCase):

    def test_add_meal(self):
        url = "http://127.0.0.1:8000/api/v1/meals/"
        header = {'Authorization': 'Token 3a5b25d39e442314861a461b591f0ffb85a62ef6'}
        data = {
            "name": "Овощной салат",
            "proteins": 1,
            "fats": 2,
            "carbohydrates": 15,
            "calories": 90,
            "price": "70",
            "category": 1,

        }
        response = requests.post(url=url, headers=header, json=data)
        response = response.json()
        assert response == {'id': 22, 'name': 'Овощной салат', 'category': 1, 'proteins': 1,
                            'fats': 2, 'carbohydrates': 15, 'calories': 90, 'price': '70.00', 'picture': None}

    def test_invalid_data(self):
        cases = [
            (
                {'Authorization': 'Token 223a5b25d39e442314861a461b591f0ffb85a62ef6'}, 'detail', {},
                'Недопустимый токен.'),
            ({}, 'detail', {}, 'Учетные данные не были предоставлены.'),
            ({'Authorization': 'Token 3a5b25d39e442314861a461b591f0ffb85a62ef6'}, 'category',
             {"name": "Лобстер9", "proteins": 45, "fats": 5, "carbohydrates": 5, "calories": 150, "price": "1000.00"},
             'Это поле обязательно.'),
            ({'Authorization': 'Token 3a5b25d39e442314861a461b591f0ffb85a62ef6'}, 'price',
             {"name": "Лобстер9", "proteins": 45, "fats": 5, "carbohydrates": 5, "calories": 150,
              "price": "1000000.00"},
             'Убедитесь, что в числе не больше 7 знаков.'),
            ({'Authorization': 'Token 3a5b25d39e442314861a461b591f0ffb85a62ef6'}, 'price',
             {"name": "Лобстер9", "proteins": 45, "fats": 5, "carbohydrates": 5, "calories": 150,
              "price": "a"}, 'Требуется численное значение.'),
            ({'Authorization': 'Token 3a5b25d39e442314861a461b591f0ffb85a62ef6'}, 'calories',
             {"name": "Лобстер9", "proteins": 45, "fats": 5, "carbohydrates": 5, "calories": [1],
              "price": "1000"}, 'Требуется целочисленное значение.'),
            ({'Authorization': 'Token 3a5b25d39e442314861a461b591f0ffb85a62ef6'}, 'name',
             {"name": "Гамбургер", "proteins": 45, "fats": 5, "carbohydrates": 5, "calories": [1],
              "price": "1000"}, 'Блюдо с таким Название уже существует.')

        ]

        for header, key, data, expected in cases:
            with self.subTest():
                url = "http://127.0.0.1:8000/api/v1/meals/"
                response = requests.post(url=url, headers=header, json=data)
                response = response.json()
                if key == 'detail':
                    response = response['detail']
                else:
                    response = response[key]
                    response = response[0]
                self.assertEqual(response, expected)
