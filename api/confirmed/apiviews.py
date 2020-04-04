from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Confirmed
from .serializers import CategorySerializer


class CategoryList(APIView):
    @staticmethod
    def get(request):
        categories = Confirmed.objects.all()
        data = CategorySerializer(categories, many=True).data
        return Response(data)


