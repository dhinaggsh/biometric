from django.db import models

class attendece(models.Model):
    user_id = models.CharField(max_length=50)
    name = models.CharField(max_length=100, blank=True)
    timestamp = models.DateTimeField()
    status = models.CharField(max_length=50)
    
    def __str__(self):
        return f"{self.user_id} - {self.timestamp}"
    
    