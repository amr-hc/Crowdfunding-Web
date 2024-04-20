from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet
from api.permissions import IsOwnerOrReadOnly, IsAdminOrpost, IsOwnerOrAdmin
from comment_report.models import Report_comment
from api.modelserializers import ReportCommentSerializer
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
# Create your views here.
class CommentReportModelViewSet(ModelViewSet):
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Report_comment.objects.all()
    serializer_class = ReportCommentSerializer



class ReportListCreateAPIView(ListCreateAPIView):
    # permission_classes = [IsAdminOrpost]
    queryset = Report_comment.objects.all()
    serializer_class = ReportCommentSerializer


class ReportRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsOwnerOrAdmin]
    queryset = Report_comment.objects.all()
    serializer_class = ReportCommentSerializer
    lookup_url_kwarg = 'id'