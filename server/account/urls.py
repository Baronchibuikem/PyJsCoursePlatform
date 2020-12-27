from django.urls import path, include
from account.views import (StudentRegisterViewSet, InstructorRegisterViewSet,
                           LoginViewSet, VerifyEmail, UserListAPIView)
# from knox import views as knox_views
from rest_framework import routers

app_name = "account"

router = routers.DefaultRouter()


urlpatterns = [
    path("login/", LoginViewSet.as_view(), name="login"),
    path("student/register/", StudentRegisterViewSet.as_view(),
         name="register-student"),
    path("instructor/register/", InstructorRegisterViewSet.as_view(),
         name="register-instructor"),
    path("email-verify/<id>/<token>/", VerifyEmail, name="email-verify"),
    # path("logout/", knox_views.LogoutView.as_view(), name="knox_logout"),
    path("users/", UserListAPIView.as_view(), name="user_list"),
    # path("user/<int:pk>/", UserDetailAPIView.as_view(), name="user_detail"),
]

urlpatterns += router.urls
