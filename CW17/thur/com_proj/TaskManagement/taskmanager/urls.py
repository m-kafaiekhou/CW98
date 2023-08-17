from django.urls import path
from .views import (
    HomePage,
    search_view,
    TaskListView,
    TaskDetailView,
    CategoryListView,
    category_task_view,
    category_create_view,
    task_create_view,
    task_cat_create_view,
    CategoryDetailView,
    category_update_view,
    TaskUpdateView,
    tag_detail_view,
    tag_update_view,
    tag_create_view,
    task_delete_view,
    category_delete_view,
    history_view,
)

urlpatterns = [
    path('', HomePage.as_view(), name="home"),
    path('search/', search_view, name="search"),
    path('tasks/', TaskListView.as_view(), name="task_list"),
    path('task/<int:pk>/', TaskDetailView.as_view(), name="task_detail"),
    path('categories/', CategoryListView.as_view(), name="categories"),
    path('categories/<str:cat>/', category_task_view, name="category_task"),
    path('category/create/', category_create_view, name='category_create'),
    path('task/create/', task_create_view, name='task_create'),
    path('task/create/<str:cat>/', task_cat_create_view, name="task_cat"),
    path('category/detail/<int:pk>/', CategoryDetailView.as_view(), name='category_detail'),
    path('category/update/<int:pk>/', category_update_view, name='category_update'),
    path('task/update/<int:pk>/', TaskUpdateView.as_view(), name='task_update'),
    path('tag/create/<int:taskpk>/', tag_create_view, name="tag_create"),
    path('tag/detail/<int:pk>/', tag_detail_view, name='tag_detail'),
    path('tag/update/<int:pk>/', tag_update_view, name='tag_update'),
    path('delete/task/<int:pk>/', task_delete_view, name='delete_task'),
    path('delete/categroy/<int:pk>/', category_delete_view, name='delete_category'),
    path('History/', history_view, name='Histories'),
]
