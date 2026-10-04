from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response

@api_view(['GET'])
def hello_world(request):
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    return Response({
        "title": "Hello World",
        "task": "#PBW3B1PBL101",
        "student": "251080200135 Adrian Syahputra",
        "framework": "Framework Pilihan -> Python [11] - Django REST",
        "time": f"TIME: [{current_time}]"
    })