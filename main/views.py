from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from main.models import Todo
from main.serializers import TodoSerializer


class TodoAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response(TodoSerializer(Todo.objects.all(), many=True).data)

        try:
            return Response(TodoSerializer(Todo.objects.filter(id=pk), many=True).data)

        except:
            return Response(f"Не существует записи с ID: {pk}")

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(f'Новая запись добавлена')

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response(f"Не указан ID записи")

        try:
            instance = Todo.objects.get(pk=pk)

        except:
            return Response(f"Записи с ID: {pk} не существует")

        serializer = TodoSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(f"Запись (ID: {pk}) успешно обновлена")

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response("Не указан ID записи")

        try:
            Todo.objects.filter(pk=pk).delete()
        except:
            return Response(f"Записи с ID: {pk} не существует")

        return Response(f'Запись {pk} успешно удалена')
