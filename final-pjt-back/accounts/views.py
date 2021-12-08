from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from rest_framework.permissions import AllowAny
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from community.serializers import ReviewSerializer
from community.models import Review
from .serializers import UserSerializer, SignupSerializer, UpdateUserSerializer, PasswordChangeSerializer
from movies.serializers import GenreSerializer
User = get_user_model()


@api_view(['POST'])
def signup(request):
    serializer = SignupSerializer(data=request.POST)

    if len(request.POST['password']) < 8:
        return Response({'error' : '비밀번호가 너무 짧습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        user.set_password(user.password)
        user.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT'])
@permission_classes([AllowAny])
def password_chg(request, username):
    user = get_object_or_404(User, username=username)

    if user.email != request.PUT['email']:
        return Response({'error': '이메일이 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    if len(request.PUT['password']) < 8:
        return Response({'error': '비밀번호가 너무 짧습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    serializer = PasswordChangeSerializer(user, data=request.data)
    if serializer.is_valid(raise_exception=True):
        person = serializer.save()
        person.set_password(person.password)
        person.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def profile(request, username):
    person = get_object_or_404(User, username=username)
    serializer = UserSerializer(person)
    return Response(serializer.data)


@api_view(['GET'])
def login_user(request):
    user = request.user
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
def user_reviews(request, username):
    user = get_object_or_404(User, username=username)
    reviews = user.review_author.all()
    serializer = ReviewSerializer(reviews, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_followings(request, username):
    person = get_object_or_404(User, username=username)
    followings = person.following
    serializer = UserSerializer(followings, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def user_followers(request, username):
    person = get_object_or_404(User, username=username)
    followers = person.followers
    serializer = UserSerializer(followers, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def follow(request, username):
    person = get_object_or_404(User, username=username)
    user = request.user
    if person != user:
        if person.followers.filter(pk=user.pk).exists():
            person.followers.remove(user)
            is_follow = False
        else:
            person.followers.add(user)
            is_follow = True

        data = {
            'is_follow': is_follow,
            'followers': person.followers.count(),
            'followings': person.following.count(),
        }
        return JsonResponse(data)
    return HttpResponse(status=200)


@api_view(['PUT'])
def profile_update(request, username):
    user = get_object_or_404(User, username=username)

    if user == request.user:
        serializer = UpdateUserSerializer(user, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(status=status.HTTP_403_FORBIDDEN)


@api_view(['POST'])
def profile_photo(request, username):
    src = request.FILES['image']
    user = get_object_or_404(User, username=username)
    serializer = UpdateUserSerializer(user, data=request.POST)

    if serializer.is_valid():
        serializer.save(profile_photo=src)
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def chart_data(request, username):
    user = get_object_or_404(User, username=username)
    movies = user.like_movies.all()
    reviews = user.review_author.all()

    cnt = [0] * 19
    name = [
        '모험', '판타지', '애니메이션', '드라마', 
        '공포', '액션', '코미디', '역사', '서부', 
        '스릴러', '범죄', '다큐멘터리', 'SF',
        '미스터리', '음악', '로맨스', '가족', '전쟁', 'TV 영화'
    ]

    for movie in movies:
        genres = GenreSerializer(movie.genres, many=True)
        
        for genre in genres.data:
            cnt[name.index(genre['name'])] += 1

    for r_movie in reviews:
        r_genres = r_movie.movie.genres.all()
        r_genres = GenreSerializer(r_genres, many=True)

        for r_genre in r_genres.data:
            cnt[name.index(r_genre['name'])] += 1

    return Response(cnt)