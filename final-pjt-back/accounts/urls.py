from django.urls import path

from rest_framework_simplejwt.views import ( TokenObtainPairView,
                                             TokenRefreshView,
                                            )

from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup),
    # JWT 토큰 발행 요청
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # JWT 토큰 만료시 재발행 요청
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<username>/profile/', views.profile),
    path('<username>/profile/update/', views.profile_update),
    path('<username>/profile/photo/', views.profile_photo),
    path('<username>/user_reviews/', views.user_reviews),
    path('login_user/', views.login_user),
    path('<username>/user_followings/', views.user_followings),
    path('<username>/user_followers/', views.user_followers),
    path('<username>/follow/', views.follow),
    # path('<username>/password_chg/', views.password_chg),

    path('<username>/chart_data/', views.chart_data),
]
