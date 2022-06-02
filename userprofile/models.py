from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from phone_field import PhoneField


# Create your models here.
class PersonalInfo(models.Model):
    street_address = models.CharField(max_length=225)
    city_name = models.CharField(max_length=225)
    notes_for_address = models.TextField(blank=True , null=True)
    mobile = PhoneField(blank=True)

    def __str__(self):
        return "{}-{}-{}-{}".format(self.street_address,self.city_name,self.notes_for_address, self.mobile)


class UserProfile(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, related_name='profile')
    user_info = models.ManyToManyField(PersonalInfo)
    avatar = models.ImageField(upload_to='profile_images/', blank=True)

    def __str__(self):
        return self.user.username


@receiver(post_save, sender=get_user_model())
def create_profile(instance, created, *args, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
