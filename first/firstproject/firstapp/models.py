from django.db import models

class Topic(models.Model):
    top_name= models.CharField(max_length=256, unique=True)

    def __str__(self):
        return self.top_name

class Webpage(models.Model):
    topic=models.ForeignKey(Topic, on_delete= models.CASCADE)
    name = models.CharField(max_length=250, unique=True)
    url = models.URLField(max_length = 200, unique=True)
    
    def __str__(self):
        return self.name
class AccessRecord(models.Model):
    name= models.ForeignKey(Webpage, on_delete= models.CASCADE)
    date= models.DateField()
    def __str__(self):
        return str(self.date)
    
    
    
    
