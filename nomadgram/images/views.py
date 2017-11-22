#from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from . import models, serializers

class Feed(APIView):
    
    def get(self, request, format=None):
        
        # 팔로잉을 하면 팔로잉 한사람의 최신 글들이 보인다. 
        # 그래서 일단 팔로잉 리스트를 불러온다.
        # 
        user = request.user
        
        following_users = user.following.all()

        image_list = []

        for following_user in following_users:

            user_images = following_user.images.all()[:2] # [:2] 두개만 필터링

            for image in user_images:
                
                image_list.append(image)

        sorted_list = sorted(
            image_list, key=lambda image: image.created_at, reverse=True)

        serializer = serializers.ImageSerializer(sorted_list, many=True)


        return Response(serializer.data)


#def get_key(image):
#    
#    return image.created_at


