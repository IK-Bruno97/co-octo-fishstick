from rest_framework.serializers import ModelSerializer
from .models import MultiForm

class MultiFormSerializer(ModelSerializer):
    class Meta:
        model = MultiForm
        fields = '__all__'
