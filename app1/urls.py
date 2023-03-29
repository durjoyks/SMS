from django.urls import path
from . import views
urlpatterns = [

   path('login/',views.loginstd,name="login"),
   path('register/',views.registerstd,name="register"),
   path('logout/',views.logoutUser,name="logout"),

   path('request/',views.Request,name="request"),


   path('',views.home,name="home"),
   path('userpage/',views.userPage,name="user-page"),
   path('department_page/',views.deptPage,name="dept-page"),
   path('account/',views.accountSettings,name="account"),
   path('account_pen/',views.accountSettingsPendingStd,name="account_pen"),

   path('department/<str:pk>/',views.department,name="department"),
   path('studentinfo/<str:pk>/',views.studentinfo,name="studentinfo"),
   
   path('navstu/',views.nav_stu,name="nav_stu"),
   path('navdept/',views.nav_dept,name="nav_dept"),


   path('create_dept/',views.create_dept,name="create_dept"),
   path('update_dept/<str:pk>/',views.update_dept,name="update_dept"),
   path('delete_dept/<str:pk>/',views.delete_dept,name="delete_dept"),

   path('create_std/',views.create_std,name="create_std"),
   path('update_std/<str:pk>/',views.update_std,name="update_std"),
   path('delete_std/<str:pk>/',views.delete_std,name="delete_std"),
   path('accept-student/<int:student_id>/', views.accept_student, name='accept_std'),

   path('register_dpt/',views.register_dpt,name="register_dpt"),
   path('acc_set_dept_pen/',views.acc_set_dept_pen,name="acc_set_dept_pen"),

   path('create_teacher/',views.create_teacher,name="create_teacher"),
   path('teacher_list/',views.teacher_list,name="teacher_list"),
   path('teacher_info/<str:pk>/',views.teacher_info,name="teacher_info"),
   path('delete_teacher/<str:pk>/',views.delete_teacher,name="delete_teacher"),
   
   path('result_details/<str:pk>/',views.result_details,name="result_details"),
   path('update_result/<str:pk>/',views.update_student_result,name="update_student_result"),



   path('admin_send_notice/',views.admin_send_notice,name="admin_send_notice"),
   path('admin_notice_list/',views.admin_notice_list,name="admin_notice_list"),

]