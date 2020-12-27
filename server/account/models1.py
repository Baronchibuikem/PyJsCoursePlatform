import cloudinary
from cloudinary.models import CloudinaryField
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import AbstractUser, Group
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


class CustomUser(AbstractUser):
    username = models.CharField(
        null=True, blank=True, max_length=50, unique=True)
    email = models.EmailField(unique=True)
    is_student = models.BooleanField(default=False)
    is_instructor = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", ]

    def __str__(self):
        return f'{self.username}'

    # def save(self, *args, **kwargs):
    #     if self.is_staff:
    #         self.password = make_password(self.password, hasher='default')
    #     elif not self.is_staff:
    #         self.password = make_password(self.password, hasher='default')
    #     super().save(*args, **kwargs)


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    age = models.IntegerField()
    location = models.CharField(max_length=50)

    class Meta:
        verbose_name = _('Student')
        verbose_name_plural = _('students')

    def __str__(self):
        return self.user.email


class Instructor(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, related_name="instructor")
    #phone = models.PhoneNumberField()
    primary_language = models.CharField(max_length=25)
    other_languages = models.CharField(max_length=250)
    years_of_experience = models.IntegerField()
    currently_work_at = models.CharField(max_length=25)
    date_registered = models.DateField(default=timezone.now)

    class Meta:
        verbose_name = _('Instructor')
        verbose_name_plural = _('instructors')

    def __str__(self):
        return f'{self.user.first_name}{self.user.last_name}'
