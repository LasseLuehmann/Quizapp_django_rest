from apps.session.models import Session
from apps.session.serializers.session import SessionSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer

@api_view(['GET'])
def listallsessions(request):
    
    session = Session.objects.all()

    data = SessionSerializer(data= session, many=True)
    data.is_valid()

    return Response(data.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def fetch_session(request, sessionid):

    sessionID = Session.objects.filter(session_id=sessionid)
    data = SessionSerializer(data=sessionID)
    data.is_valid()

    question_id = [id for id in data.data['session_questions']]
    score = 0
    for id in question_id:
        question = Question.objects.get(question_id = id)
        points = QuestionSerializer(data = question)
        points.is_valid()
        score += points.data['score']

    return Response(data.data, status=status.HTTP_200_OK)


