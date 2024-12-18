from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import add

class AddView(APIView):
    def get(self, request, *args, **kwargs):
        result = add.delay(4, 6)  
        return Response({"task_id": result.id})
