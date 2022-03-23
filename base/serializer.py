# import serializers from the REST framework
from rest_framework import serializers
from django import forms
# import the todo data model
from .models import Blog, User

# create a serializer class


class BlogSerializer(forms.ModelForm):
    # created_by=serializers.CharField(source='User.email')
    class Meta:
        model = Blog
        fields = ('title',
                  'description',
                  'created_by',
                  "image"
                  )

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "username", "admin")
 