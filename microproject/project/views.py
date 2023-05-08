from django.shortcuts import render, redirect
from .models import MultiForm
from .serializer import MultiForm
import json
from .serializer import MultiFormSerializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
# Create your views here.


def index(request):
    return render(request, "index.html")

def result(request):
    result = MultiForm.objects.all()
    return render(request, "result.html", {"result": result})

@api_view(['POST'])
def receipt(request):
    data = request.data
    print(json.loads(data))
    message = MultiForm.objects.create(
                store_name = data['store'],
                balance = data['balance'],
                price = data['price'],
                network = data['network'],
                address = data['address'],
                email = data['email'],
    )
    serializer = MultiFormSerializer(message, many=True)
    return Response(serializer.data)