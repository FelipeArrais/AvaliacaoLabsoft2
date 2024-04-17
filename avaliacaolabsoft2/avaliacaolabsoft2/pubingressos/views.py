from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render
from django.http import HttpRequest
from .models import PubIngresso
import json

def ingressosDisponiveis():
    return PubIngresso.objects.filter(status=0)

def view_ingressos(request: HttpRequest):
    return render(request, "reserva_ingresso.html")

@api_view(['POST'])
def compra_ingresso(request: HttpRequest) -> Response:
    body: dict = json.loads(request.body.decode('utf-8'))

    fileira = body.get('fileira')
    numero = body.get('numero')
    ingressos = PubIngresso.objects.filter(fileira=fileira, numero=numero)

    if len(ingressos) > 0:
        ingresso = ingressos.first()
        if ingresso.status == 0:
            ingresso.status = 1
            ingresso.save()
            return Response({'success': True})
        return Response({'success': False})
    
    PubIngresso.objects.create(
        fileira=fileira,
        numero=numero,
        status=1
    )
    
    return Response({'success': True})

