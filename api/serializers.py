from rest_framework import serializers

from meals.models import Meals


class MealSerializer(serializers.ModelSerializer):
    """Информация о блюде"""

    class Meta:
        model = Meals
        fields = "__all__"
