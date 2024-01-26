from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import EventPage, RaiseHand, RequestInstitute, InstituteDetails, EditProfile
from .serializer import DataSerializer, RaiseHandSerializer, RequestInstituteSerializer, InstituteDetailsSerializer, EditProfileSerializer

@api_view(['GET'])
def get_data(request):
    data = EventPage.objects.filter(user=request.user)
    serializer = DataSerializer(data, many=True)
    return Response(serializer.data)

@api_view(['POST'])
# @permission_classes([IsAuthenticated]) add this only of u are able to add memebers after clicking the buttons by taking the username 
def post_data(request):
    serializer = DataSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def raise_hand(request):
    serializer = RaiseHandSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def request_institute(request):
    serializer = RequestInstituteSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_institute_details(request):
    details = InstituteDetails.objects.filter(user=request.user)
    serializer = InstituteDetailsSerializer(details, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def post_institute_details(request):
    serializer = InstituteDetailsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save(user=request.user)
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_profile(request):
    profile = EditProfile.objects.get(user=request.user)
    serializer = EditProfileSerializer(profile)
    return Response(serializer.data)
