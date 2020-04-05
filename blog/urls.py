from django.urls import path, include
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView, UserPostListView
from . import views

# checks for these patterns in urls
urlpatterns = [
    path('', PostListView.as_view(), name = 'blog-home'),
    path('about/', views.about, name = 'blog-about'),
    path('post/<int:pk>/', PostDetailView.as_view(), name = 'post-detail'), # pk - primary key, use this when you want to have a variable in path
    path('post/new/', PostCreateView.as_view(), name = 'post-create'), 
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name = 'post-update'),  # Update and create will share the same template
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name = 'post-delete'),  # Template = post_confirm_delete.html
    path('user/<str:username>/', UserPostListView.as_view(), name = 'user-posts'),   # Username is a variable hence<>
]