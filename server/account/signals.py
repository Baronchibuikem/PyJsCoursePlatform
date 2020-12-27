from django.dispatch import receiver, Signal
from django.db.models.signals import pre_delete, pre_save, post_save
from account.models import CustomUser


change_user_status = Signal(providing_args=["user"])
deactivate_user_status = Signal(providing_args=["user"])

# we are using this signal to change a user status to is not false upon user registration
@receiver(deactivate_user_status, sender=CustomUser)
def user_to_inactive(sender, **kwargs):
    """
    We are using this custom signal to change 'is_active' of a new user who is just registering
    on the platform to false to ensure the can't login if their account has not been verified
    """
    # Get the email of the user from the user object
    user_email = kwargs["user"]['email']
    # Use the email to get the owner of the email who will be the user registering 
    user = CustomUser.objects.get(email=user_email)
    # check if is_active is True, if yes check it to false
    try:
        if user.is_active:
            user.is_active = False
            print(user.password)
            user.save()
    except:
        user.save()


# we are using a custom dango signal to change a user status to is active
@receiver(change_user_status, sender=CustomUser)
def user_to_active(sender, **kwargs):
    # get the current user being verified
    user = kwargs["user"]
    try:
        if not user.is_active:
            user.is_active = True
            user.save()
    except:
        user.save()
    
