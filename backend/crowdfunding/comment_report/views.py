from rest_framework.viewsets import ModelViewSet
from api.permissions import IsOwnerOrReadOnly
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