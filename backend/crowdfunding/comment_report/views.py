from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from api.permissions import IsAdminOrpost, IsOwnerOrAdmin
from comment_report.models import Report_comment
from api.modelserializers import ReportCommentSerializer



class ReportListCreateAPIView(ListCreateAPIView):
    permission_classes = [IsAdminOrpost]
    queryset = Report_comment.objects.all()
    serializer_class = ReportCommentSerializer


class ReportRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    permission_classes = [IsOwnerOrAdmin]
    queryset = Report_comment.objects.all()
    serializer_class = ReportCommentSerializer
    lookup_url_kwarg = 'id'