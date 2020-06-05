from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Channel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='channel_pics')

    def __str__(self):
        return f'{self.user.username} Channel'

    @property
    def subscriber(self):
        return Subscribe.objects.filter(subscribe_user=self.user).count()

    @property
    def subscribing(self):
        return Subscribe.objects.filter(user=self.user).count()

    def save(self, force_insert=False, force_update=False, using=None, update_fields=None):
        super().save()

    def get_absolute_url(self):
        return reverse('channel', kwargs={'pk':self.pk})
        

class Subscribe(models.Model):
    user = models.ForeignKey(User, related_name="user", on_delete=models.CASCADE)
    subscribe_user = models.ForeignKey(User, related_name="subscribe_user", on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)