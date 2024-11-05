from allauth.socialaccount.models import SocialAccount
from django.conf import settings
from django.db import models


# Create your models here.
def upload_to(instance, filename):
    return "images/{filename}".format(filename=filename)


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    profile_pic = models.ImageField(upload_to=upload_to, blank=True, null=True)

    def __str__(self):
        return self.user.email

    def save(self, *args, **kwargs):
        if not self.profile_pic:
            if SocialAccount.objects.filter(user=self.user).exists():
                social_account = SocialAccount.objects.get(user=self.user)
                self.avatar_url = social_account.extra_data.get("picture", "")

        super().save(*args, **kwargs)
