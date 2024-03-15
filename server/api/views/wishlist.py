from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import WishlistModel, UserModel
from ..serializers import WishlistSerializer
from rest_framework.permissions import IsAuthenticated


# CREATE WISHLIST
@permission_classes([IsAuthenticated])
@api_view(['GET','POST'])
def wishlist_create_and_list(request, username):
    try:
        current_user = UserModel.objects.get(username=username)
    except UserModel.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if (request.method == 'POST'):
        print("In wishlist post")
        request.data['user'] = current_user.id

        # Serialize data
        serializer = WishlistSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        wishlists = WishlistModel.objects.filter(user=request.user.id)
        serializer = WishlistSerializer(wishlists, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

@permission_classes([IsAuthenticated])
@api_view(['GET'])
def get_all_wishlists(request):
    wishlists = WishlistModel.objects.all()
    serializer = WishlistSerializer(wishlists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# WISHLIST VIEWS
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PATCH', 'DELETE'])
def wishlist_details(request, username):
    # If request gives username, can also filter wishlists of the respective user
    # in the response <NOT DONE>
    try:
        current_user = UserModel.objects.get(username=username)
    except UserModel.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if request.method == "GET":
        try: 
            wishlist = WishlistModel.objects.get(user=request.user.id)
        except WishlistModel.DoesNotExist:
            wishlist = { 'user': current_user.id, 'venues': [], 'events': [] }
            return Response({"Wishlist": wishlist}, status=status.HTTP_200_OK)
        
        serializer = WishlistSerializer(wishlist, many=False)
        return Response(serializer.data)
    
    # delete from & add to wishlist
    elif request.method == "PATCH":
        request.data['user'] = current_user.id
        try: 
            wishlist = WishlistModel.objects.get(user=request.user.id)
        except WishlistModel.DoesNotExist:
            serializer = WishlistSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                wishlist = WishlistModel.objects.get(user=request.user.id)
            else: return Response(serializer.errors, status=status.HTTP_403_FORBIDDEN)
        
        serializer = WishlistSerializer(wishlist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Wishlist updated", 
                             "updated_wishlist": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)
    
    elif request.method == "DELETE":
        try: 
            wishlist = WishlistModel.objects.get(user=request.user.id)
        except WishlistModel.DoesNotExist:
            return Response({"error": "Wishlist not found"}, status=status.HTTP_404_NOT_FOUND)
        
        wishlist.delete()
        serializer = WishlistSerializer(wishlist)
        return Response({"message": "Wishlist deleted", 
                             "deleted_wishlist": serializer.data}, status=status.HTTP_204_NO_CONTENT)

#
#
# MYWISHLIST PAGE <NOT SURE IF THIS IS NEEDED)
#
# Logged in users(not organiser) can view their wishlisted venues and events
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def mywishlist_page(request):
    # Get associated user
    try:
        current_user = UserModel.objects.get(username=request.data['username'])
    except UserModel.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)
    
    # Retrieve events booked by the user
    wishlists = WishlistModel.object.filter(user=request.user.id)
    serializer = WishlistSerializer(wishlists, many=True)

    return Response(serializer.data, status=status.HTTP_200_OK)
