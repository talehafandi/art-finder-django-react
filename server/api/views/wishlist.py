from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models import WishlistModel, UserModel
from ..serializers import WishlistSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions

# CREATE WISHLIST
@permission_classes([IsAuthenticated])
@api_view(['POST'])
def create_wishlist(request):
    # Get associated user
    try:
       current_user = UserModel.objects.get(username=request.data['username'])
    except UserModel.DoesNotExist:
        return Response({"error": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    request.data['user'] = current_user.id
    serializer = WishlistSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# WISHLIST VIEWS
@permission_classes([IsAuthenticated])
@api_view(['GET', 'PATCH', 'DELETE'])
def wishlist_details(request, pk):
    try:
        wishlist = WishlistModel.objects.get(id=pk)
    except WishlistModel.DoesNotExist:
        return Response({"error": "Wishlist not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = WishlistSerializer(wishlist, many=False)
        return Response(serializer.data)
    
    elif request.method == "PATCH":
        serializer = WishlistSerializer(wishlist, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Wishlist updated", 
                             "updated_wishlist": serializer.data}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == "DELETE":
        wishlist.delete()
        return Response({"message": "Wishlist deleted", 
                             "deleted_wishlist": serializer.data}, status=status.HTTP_204_NO_CONTENT)

# LIST ALL WISHLISTS
@permission_classes([IsAuthenticated])
@api_view(['GET'])
def list_wishlists(request):
    wishlists = WishlistModel.objects.all()
    serializer = WishlistSerializer(wishlists, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)
