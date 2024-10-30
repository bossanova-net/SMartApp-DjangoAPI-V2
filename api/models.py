from django.db import models

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_name = models.CharField(max_length=200)
    start_date = models.DateField()
    end_date = models.DateField()
    project_manager = models.CharField(max_length=100)
    customer_company = models.CharField(max_length=200)

    def __str__(self):
        return self.project_name