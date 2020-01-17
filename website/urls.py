from django.urls import path
from . import views

urlpatterns = [
    path('settings', views.settings, name='settings'),

    # Login Logout
    path('login', views.login_view, name='login'),
    path('logout', views.logout_view, name='logout'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Branch
    path('branches', views.view_branches, name='branch-viewall'),
    path('change-branch', views.change_branch, name='branch-change'),

    # Course
    path('courses', views.view_courses, name='course-viewall'),

    # Calendar
    path('calendar', views.calendar, name='calendar'),

    # Student
    path('student/all', views.student, name='student-viewall'),
    path('student/add', views.student_add, name='student-add'),

    #Batch
    path('batch/all',views.batch,name = 'batch-view'),
    path('batch/add',views.batch_add,name = 'batch-add'),
    path('batch/edit/<int:pk>',views.batch_edit,name = 'batch-edit'),


]
