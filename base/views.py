from django.shortcuts import render
from rest_framework import viewsets
from .serializer import BlogSerializer, UserSerializer
from .models import Blog, User
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
import logging
from django.views.decorators.csrf import csrf_exempt
import json
from django.core import serializers
from django.utils.crypto import get_random_string
logger = logging.getLogger(__name__)


@csrf_exempt
def UserList(request):
    if request.method == 'GET':
        user = User.objects.all()
        user_serializers = UserSerializer(user, many=True)
        return JsonResponse(user_serializers.data, safe=False)

    elif request.method == 'POST':
        user_data = JSONParser().parse(request)
        unique_id = get_random_string(length=32)
        user_data.setdefault("token")
        user_data['token'] = unique_id
        logger.warning(user_data)
        user_serializer = UserSerializer(data=user_data)
        if user_serializer.is_valid():
            user_serializer.save()
            return JsonResponse(user_data, status=status.HTTP_201_CREATED)
        return JsonResponse(user_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = User.objects.all().delete()
        return JsonResponse({'message': '{} users were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)


@csrf_exempt
def UserLogin(request):
    try:
        if request.method == 'POST':
            body_unicode = request.body.decode('utf-8')
            body = json.loads(body_unicode)
            email = body['email']
            password = body['password']
            if email == None or password == None:
                return JsonResponse({"message": "the email or password cannot be empty"})
            else:
                user_exist = User.objects.filter(email=email).exists()
                if user_exist == True:
                    user = User.objects.filter(email=email).values()
                    if list(user)[0]["password"] == str(password):
                        userslist = list(user)[0].setdefault("token")
                        unique_id = get_random_string(length=32)
                        list(user)[0]['token'] = unique_id
                        return JsonResponse(list(user)[0], safe=False)
                    else:
                        return JsonResponse({"message": "authentication failed"})
                else:
                    return JsonResponse({"message": "the user does not exists"})
    except Exception as err:
        logger.warning(err)
        return JsonResponse({"message": "something went wrong while logging in"})


@csrf_exempt
def Blog_list(request):
    if request.method == 'GET':
        blogs = Blog.objects.all()
        blog_serializer = BlogSerializer(blogs, many=True)
        return JsonResponse(blog_serializer.data, safe=False)

    elif request.method == 'POST':
        blog_serializer = BlogSerializer(request.POST,request.FILES)
        if blog_serializer.is_valid():
            blog_serializer.save()
            return JsonResponse(blog_serializer.data, status=status.HTTP_201_CREATED)
        return JsonResponse(blog_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        count = Blog.objects.all().delete()
        return JsonResponse({'message': '{} blogs were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
