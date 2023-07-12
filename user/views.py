from django.http import JsonResponse, HttpResponse
from rest_framework import viewsets
from user.models import user
from user.serializers import userSerializer
from rest_framework.decorators import action
from django.contrib.auth.hashers import make_password
from django.contrib.auth import authenticate


class userViewSet(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userSerializer

    @action(detail=False, methods=['post'], url_path='register')
    def register(self, request):
        try:
            name = request.data.get('name')
            firstname = request.data.get('firstname')
            birthdate = request.data.get('birthdate')
            sexe = request.data.get('sexe')
            email = request.data.get('email')
            password = request.data.get('password')
            role = request.data.get('role')

            if len(password) < 8:
                raise ValueError('Password must be at least 8 characters')

            serializer = userSerializer(data={'email': email, 'name': name, 'role': role, 'birthdate': birthdate, 'sexe': sexe, 'firstname': firstname, 'password': make_password(password)})
            
            if serializer.is_valid():
                serializer.save()
                user_data = serializer.data
                del user_data['password']
                data = {
                    "status": True,
                    "data": user_data
                }
                return JsonResponse(data, status=201)
            
            data = {
                "status": False,
                "error": serializer.errors
            }
            return JsonResponse(data, status=400)

        except Exception as e:
            data = {
                "status": False,
                "error": str(e)
            }
            return JsonResponse(data, status=400)

    @action(detail=False, methods=['post'], url_path='login')
    def login(self, request):
        try:
            email = request.data.get('email')
            password = request.data.get('password')

            user = authenticate(request, email=email, password=password)

            if user is not None:
                data = {
                    "status": True,
                    "message": "Bienvenue"
                }
                return JsonResponse(data, status=200)
            else:
                error_message = "Email ou mot de passe incorrect."
                return JsonResponse({'status': False, 'error': error_message}, status=400)

        except Exception as e:
            data = {
                "status": False,
                "error": str(e)
            }
            return JsonResponse(data, status=400)
