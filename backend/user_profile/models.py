from django.db import models


# Create your models here.
def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class Profile(models.Model):
    user = models.OneToOneField("auth.User", on_delete=models.CASCADE)
    bio = models.TextField
    profile_pic = models.ImageField(upload_to=upload_to, blank=True, null=True)
