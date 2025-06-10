import os
import django
from datetime import datetime,timedelta
from django.utils.timezone import make_aware

os.environ.setdefault('DJANGO_SETTINGS_MODULE','fitness_project.settings')
django.setup()

from api.models import FitnessClass
from api.models import FitnessClass

# Delete all records
FitnessClass.objects.all().delete()


now =datetime.now()

classes = [
    {"Name":"yoga","Instructor":"asha","Start_time":now + timedelta(days=1,hours=9)},
    {"Name":"Zumba","Instructor":"john","Start_time":now + timedelta(days=1,hours=11)},
    {"Name":"HIIT","Instructor":"Kiran","Start_time":now + timedelta(days=2,hours=8)}
]

for cls in classes:
     FitnessClass.objects.create(
         Name = cls["Name"],
         Instructor = cls["Instructor"],
         Start_time =make_aware (cls ["Start_time"]),
         Total_slot = 10,
         Availabel_slot = 10
     )
print("created classes successfull.... ")
