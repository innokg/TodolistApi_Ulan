from django.contrib.auth import authenticate
from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from authentication.serializers import RegisterSerializer, LoginSerializer
from rest_framework import response, status


class RegisterAPIView(GenericAPIView): # cоздаем класс для регистрации Апишки

    serializer_class = RegisterSerializer

    def post(self, request):
        serializers = self.serializer_class(data=request.data)

        if serializers.is_valid(): # после того как мы создали аккаунт, нужно сообщить юзеру, что его аккаунт создан
            serializers.save()
            return response.Response(serializers.data, status=status.HTTP_201_CREATED)

        return response.Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) # данные от пользователя неправильные

class LoginAPIView(GenericAPIView):
    authentication_classes = []

    serializer_class = LoginSerializer # используется для проверки и десериализации ввода, а также для сериализации вывода

    def post(self, request):
        email = request.data.get('email', None)
        password = request.data.get('password', None)

        user = authenticate(username=email, password=password)

        if user:
            serializer=self.serializer_class(user)

            return response.Response(serializer.data, status=status.HTTP_200_OK)
        return response.Response({'message': 'Неправильные данные, попробуйте снова!'}, status=status.HTTP_401_UNAUTHORIZED)