from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),

    # API routes
    path("contact", views.contact, name="contact"),
    path("account", views.account, name="account"),
    path("questions", views.questions, name="questions"),
    path("quiz", views.quiz, name="quiz"),
    path("del_edit/<int:account_id>", views.del_edit, name="del_edit")
]