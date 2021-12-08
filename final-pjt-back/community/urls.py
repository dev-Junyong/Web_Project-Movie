from django.urls import path

from . import views

app_name = 'community'
urlpatterns = [
    path('', views.review_index, name='review_index'),
    path('<int:movie_id>/create_review/', views.create_review, name='create_review'),
    path('<int:review_id>/', views.review_detail, name='review_detail'),
    path('<int:review_id>/update_review/', views.update_review, name='update_review'),
    
    path('<int:review_id>/like_review/', views.like_review, name='like_review'),
    
    path('<int:review_id>/comment/', views.create_comment, name='create_comment'),
    path('<int:review_id>/comment_load/', views.comment_detail, name='comment_detail'),
    path('<int:review_id>/comment/<int:comment_id>/update_comment/', views.update_comment, name='update_comment'),
    
    path('<int:review_id>/comment/<int:comment_id>/like_comment/', views.like_comment, name='like_comment'),
]