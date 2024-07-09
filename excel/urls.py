"""
URL configuration for excel project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('aboutus',views.aboutus),
    path('courses',views.courses),
    path('contact',views.contact),
    path('login/',views.login),
    path('signup',views.signup),
    path('signupta',views.signupta),
    path('adminhome',views.adminhome),
    path('adddepartment',views.add_department),
    path('addteacher',views.add_teacher),
    path('logoutFun',views.logoutFun),
    path('incharge',views.incharge),
    path('incharge_edit',views.incharge_edit),
    path('batches',views.batches),
    path('add_batches',views.add_batches),
    path('classes',views.classes),
    path('incharge_add',views.incharge_add),
    path('add_class',views.add_class),
    path('class_edit',views.class_edit),
    path('batch_edit',views.batch_edit),
    path('delete_batch',views.delete_batch),
    path('delete_class',views.delete_class),
    path('viewfpage',views.viewfpage),
    path('viewstudent',views.viewstudent),
    path('editstudent',views.editstudent),
    path('viewteacher',views.viewteacher),
    path('editteacher',views.editteacher),
    path('deleteteacher',views.deleteteacher),
    path('deletestudent',views.deletestudent),
    path('msg_to_student',views.msg_to_student),
    path('msg_to_teacher',views.msg_to_teacher),
    path('dltmsg',views.dltmsg),
    path('employehome',views.employehome),
    path('msg_to_admin',views.msg_to_admin),
    path('profile_tr',views.profile_tr),
    path('received_msg',views.received_msg),
    path('time_table',views.time_table),
    path('add_table',views.add_table),
    path('edit_table',views.edit_table),
    path('delete_table',views.delete_table),
    path('set_class',views.set_class),
    path('in_set_class',views.in_set_class),
    path('delete_set_class',views.delete_set_class),
    path('studenthome',views.studenthome),
    path('s_timetable',views.s_timetable),
    path('join_class',views.join_class),
    path('privacypolicy',views.privacypolicy),
    path('cprivacypolicy',views.cprivacypolicy),
]
