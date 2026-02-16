from django.urls import path
from django.http import JsonResponse
from datetime import datetime

def info(request):
    today = datetime.now()
    new_year = datetime(today.year + 1, 1, 1)
    delta = new_year - today

    return JsonResponse({
        "days_before_new_year": delta.days
    })

urlpatterns = [
    path('info/', info),
]
