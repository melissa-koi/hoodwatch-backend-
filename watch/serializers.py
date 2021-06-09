from rest_framework import serializers
from .models import User, Neighborhood, Business, Profile
from django import forms

class UserSerializer(serializers.ModelSerializer):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')
    class Meta:
        model = User
        fields = ['id', 'username', 'email' ,'password']

class BusinessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Business
        fields = ['id', 'business_name', 'email', 'neighborhood', 'user']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['user', 'avatar', 'email', 'neighborhood']

class NeighborhoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Neighborhood
        fields = ['id','name', 'location', 'occupants_count']



