from django.urls import path
from .views import *
from .push_method.getatten import *


urlpatterns = [
    path('get_attendance', view=get_attendance, name='get_attendence'),
    path('selected_user_attendance', view=selected_user_attendance, name='selected_user_attendance'),
    
    path('get_users', view=get_users, name='get_users'),
    path('create_user', view=create_user, name='create_user'),
    path('delete_user', view=delete_user, name='delete_user'),
    path('update_user', view=update_user, name='update_user'),
    
    path('biometric_push', view=biometric_push, name='biometric_push'),
    
    path('push', view=push_attendance, name='push_attendance'),
    path('process_data', view=process_data, name='process_data'),
    path('iclock/getrequest.aspx', view=getrequest),
    path('iclock/cdata.aspx', view=cdata),
]
