from django.core.validators import RegexValidator
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _
from Core.models import User


def profile_upload_path(instance, filename):
    path = f'Users/{instance.user.id}/{filename}'
    return path


CHOSE_GENDER = [('M', 'Male'), ('F', 'Female')]


class Profile(models.Model):
    # User Profile model
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True, unique=True
    )
    photo = models.ImageField(
        verbose_name="Profile photo", blank=True, null=True,
        upload_to=profile_upload_path
    )
    website = models.URLField(
        verbose_name='Website', blank=True, null=True
    )
    birthday = models.DateField(
        verbose_name='Date of Birth', blank=True, null=True
    )
    gender = models.CharField(
        verbose_name='Gender', max_length=1, blank=True, null=True,
        choices=CHOSE_GENDER
    )
    father_name = models.CharField(
        verbose_name='Name of Father', max_length=255, blank=True, null=True
    )
    mother_name = models.CharField(
        verbose_name='Name of Mother', max_length=255, blank=True, null=True
    )
    nid = models.CharField(
        verbose_name='National ID', max_length=17, unique=True,
        blank=True, null=True,
        validators=[RegexValidator(
            r'^(\d{10}|\d{13}|\d{17})$',
            message='Numeric 10/13/17 digits (ex: 1234567890)'
        )]
    )
    address = models.TextField(
        _('Street Address'), max_length=255, blank=True, null=True
    )

    def __str__(self):
        return f'{self.user}'


@receiver(post_save, sender=User)
def create_or_update_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.get_or_create(user=instance)
    instance.profile.save()
