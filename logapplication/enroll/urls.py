from django.urls import path
from . import views
urlpatterns=[
    path('',views.HomeView.as_view(),name="homepage"),
    path('about/',views.AboutView.as_view(),name="aboutpage"),
    path('datatables/',views.DataTableView.as_view(),name="datatables"),
    path('signup/',views.SignUpView.as_view(),name="signuppage"),
    path('profile/',views.ProfileView.as_view(),name="profilepage"),
    path('logout/',views.UserLogOutView.as_view(),name="logoutuser"),
    path('delete/<int:id>',views.DeleteTask.as_view(),name="deletetask"),
    path('login/',views.user_login,name="loginpage"),
    path('changepass/',views.changepass,name="changepass"),
    path('update/<int:id>',views.update_task,name="updatetask"),
]
