from django.shortcuts import render
from django.http.response import JsonResponse


def main_view(request):
    # for testing purpose
    # http://localhost:8000/api/v1/?test=world
    param_test = request.GET.get('test')
    response = {"message": "hello " + param_test}

    return JsonResponse(response)