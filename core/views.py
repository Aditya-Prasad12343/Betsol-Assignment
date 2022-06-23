from celery.result import AsyncResult
import subprocess as s
from django.shortcuts import render
from django.http import JsonResponse

from .tasks import test_func


def home(request):
    return render(request, 'home.html')

def run_long_task(request):
    if request.method == 'POST':
        l = request.POST.get('number')
        commands = request.POST.get('commands')
        sleep_duration = request.POST.get('sleep_duration')
        print(commands)
        print(sleep_duration)  
        task = test_func.delay(l,commands,sleep_duration)
        return JsonResponse({"task_id": task.id}, status=202)

    
def task_status(request, task_id):
    task = AsyncResult(task_id)
    if task.state == 'FAILURE' or task.state == 'PENDING':
        response = {
            'task_id': task_id,
            'state': task.state,
            'progression': "None",         
        }
        return JsonResponse(response, status=200)
    current = task.info.get('current', 0)
    total = task.info.get('total', 1)
    progression = (int(current) / int(total)) * 100 
    response = {
        'task_id': task_id,
        'state': task.state,
        'progression': progression,
    }
    return JsonResponse(response, status=200)