from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Article
from .serializers import ArticleListSerializer

# 템플릿이 없기에 render 불필요
# from django.shortcuts import render
# 4## : 클라이언트 에러 (예시) 404 : Not found
# 5## : 서버 에러 
from django.shortcuts import get_object_or_404, get_list_or_404
# object는 단일 객체 조회 vs list는 전체 객체 조회 

@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'GET':
        # 게시글이 없다 -> 404 에러 반환 
        articles = get_list_or_404(Article)
        # 직렬화
        # many=True : 여러개의 객체일 때
        serializer = ArticleListSerializer(articles, many=True)
        # .data -> json으로 반환 
        return Response(serializer.data)

