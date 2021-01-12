from meals.models import Meals


def get_order_info(data):
    """
    Функция возвращает сумму заказа, список блюд,
    входящих в заказ и список аллергенов, содержащихся
    в блюдах
    """

    total_price = 0
    allergens = set()
    order = []
    for key in list(data.keys()):
        if key != 'csrfmiddlewaretoken':
            meal = Meals.objects.get(name=key)
            total_price += meal.price
            order.append(meal.name)
            for item in meal.allergens.all():
                allergens.add(item.name)
    return {'order': order, 'price': total_price, 'allergens': allergens}
