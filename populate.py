import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'jobportal.settings')
django.setup()

from WebApp.models import *
from faker import Faker
from random import *

faker = Faker()


def populate(n):
    for i in range(n):
        fjobtitle = faker.random_element(elements=('Software Engineer', 'Software Testing', 'Data Science', '.Net Developer', 'Technical support', 'Java Develper', 'Artificial Intellegence', 'Python Developer', 'Android Developer' ))
        fexp = randrange(10)
        fcompany = faker.random_element(elements=('Wipro pvt ltd', 'Infosys pvt ltd', 'Google', 'Facebook', 'Oracle', 'Capgemini', 'Accenture', 'Deloite', 'Microsoft' ))
        flocations = faker.city()
        Job.objects.get_or_create(jobtitle=fjobtitle, exp=fexp, company=fcompany, locations=flocations)


populate(30)
