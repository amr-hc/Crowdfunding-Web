from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.viewsets import ModelViewSet

# Project Pics Model
from Project_Pics.models import ProjectPics

# Serializer
from Project_Pics.api.serializer import ProjectPicsSerializer

# Permissions
from rest_framework.permissions import AllowAny
from rest_framework.authentication import TokenAuthentication

class ProjectPicsViewSet(ModelViewSet):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    queryset = ProjectPics.objects.all()
    serializer_class = ProjectPicsSerializer

    @action(detail=False, methods=['get'])
    def get_pics_of_project(self, request):
        project_id = request.query_params.get('project_id', None)
        if project_id is None:
            return Response({"error": "project_id parameter is required"}, status=400)

        try:
            pics = ProjectPics.objects.filter(project_id=project_id)
            serializer = self.get_serializer(pics, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=500)
