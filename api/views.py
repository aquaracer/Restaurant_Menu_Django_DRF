from meals.models import Meals
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated

from .serializers import MealSerializer


class ApiMealViewSet(ModelViewSet):
    """CRUD информации о блюде из меню"""

    queryset = Meals.objects.all()
    serializer_class = MealSerializer
    permission_classes = (IsAuthenticated,)
