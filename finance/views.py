from rest_framework import generics, viewsets
from finance.models import Account
from finance.serializers import AccountSerializer

# Create your views here.

class FinanceCreateListView(generics.ListCreateAPIView):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

class AccountViewSet(viewsets.ModelViewSet):
    queryset = Account.objects.all()
    serializer_class = AccountSerializer

    def get_queryset(self):
        # Filter accounts by the logged-in user
        return Account.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        # Automatically assign the logged-in user to the account
        serializer.save(user=self.request.user)
