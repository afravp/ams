from django.contrib import admin
from django.urls import path
from admin_employee import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('employee_reg/',views.employee_reg,name="Employee_Registration"),
    path('subjectdrop/',views.select_subject,name="select_subject"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)