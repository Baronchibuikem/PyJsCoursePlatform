# from django.contrib.auth.models import User
from rest_framework import status, generics, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from account.models import CustomUser, Student
from knox.models import AuthToken
from rest_framework import status, generics, permissions
# from account.permissions import IsOwnerOrReadonly
from account.serializers import (
    LoginSerializer, UserSerializer, GetUserSerializer)
from utils.sendEmail import Email
from django.contrib.sites.shortcuts import get_current_site
from django.urls import reverse
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect, render
from account.signals import change_user_status, deactivate_user_status


class LoginViewSet(generics.GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = (permissions.AllowAny,)

    error_messages = {
        'invalid': "Invalid username or password",
        'pending_confirmation': "Sorry, this account is yet to be verified. Please check the mail sent to you",
    }

    def _error_response(self, message_key):
        data = {
            'success': False,
            'message': self.error_messages[message_key],
            'user_id': None,
        }
        return data

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            print(serializer.data['email'])
            user_obj = authenticate(
                request, email=serializer.data["email"], password=serializer.data["password"])
            print(user_obj)
            if user_obj != None:
                if user_obj.is_active:
                    login(request, user_obj)
                    user = CustomUser.objects.get(username=user_obj)
                    return Response({
                        "user": GetUserSerializer(user, context=self.get_serializer_context()).data,
                        "token": AuthToken.objects.create(user)[1], },
                        status.HTTP_200_OK)
                if not user_obj.is_active:
                    return Response(self._error_response('pending_confirmation'), status.HTTP_400_BAD_REQUEST)
            else:
                return Response(self._error_response('invalid'), status.HTTP_400_BAD_REQUEST)
        return Response(serializer.errors, status.HTTP_400_BAD_REQUEST)


class StudentRegisterViewSet(generics.GenericAPIView):
    """
    For registering a user into the database as a student
    """
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            # get the user email
            print(serializer.data['email'])
            user_email = serializer.data["email"]
            # use the email to get the user object from CustomUser model in the database
            get_current_user_email = CustomUser.objects.get(email=user_email)
            user_obj = serializer.data
            # Send a signal to change the user is_active to false
            deactivate_user_status.send(sender=CustomUser, user=user_obj)
            # generate a token for the user
            token = AuthToken.objects.create(get_current_user_email)[1]
            # get the current site and domain name
            current_site = get_current_site(request).domain
            # Here we are calling the endpoint to email-verify and passing in the user id and token dynamically
            relative_link = reverse(
                "account:email-verify", args=[user_obj["id"], token])
            # Here we pass in the current_site and the relative_link with it's added arguments
            absolute_url = f"http://{current_site}{relative_link}"
            email_body = f'Hi {user_obj["last_name"]} {user_obj["first_name"]}, please use the link below to verify your email \n {absolute_url}'
            data = {"email_body": email_body,
                    'email_subject': 'Verify your email',
                    "to_email": user_email
                    }
            # sending the mail to the user
            Email.send_mail(data)
            return Response({
                "user": user_obj,
                "token": token,
                "message": "Account created successfully"
            }, status.HTTP_201_CREATED,)


# class InstructorRegisterViewSet(generics.GenericAPIView):
#     """
#     For registering a user into the database as an Instructor
#     """
#     serializer_class = InstructorSerializer
#     permission_classes = (permissions.AllowAny,)

#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             serializer.save()
#             # get the user email
#             user_email = serializer.data["user"]["email"]
#             # use the email to get the user object from CustomUser model in the database
#             get_current_user_email = CustomUser.objects.get(email=user_email)
#             user_obj = serializer.data["user"]
#             # Send a signal to change the user is_active to false
#             deactivate_user_status.send(sender=CustomUser, user=user_obj)
#             # generate a token for the user
#             token = AuthToken.objects.create(get_current_user_email)[1]
#             # get the current site and domain name
#             current_site = get_current_site(request).domain
#             # Here we are calling the endpoint to email-verify and passing in the user id and token dynamically
#             relative_link = reverse(
#                 "account:email-verify", args=[user_obj["id"], token])
#             # Here we pass in the current_site and the relative_link with it's added arguments
#             absolute_url = f"http://{current_site}{relative_link}"
#             email_body = f'Hi {user_obj["last_name"]} {user_obj["first_name"]}, please use the link below to verify your email \n {absolute_url}'
#             data = {"email_body": email_body,
#                     'email_subject': 'Verify your email',
#                     "to_email": user_email
#                     }
#             # sending the mail to the user
#             Email.send_mail(data)
#             return Response({
#                 "user": user_obj,
#                 "token": token,
#                 "message": "Account created successfully"
#             }, status.HTTP_201_CREATED,)


def VerifyEmail(request, id, token):
    """
    Used to verify a user through a link embedded in the mail that was sent to him/her
    during registration
    """
    user = CustomUser.objects.get(id=id)
    # Calling a custom signal to change the user is_active to True
    change_user_status.send(sender=CustomUser, user=user)
    template = "account/email_auth_confirmation.html"
    context = {"user": user}
    return render(request, template, context)


class UserListAPIView(generics.ListAPIView):
    """
    This endpoint is used for listing all registered users in the platform,
    but only an admin user can access the data in this endpoint
    """
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.AllowAny,)

# class UserDetailAPIView(generics.RetrieveUpdateAPIView):
#     """
#     For retrieving a single user from the database.
#     """
#     queryset = CustomUser.objects.all()
#     serializer_class = GetUserSerializer
#     permission_classes = (IsOwnerOrReadonly, )

#     def get(self, request, pk, format=None):
#         try:
#             user_info = OrderedDict()
#             user = self.get_object()
#             serializer = GetUserSerializer(
#             user, context=self.get_serializer_context())
#             user_info['user'] = serializer.data
#             print(user_info)
#             return Response({"user_details": user_info, "status":status.HTTP_200_OK})
#         except:
#             return Response({"status": "User ID not found"})
