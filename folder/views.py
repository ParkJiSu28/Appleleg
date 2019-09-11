from rest_framework.viewsets import ModelViewSet
from .models import Quiz, Wrongnote, Management
from .serializers import QuizSerializer, WrongnoteSerializer, ManagementSerializer
from rest_framework.filters import SearchFilter


class ManagementViewSet(ModelViewSet):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer


class ManagementSearchViewSet(ModelViewSet):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer




class QuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        qs = Quiz.objects.all()
        folder_qs = self.request.query_params.get('Management_id', None)
        if folder_qs is not None:
            folder = qs.filter(Management_id=folder_qs)
            return folder


class QuizSelectViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

    def get_queryset(self):
        qs = Quiz.objects.all()
        quiz_list = self.request.query_params.getlist('quiz_id', None)
        result = Quiz.objects.none()
        if quiz_list is not None:
            length = len(quiz_list)
            if length == 1:
                return qs.filter(quiz_id=quiz_list.pop())
            else:
                for x in range(0, length):
                    qs_ = qs.filter(quiz_id=quiz_list.pop())
                    result = result | qs_
                return result


class WrongnoteViewSet(ModelViewSet):
    queryset = Wrongnote.objects.all()
    serializer_class = WrongnoteSerializer
