from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from SystemsApp.models import *
from SystemsApp.serializers import *

from django.http import Http404
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django_celery_beat.models import PeriodicTask, IntervalSchedule

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
            d=serializer.save()
            sis=Sistema.objects.get(id_system=d.id_system)
            if sis.type_frequency=="days":
                schedule, created = IntervalSchedule.objects.get_or_create(every=sis.frequency,period=IntervalSchedule.DAYS )
            elif sis.type_frequency=="hours":
                schedule, created = IntervalSchedule.objects.get_or_create(every=sis.frequency,period=IntervalSchedule.HOURS )
            elif sis.type_frequency=="minutes":
                schedule, created = IntervalSchedule.objects.get_or_create(every=sis.frequency,period=IntervalSchedule.MINUTES )
            elif sis.type_frequency=="seconds":
                schedule, created = IntervalSchedule.objects.get_or_create(every=sis.frequency,period=IntervalSchedule.SECONDS ) 
            pe=PeriodicTask.objects.create(interval=schedule, name=str(sis.id_system),task='run_script', args=json.dumps([sis.id_system]))
            pe.enabled = True
            pe.save()
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
        print("PASO")
        if serializer.is_valid():
            serializer.save()
            pe=PeriodicTask.objects.filter(name=str(system.id_system))
            sis=Sistema.objects.get(id_system=system.id_system)
            if sis.type_frequency=="days":
                schedule, created = IntervalSchedule.objects.get_or_create(every=sis.frequency,period=IntervalSchedule.DAYS )
            elif sis.type_frequency=="hours":
                schedule, created = IntervalSchedule.objects.get_or_create(every=sis.frequency,period=IntervalSchedule.HOURS )
            elif sis.type_frequency=="minutes":
                schedule, created = IntervalSchedule.objects.get_or_create(every=sis.frequency,period=IntervalSchedule.MINUTES )
            elif sis.type_frequency=="seconds":
                schedule, created = IntervalSchedule.objects.get_or_create(every=sis.frequency,period=IntervalSchedule.SECONDS ) 
            for i in pe:
                i.interval=schedule
                i.enabled = True
                i.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        system = self.get_object(pk)
        pe=PeriodicTask.objects.filter(name=str(system.id_system))
        for i in pe:
            i.enabled = False
            i.save()
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
