from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from SystemsApp.models import *
from SystemsApp.serializers import *

from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class SystemsList(APIView):
    """
    Lista todos los sistema y permite crear uno nuevo.
    """
    def get(self, request, format=None):
        system = Sistema.objects.all()
        serializer = SistemaSerializer(system, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = SistemaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class SystemsDetail(APIView):
    """
    Retrieve, update or delete a Sistema instance.
    """
    def get_object(self, pk):
        try:
            return Sistema.objects.get(id_system=pk)
        except Sistema.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        system = self.get_object(pk)
        serializer = SistemaSerializer(system)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        system = self.get_object(pk)
        serializer = SistemaSerializer(system, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        system = self.get_object(pk)
        system.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class CopyServerList(APIView):
    """
    Lista todos los servidores asociados a un sistema, donde se hace copia del respaldo.
    Permite crear dicha relación.
    """
    def get(self, request, format=None):
        respaldo = CopiaRespaldo.objects.all()
        serializer = CopiaRespaldoSerializer(respaldo, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = CopiaRespaldoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CopyServerDetail(APIView):
    """
    Retrieve, update or delete a CopiaRespaldo instance.
    """
    def get_object(self, pk):
        try:
            return CopiaRespaldo.objects.get(id_respaldo=pk)
        except CopiaRespaldo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        respaldo = self.get_object(pk)
        serializer = CopiaRespaldoSerializer(system)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        respaldo = self.get_object(pk)
        serializer = CopiaRespaldoSerializer(system, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        respaldo = self.get_object(pk)
        respaldo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
