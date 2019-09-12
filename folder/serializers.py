from .models import Quiz, Wrongnote, Management
from rest_framework.serializers import ModelSerializer
import sys

sys.path.append("..")
from user.serializers import UserSerializer


class QuizSerializer(ModelSerializer):
    UserKey = UserSerializer(read_only=True)

    class Meta:
        model = Quiz
        fields = '__all__'


class WrongnoteSerializer(ModelSerializer):
    UserKey = UserSerializer(read_only=True)

    class Meta:
        model = Wrongnote
        fields = '__all__'


class ManagementSerializer(ModelSerializer):
    UserKey = UserSerializer(read_only=True)

    class Meta:
        model = Management
        fields = '__all__'


class QuizDetailSerializer(ModelSerializer):

    class Meta:
        model = Quiz
        fields = ('quiz_id', 'title', 'Management_id')


class WrongnoteDetailSerializer(ModelSerializer):

    class Meta:
        model = Wrongnote
        fields = ('wrong_id', 'title', 'Management_id')