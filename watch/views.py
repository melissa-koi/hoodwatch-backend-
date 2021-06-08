from django.shortcuts import render
from rest_framework import status
from django.http import Http404,QueryDict
from .serializers import BusinessSerializer, NeighborhoodSerializer, UserSerializer, ProfileSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import User, Business, Neighborhood, Profile

# Create your views here.
class NeighborhoodList(APIView):
    serializer_class=NeighborhoodSerializer
    def get_hood(self, pk):
        try:
            return Neighborhood.objects.get(pk=pk)
        except Neighborhood.DoesNotExist:
            return Http404()

    def get(self, request,pk,format=None):
        hood = self.get_hood(pk)
        serializers = self.serializer_class(hood)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        hood = self.get_hood(pk)
        serializers = self.serializer_class(hood, request.data)
        if serializers.is_valid():
            serializers.save()
            hood_list = serializers.data
            response = {
                'data': {
                    'neighbourhood': dict(hood_list),
                    'status': 'success',
                    'message': 'Neighbourhood updated successfully',
                }
            }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, pk, format=None):
        hood = self.get_hood(pk)
        hood.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IndividualHood(APIView):
    serializer_class=NeighborhoodSerializer
    def get(self, request, format=None):
        hood=Neighborhood.objects.all()
        serializers=self.serializer_class(hood, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            hood=serializers.data
            response = {
                'data': {
                    'neighbourhood': dict(hood),
                    'status': 'success',
                    'message': 'Neighbourhood created successfully',
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, format=None):
        hood=Neighborhood.objects.all()
        serializers=self.serializer_class(hood, many=True)
        return Response(serializers.data)

class BusinessList(APIView):
    serializer_class=BusinessSerializer
    def get_business(self, pk):
        try:
            return Business.objects.get(pk=pk)
        except Business.DoesNotExist:
            return Http404()

    def get(self, request,pk,format=None):
        business = self.get_business(pk)
        serializers = self.serializer_class(business)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        business = self.get_business(pk)
        serializers = self.serializer_class(business, request.data)
        if serializers.is_valid():
            serializers.save()
            business_list = serializers.data
            response = {
                'data': {
                    'business': dict(business_list),
                    'status': 'success',
                    'message': 'Business updated successfully',
                }
            }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        business = self.get_business(pk)
        business.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IndividualBusiness(APIView):
    serializer_class=BusinessSerializer

    def get(self, request,format=None):
        business=Business.objects.all()
        serializers=self.serializer_class(business, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            business=serializers.data
            response = {
                'data': {
                    'business': dict(business),
                    'status': 'success',
                    'message': 'Business created successfully',
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, format=None):
        business=Business.objects.all()
        serializers=self.serializer_class(business, many=True)
        return Response(serializers.data)

class UserList(APIView):
    serializer_class=UserSerializer
    def get_user(self, pk):
        try:
            return User.objects.get(pk=pk)
        except User.DoesNotExist:
            return Http404()

    def get(self, request,pk,format=None):
        user = self.get_user(pk)
        serializers = self.serializer_class(user)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        user = self.get_user(pk)
        serializers = self.serializer_class(user, request.data)
        if serializers.is_valid():
            serializers.save()
            user_list = serializers.data
            response = {
                'data': {
                    'user': dict(user_list),
                    'status': 'success',
                    'message': 'User updated successfully',
                }
            }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        user = self.get_user(pk)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class IndividualUser(APIView):
    serializer_class=UserSerializer

    def get(self, request,format=None):
        user = User.objects.all()
        serializers=self.serializer_class(user, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers=self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            user=serializers.data
            response = {
                'data': {
                    'user': dict(user),
                    'status': 'success',
                    'message': 'User created successfully',
                }
            }
            return Response(response, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, format=None):
        user=User.objects.all()
        serializers=self.serializer_class(user, many=True)
        return Response(serializers.data)

class ProfileList(APIView):
    serializer_class=ProfileSerializer
    def get_profile(self, pk):
        try:
            return Profile.objects.get(pk=pk)
        except Profile.DoesNotExist:
            return Http404()

    def get(self, request,pk,format=None):
        profile = self.get_profile(pk)
        serializers = self.serializer_class(profile)
        return Response(serializers.data)

    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = self.serializer_class(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            profile_list = serializers.data
            response = {
                'data': {
                    'profile': dict(profile_list),
                    'status': 'success',
                    'message': 'Profile updated successfully',
                }
            }
            return Response(response)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class IndividualProfile(APIView):
    serializer_class=ProfileSerializer

    def get(self, request,format=None):
        profile=Profile.objects.all()
        serializers=self.serializer_class(profile, many=True)
        return Response(serializers.data)

    def delete(self,request, format=None):
        profile=Profile.objects.all()
        serializers=self.serializer_class(profile, many=True)
        return Response(serializers.data)