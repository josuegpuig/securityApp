from .models import Evaluation
from .serializers import EvaluationSerializer
from rest_framework import generics, permissions
from .permissions import IsOwnerOrReadOnly
from textblob import TextBlob


class EvaluationList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer

    def perform_create(self, serializer):
        analysis = TextBlob(self.request.data['opinion'])
        analysis  = analysis.translate(to='en')
        sentiment = ''
        # set sentiment 
        if analysis.sentiment.polarity > 0: 
            sentiment = 'positive'
        elif analysis.sentiment.polarity == 0: 
            sentiment = 'neutral'
        else: 
            sentiment = 'negative'

        serializer.save(user=self.request.user, sentiment=sentiment)


class EvaluationDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializer