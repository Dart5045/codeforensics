from django.shortcuts import render
from django.http import JsonResponse

def sensitive_info(request):
    data = ["user1", "user2", "user3"]  # Aquí hay un error intencionado
    return JsonResponse({"data": data[1]})  # Bug: índice fuera de rango
