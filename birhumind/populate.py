import os
import django
print("Before setting up Django")
os.environ.setdefault('django setting module', 'birhumindapp.settings')
django.setup()

print("setup")

import random
from birhumindapp.models import Topic, WebPage, AccessRecord
from faker import Faker


fakegen=Faker()
topics=['search', 'social', 'Marketplace', 'News', 'Games']

def add_topic():
    t=Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):
    for entry in range(N):
        top=add_topic()
        fake_url=fakegen.url()
        fake_date=fakegen.date()
        fake_name=fakegen.company()

        WebPg=WebPage.objects.get_or_create(topic=top, url=fake_url, name=fake_name)[0]
        acc_rec=AccessRecord.objects.get_or_create(name=WebPg, date=fake_date)[0]
if __name__=='__main__':
    print("populating script")
    populate(20)
    print("populating complete")