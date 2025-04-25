from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import permissions
from company.models import Company, CompanyMember
from company.serializers import CompanySerializer, CompanyMemberSerializer


class CompanyViewSet(viewsets.ModelViewSet):
    serializer_class = CompanySerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Company.objects.filter(owner=self.request.user)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def retrieve(self, request, pk=None):
        queryset = Company.objects.all()
        company = get_object_or_404(queryset, pk=pk)
        serializer = CompanySerializer(company)
        data = serializer.data
        data['companymembers'] = company.company_members.values()
        return Response(data)


class CompanyMemberViewSet(viewsets.ModelViewSet):
    serializer_class = CompanyMemberSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        pk = self.kwargs['pk']
        return Company.objects.get(pk=pk).company_members

    def get_object(self):
        user = self.request.user
        queryset = CompanyMember.objects.all()
        company = get_object_or_404(queryset, user_id=user)
        return company
