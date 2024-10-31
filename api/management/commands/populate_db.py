from django.core.management.base import BaseCommand
from api.models import Project
from datetime import date, timedelta
import random

class Command(BaseCommand):
    help = 'Populate the database with fake project data'

    def handle(self, *args, **kwargs):
        self.stdout.write('Populating database...')

        # Clear existing data
        Project.objects.all().delete()

        # Create fake projects
        for i in range(100):
            start_date = date.today() - timedelta(days=random.randint(1, 365))
            end_date = start_date + timedelta(days=random.randint(30, 365))

            Project.objects.create(
                project_name=f'Project {i+1}',
                start_date=start_date,
                end_date=end_date,
                project_manager=f'Manager {i+1}',
                customer_company=f'Company {i+1}'
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated database'))