


from django.urls import path
from  .import views

urlpatterns = [

    path('',views.home, name='home'),
   
    path('signup/', views.signup, name='signup'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    
     # projects
    path('projects/', views.project_list, name='project_list'),
    path('projects/add/', views.add_project, name='add_project'),
    path('projects/update/<int:pk>/', views.update_project, name='update_project'),
    path('projects/delete/<int:pk>/', views.delete_project, name='delete_project'),
    path('projects/', views.project_list, name='project_list'),
    path('projects/create/', views.create_project, name='create_project'),

   # Tasks
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/add/', views.add_task, name='add_task'),
   path('tasks/update/<int:id>/', views.update_task, name='update_task'),
    path('tasks/delete/<int:pk>/', views.delete_task, name='delete_task'),
    path('tasks/', views.task_list, name='task_list'),
    path('tasks/<int:task_id>/complete/', views.mark_task_completed, name='mark_task_completed'),
    path('tasks/<int:task_id>/', views.task_detail, name='task_detail'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('tasks/create/', views.create_task, name='create_task'),

    #  for documentation and contact form
    path('documentation/', views.documentation, name='documentation'),
    
    
]

