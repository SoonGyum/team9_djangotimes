from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
class SignupView(APIView):
    def post(self, request):
        pass