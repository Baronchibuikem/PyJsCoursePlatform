from django.db import models
from django.contrib.auth.models import AbstractUser, Group
from django.contrib.auth.hashers import make_password
from cloudinary.models import CloudinaryField
import cloudinary
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import Permission
from django.contrib.contenttypes.models import ContentType



# Here we are extending django user model
class CustomUser(AbstractUser):

    class Types(models.TextChoices):
        """
        Setting the types of user's we will have
        """
        Student = "Student", "Student"
        Instructor = "Instructor", "Instructor"
    user_type = models.CharField(_("Type"),
                                 max_length=50, choices=Types.choices, default=Types.Student)
    username = models.CharField(
        null=True, blank=True, max_length=50, unique=True)
    email = models.EmailField(unique=True)
    # bio = models.CharField(max_length=250, null=True, blank=True)
    # image = CloudinaryField("user_image", null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['user_type', 'username']

    def __str__(self):
        return f'{self.username}'

    def save(self, *args, **kwargs):
        if self.is_staff:
            self.password = self.password
        elif not self.is_staff:
            self.password = make_password(self.password)
        super().save(*args, **kwargs)


class StudentManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=CustomUser.Types.Student)


class StudentProfile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)


# Student abstract model
class Student(CustomUser):
    base_type = CustomUser.Types.Student
    objects = StudentManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = CustomUser.Types.Student
        return super().save(*args, **kwargs)

    @ property
    def studentprofile(self):
        return self.studentprofile


class InstructorManager(models.Manager):
    """[summary]
    Custom model manager for querying Instructor objects
    """

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(user_type=CustomUser.Types.Instructor)


class Instructor(CustomUser):
    """
    Models for Instructor
    """
    base_type = CustomUser.Types.Instructor
    objects = InstructorManager()

    class Meta:
        proxy = True

    def save(self, *args, **kwargs):
        if not self.pk:
            self.user_type = CustomUser.Types.Instructor
        return super().save(*args, **kwargs)


class GlobalPermissionManager(models.Manager):
    def get_queryset(self):
        return super(GlobalPermissionManager, self).\
            get_queryset().filter(content_type__model='global_permission')


class GlobalPermission(Permission):
    """A global permission, not attached to a model"""

    objects = GlobalPermissionManager()

    class Meta:
        proxy = True
        verbose_name = "global_permission"

    def save(self, *args, **kwargs):
        ct, created = ContentType.objects.get_or_create(
            model=self._meta.verbose_name, app_label=self._meta.app_label,
        )
        self.content_type = ct
        super(GlobalPermission, self).save(*args)

# # for deleting a photo
# @receiver(pre_delete, sender=CustomUser)
# def photo_delete(sender, instance, **kwargs):
#     cloudinary.uploader.destroy(instance.image.public_id)
