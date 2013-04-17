from django.db import models

# Create your models here.

class ImportSession(models.Model):
    import_date = models.DateTimeField('date imported')

class Contact(models.Model):
    def __unicode__(self):
        return self.email
    session = models.ForeignKey(ImportSession)
    email = models.CharField(max_length=200)
    highrise_id = models.CharField(max_length=200)
    import_date = models.DateTimeField('date imported')
