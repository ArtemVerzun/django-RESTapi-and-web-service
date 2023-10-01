from django.db import models


class User(models.Model):
    objects = models.Manager()

    login = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    registration_date = models.DateField(auto_now_add=True)
    birth_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.login


class Event(models.Model):
    objects = models.Manager()

    title = models.CharField(max_length=255)
    text = models.TextField()
    creation_date = models.DateField(auto_now_add=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='created_events')
    participants = models.ManyToManyField(User, related_name='events_participated')

    def __str__(self):
        return self.title

