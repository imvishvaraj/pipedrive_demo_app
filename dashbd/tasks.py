from cmsapp import celery_app
from .pipedrive_client import PPerson
from .models import PDKey, Persons

@celery_app.task
def see_you():
    print("See you in ten seconds!")

@celery_app.task
def fetch_data():
    key = PDKey.objects.get()
    ppl = PPerson(key)
    persons = ppl.get_all()
    print(persons)
    print(type(persons))
    for person in persons:
        print(person)
        try:
            per = Persons.objects.get(person['id'])
        except:
            per = Persons(id=person['id'], name=person['name'])
            per.save()


celery_app.conf.beat_schedule = {
    "see-you-in-ten-seconds-task": {
        "task": "periodic.see_you",
        "schedule": 10.0
    }
}