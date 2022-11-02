import logging

from rest_framework import generics, status
from rest_framework.response import Response
from .models import ArticlesModel
from .serializers import ArticleSerializer

logger = logging.getLogger(__name__)

class ArticleListCreateAPIView(generics.ListCreateAPIView):
    '''
        Allowed methods: POST and LIST
        POST: Creates a new Articles
        LIST: Returns list of Articles
        
    '''
    queryset = ArticlesModel.objects.all()
    serializer_class = ArticleSerializer
    

    #? Create a new Article
    def post(self, request, *args, **kwargs):
        serializer = ArticleSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)
        try:
            serializer.save()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Article Created Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)

  
class ArticleUpdateRetriveDeleteAPIView(generics.GenericAPIView):
    '''
        Allowed methods: Patch
        GET: Article by ID
        PATCH: Update an Article 
        DELETE: Delete an Article
       
    '''
    queryset = ArticlesModel.objects.all()
    serializer_class = ArticleSerializer
    lookup_field = 'pk'

    #? get single Article
    def get(self, request, *args, **kwargs):
        article = self.get_object()
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    #? Update a Course
    def patch(self, request, *args, **kwargs):
        article = self.get_object()
        serializer = ArticleSerializer(article, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)

        try:
            serializer.save() 
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Article Updated Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)

    #? Delete an Article
    def delete(self, request, *args, **kwargs):
        article = self.get_object()
        try:
            article.delete()
        except Exception as ex:
            logger.error(str(ex))

            return Response({'detail': str(ex)},
                            status=status.HTTP_400_BAD_REQUEST)

        response = {'detail': 'Article Deleted Successfully'}
        logger.info(response)

        return Response(response, status=status.HTTP_201_CREATED)


