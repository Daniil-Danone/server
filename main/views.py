from rest_framework import views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from main.models import Marks, Event, User
from main.serializers import MarksSerializer, EventsSerializer, UserSerializer


class UserAPIView(views.APIView):
    permission_classes = [AllowAny]

    #  Получение объекта пользователя или массива объектов пользователей
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        #  Получение всех пользователей
        if not pk:
            return Response(UserSerializer(User.objects.all(), many=True).data)

        #  Получение определённого пользователя по его ID
        try:
            return Response(UserSerializer(User.objects.get(id=self.kwargs["pk"])).data)

        except:
            return Response({"ERROR": f"Пользователя с ID: {self.kwargs['pk']} не существует"})


class MarksAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response(MarksSerializer(Marks.objects.all(), many=True).data)

        try:
            return Response(MarksSerializer(Marks.objects.filter(id=pk), many=True).data)

        except:
            return Response(f"Не существует маркера с ID: {pk}")

    def post(self, request):
        serializer = MarksSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response(f"Не указан ID записи")

        try:
            instance = Marks.objects.get(pk=pk)

        except:
            return Response(f"Записи с ID: {pk} не существует")

        serializer = MarksSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(f"Запись (ID: {pk}) успешно обновлена")

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response("Не указан ID записи")

        try:
            Marks.objects.filter(pk=pk).delete()
        except:
            return Response(f"Записи с ID: {pk} не существует")

        return Response(f'Запись {pk} успешно удалена')


class EventsAPIView(views.APIView):
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response(EventsSerializer(Event.objects.all(), many=True).data)

        try:
            return Response(EventsSerializer(Event.objects.filter(id=pk), many=True).data)

        except:
            return Response(f"Не существует маркера с ID: {pk}")

    def post(self, request):
        print(request)
        serializer = EventsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def put(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)

        if not pk:
            return Response(f"Не указан ID записи")

        try:
            instance = Event.objects.get(pk=pk)

        except:
            return Response(f"Записи с ID: {pk} не существует")

        serializer = EventsSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(f"Запись (ID: {pk}) успешно обновлена")

    def delete(self, request, *args, **kwargs):
        pk = kwargs.get("pk", None)
        if not pk:
            return Response("Не указан ID записи")

        try:
            Event.objects.filter(pk=pk).delete()
        except:
            return Response(f"Записи с ID: {pk} не существует")

        return Response(f'Запись {pk} успешно удалена')
