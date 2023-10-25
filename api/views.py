from django.shortcuts import render
from rest_framework import generics
from .models import SkinType
from .serializers import SkinTypeSerializer


# Create your views here.
def profile_view(request):
    return render(request, 'api/profile.html')


class SkinTypeList(generics.ListCreateAPIView):
    queryset = SkinType.objects.all()
    serializer_class = SkinTypeSerializer
