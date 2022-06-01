from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField


# Create your models here.


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=450, blank=True)
    mobile = PhoneField(blank=True, help_text='Enter mobile number')
    avatar = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=get_user_model())
def create_profile(instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
