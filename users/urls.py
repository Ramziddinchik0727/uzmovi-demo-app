from django.urls import path
from .serializers import SignUpSerializer
from .views import CreateUserView, VerifyAPIView, GetNewVerification, \
    ChangeUserInformationView, ChangeUserPhotoView, LoginView, LoginRefreshView, \
    LogOutView, ForgotPasswordView, ResetPasswordView

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('login/refresh/', LoginRefreshView.as_view(), name='login-refresh'),
    path('logout/', LogOutView.as_view(), name='logout'),
    path('signup/', CreateUserView.as_view(), name='signup'),
    path('verify/', VerifyAPIView.as_view(), name='verify'),
    path('new-verify/', GetNewVerification.as_view(), name='new-verify'),
    path('change-user/', ChangeUserInformationView.as_view(), name='change-user-information'),
    path('change-user-photo/', ChangeUserPhotoView.as_view(), name='change-user-photo'),
    path('forgot-password/', ForgotPasswordView.as_view(), name='forgot-password'),
    path('reset-password/', ResetPasswordView.as_view(), name='reset-password'),

]
