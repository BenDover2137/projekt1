from django.db import models
from django.urls import reverse
# Create your models here.
from django.conf import settings
from django.db import models

class Note(models.Model):
    STATUS_CHOICES = ((1, 'malo_wazne'),
                      (2, 'srednio_wazne'),
                      (3  , 'bardzo_wazne'),)

    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    importance = models.IntegerField(choices=STATUS_CHOICES, default='1')

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-importance',)