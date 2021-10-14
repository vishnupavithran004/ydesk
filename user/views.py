from django.shortcuts import render
from django.contrib.auth.models import User
from .models import UserProfile
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import RegisterUserSerializer
from django.contrib.auth.password_validation import validate_password
from rest_framework.permissions import AllowAny,IsAuthenticated
from django.contrib.auth import authenticate, login
from django.conf import settings
import jwt
from rest_framework import status



# Create your views here.
class UserRegister(APIView):

    """
    Creating new user:
    validating using serializer,
    saving the data
    """
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            # passing data to the serializer
            serializer = RegisterUserSerializer(data=request.data)
            if serializer.is_valid():
                # saving valid user data
                valid_data = serializer.validated_data
                ins_user = UserProfile(**valid_data)
                ins_user.set_password(valid_data.get('password'))
                ins_user.save()
                return Response({'statuis':1, 'message': 'success'})
            # returning validation errors
            return Response({'status': 0, 'message': serializer.errors})
        except Exception as e:
            return Response({'status':0, 'message': str(e)})


class UserLogin(APIView):

    """
    User login Api
    getting username and password and validating to
    authenticate user and generating the jwt token for the user
    """
    permission_classes = [AllowAny]

    def post(self, request):
        try:
            username = request.data.get('username')
            password = request.data.get('password')
            response = {}
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                # creates jwt token
                auth_token = jwt.encode({'user_id': user.id, 
                    'username': user.first_name, 
                    'email': user.username
                    }, str(settings.SECRET_KEY), algorithm="HS256")
                authorization = 'Bearer '+auth_token.decode("utf-8")
                response['data'] = {'status': 1, 'message': 'successfull'}
                header = {'Authorization': authorization}
                return Response(response['data'], headers=header, 
                    status=status.HTTP_200_OK)
            # returns response for unauthenticated user
            response['error'] = {
                'message': 'Invalid credentials', 'status': 0}
            return Response(response['error'], headers={},
                status= status.HTTP_401_UNAUTHORIZED)
        except Exception as e:
            return Response({'status': 0, 'message': str(e)})
