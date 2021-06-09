from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.
class Neighborhood(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    occupants_count = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def save_neighborhood(self):
        self.save()

    def delete_neighborhood(self):
        self.delete()

    @classmethod
    def find_neighborhood(cls, id):
        return cls.objects.filter(name__icontains=id)

    @classmethod
    def update_neighborhood(cls, id, name):
        update = cls.objects.filter(id=id).update(name=name)
        return update

class Profile(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    avatar=CloudinaryField('photos')
    email=models.EmailField()
    neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE)

    def __str__(self):
        """Return username"""
        return self.name

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()


class Business(models.Model):
    business_name=models.CharField(max_length=50)
    user=models.ForeignKey(User,on_delete=models.CASCADE, null=True)
    email=models.EmailField()
    neighborhood=models.ForeignKey(Neighborhood,on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    def save_business(self):
        self.save()

    def delete_business(self):
        self.delete()

    @classmethod
    def find_business(cls, name):
        return cls.objects.filter(name__icontains=name)

    @classmethod
    def update_business(cls, id, name):
        update = cls.objects.filter(id=id).update(name=name)
        return update

