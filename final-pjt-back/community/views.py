from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import ( get_object_or_404,
                               get_list_or_404 )
from django.contrib.auth import get_user_model
from django.db.models import Count

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.core.paginator import Paginator

from accounts.serializers import UserSerializer

from .models import Review, Comment
from .serializers import CommentSerializer, ReviewSerializer
from movies.models import Movie
User = get_user_model()


@api_view(['POST'])
def create_review(request, movie_id):
    movie = get_object_or_404(Movie, pk=movie_id)
    serializer = ReviewSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, author=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def update_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if request.method == 'PUT':
        serializer = ReviewSerializer(review, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(review=review, author=request.user)
            return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'DELETE':
        review.delete()
        data = {
            'msg': f'{review_id}번 글이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def review_index(request):
    users = User.objects.alias(review=Count('review_author')).filter(review__gte=4).order_by('-review')
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)



@api_view(['GET'])
def review_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    serializer = ReviewSerializer(review)

    return Response(serializer.data)



@api_view(['POST'])
def create_comment(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(author=request.user, review=review)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def comment_detail(request, review_id):
    review = get_object_or_404(Review, pk=review_id)
    comments = review.review_comments
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)


@api_view(['PUT', 'DELETE'])
def update_comment(request, review_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)

    if request.method == 'PUT':
        if comment.author == request.user:
            serializer = CommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(comment=comment, author=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            return Response(status=status.HTTP_403_FORBIDDEN)

    
    elif request.method == 'DELETE':
        if comment.author == request.user:
            comment.delete()
        data = {
            'msg': f'{comment_id}번 댓글이 삭제되었습니다.'
        }
        return Response(data, status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def like_review(request, review_id):
    review = get_object_or_404(Review, pk=review_id)

    if review.users_like.filter(pk=request.user.pk).exists():
        review.users_like.remove(request.user)
        is_like = False
    else:
        review.users_like.add(request.user)
        is_like = True

    context = {
        'is_like': is_like,
        'cnt_like': review.users_like.count()
    }
    return JsonResponse(context)


@api_view(['POST'])
def like_comment(request, review_id, comment_id):
    comment = get_object_or_404(Comment, pk=comment_id)
    
    if comment.like_users.filter(pk=request.user.pk).exists():
        comment.like_users.remove(request.user)
        is_like = False
    else:
        comment.like_users.add(request.user)
        is_like = True
    context = {
        'is_like': is_like,
        'cnt_like': comment.like_users.count()
    }
    return JsonResponse(context)
