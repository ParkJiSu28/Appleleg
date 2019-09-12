from rest_framework.viewsets import ModelViewSet
from .models import Quiz, Wrongnote, Management
from .serializers import QuizSerializer, WrongnoteSerializer, ManagementSerializer, QuizDetailSerializer, \
    WrongnoteDetailSerializer
from rest_framework.filters import SearchFilter
from django_filters import rest_framework as filters


# Folder(폴더 생성 및 조회)
class ManagementViewSet(ModelViewSet):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer


class ManagementSearchViewSet(ModelViewSet):
    queryset = Management.objects.all()
    serializer_class = ManagementSerializer
    filter_backends = (filters.DjangoFilterBackend, SearchFilter)
    filter_fields = ['email']


# Quiz(문제 출제 및 풀기)

class OriginQuizViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer


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


class QuizDetailViewSet(ModelViewSet):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer

    def get_queryset(self):
        qs = Quiz.objects.all()
        quiz_qs = self.request.query_params.get('Management_id', None)
        if quiz_qs is not None:
            quiz_detail = qs.filter(Management_id=quiz_qs)
            return quiz_detail


# Wrongnote(오답 관리)
class WrongnoteViewSet(ModelViewSet):
    queryset = Wrongnote.objects.all()
    serializer_class = WrongnoteSerializer


class WrongnotDetailViewSet(ModelViewSet):
    queryset = Wrongnote.objects.all()
    serializer_class = WrongnoteDetailSerializer

    def get_queryset(self):
        qs = Wrongnote.objects.all()
        wrong_qs = self.request.query_params.get('Management_id', None)
        if wrong_qs is not None:
            wrong_detail = qs.filter(Management_id=wrong_qs)
            return wrong_detail