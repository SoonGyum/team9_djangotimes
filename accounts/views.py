from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User
from .validators import validate_signup
from .serializers import UserSerializer
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework_simplejwt.exceptions import TokenError


class SignupView(APIView):
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request):
        is_valid, err_msg = validate_signup(request.data)
        if not is_valid:
            return Response({"error": err_msg}, status=400)

        username = request.data.get("username")
        password = request.data.get("password")
        email = request.data.get("email")
        introductions = request.data.get("introductions", "")
        profile_image = request.FILES.get("profile_image")

        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            introductions=introductions,
            profile_image=profile_image
        )

        serializer = UserSerializer(user)
        return Response(serializer.data)


class SigninView(APIView):
    def post(self, request):
        user = authenticate(**request.data)
        if not user:
            return Response(
                {"error": "아이디 혹은 비밀번호가 올바르지 않습니다."}, status=400
            )

        res_data = UserSerializer(user).data
        refresh = RefreshToken.for_user(user)
        res_data["access_token"] = str(refresh.access_token)
        res_data["refresh_token"] = str(refresh)
        return Response(res_data)


class SignoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        refresh_token_str = request.data.get("refresh_token")
        try:
            refresh_token = RefreshToken(refresh_token_str)
        except TokenError as e:
            return Response({"msg": str(e)}, status=400)
        
        refresh_token.blacklist()
        return Response(status=200)


class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, username):
        user = User.objects.get(username=username)
        serializer = UserSerializer(user)
        return Response(serializer.data)