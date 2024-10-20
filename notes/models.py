from django.db import models
<<<<<<< HEAD
from django.template.defaultfilters import length
from django.urls import reverse
=======

>>>>>>> bcd463fa155895d281d17e13cb33b5f89f695e4f
# Create your models here.
from django.conf import settings
from django.db import models

class Note(models.Model):
<<<<<<< HEAD
    STATUS_CHOICES = (( '1','malo wazne'),
                      ( '2','srednio wazne'),
                      ( '3','bardzo wazne'),)

=======
>>>>>>> bcd463fa155895d281d17e13cb33b5f89f695e4f
    title = models.CharField(max_length=50)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
<<<<<<< HEAD
    importance = models.CharField(max_length=13,choices=STATUS_CHOICES, default='1')

    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-importance',)
=======

    def __str__(self):
        return self.title
>>>>>>> bcd463fa155895d281d17e13cb33b5f89f695e4f
