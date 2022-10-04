from django.db import models

# Create your models here.


class Newsletter(models.Model):
    email = models.CharField(blank=True, max_length=200)
    creato = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name_plural = "Newsletter"
