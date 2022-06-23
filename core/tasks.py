import time
from celery import shared_task
from mysite.celery import app
import subprocess as s

from django.core.mail import send_mail


    
@app.task(bind=True)
def test_func(self,l,commands,sleep_duration):
    for i in range(int(l)):
        time.sleep(int(sleep_duration))
        print(s.getoutput(commands))
        self.update_state(state='Running',
                          meta={'current': i, 'total': l})
    print('Task completed')
    return {'current': 100, 'total': 100, }
