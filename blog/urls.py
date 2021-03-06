from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:blog_id>', views.detail, name = "detail"),
    path('new',views.new, name = "new"),
    path('creat',views.create, name = "create"),
    path('edit/<int:blog_id>', views.edit, name = "edit"),
    path('update/<int:blog_id>',views.update, name = "update"),
    path('delete/<int:blog_id>',views.delete, name = "delete"),
    path('commenting/<int:blog_id>',views.commenting, name = "commenting"),
    path('like/<int:blog_id>',views.like, name='like'),
    # path('edit_commenting/<int:comment_id>', views.edit_commenting, name = "edit_commenting"),
    # path('update_commenting/<int:comment_id>',views.update_commenting, name = "update_commenting"),
]