from rest_framework.response import Response
from rest_framework.views import APIView
from .tasks import add, time_task

class AddView(APIView):
    def get(self, request, *args, **kwargs):
        result = add.apply_async([4, 6])
        result1 = time_task.apply_async()
        return Response({
            "add_task_id": result.id,
            "time_task_id": result1.id
        })
