from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RegisterSerializer,productserializer
from django.contrib.auth.models import User
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated
)
from .models import product


class register(APIView):

    def post(self,request):

        serializer=RegisterSerializer(data=request.data)


        if serializer.is_valid():

            serializer.save()

            return Response({
                "message":"user registered succesfully"
            })


        return Response(serializer.errors)
    

class productapiview(APIView):
    def get(self,request):
        get=product.objects.all()

        serializer=productserializer(get,many=True)

        return Response(serializer.data)

    def post(self,request):

        serializer=productserializer(data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)


class productsapiview(APIView):

    def get(self,request,id):

        try:
           prod= product.objects.get(id=id)
        except product.DoesNotExist:
            return Response("id not valid")

        serialzer=productserializer(prod)

        return Response(serialzer.data)

    def delete(self, request, id):

        try:
            prod = product.objects.get(id=id)
        except product.DoesNotExist:
            return Response("id not valid")

        prod.delete()

        return Response("deleted successfully")


    def put(self,request,id):
        prod= product.objects.get(id=id)

        serializer=productserializer(prod,data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data)

        return Response(serializer.errors)









    





