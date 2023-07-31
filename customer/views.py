from django.db.models import Sum, Count, Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from customer.models import Customer


class CustomerView(APIView):

    def get(self, request, format=None):
        date = request.query_params.get('date', None)
        start_location = request.query_params.get('start_location', None)
        end_location = request.query_params.get('end_location', None)

        query = Customer.objects.filter(date=date, start_location_id=start_location, end_location_id=end_location).\
            aggregate(confirm_total=Count('pk', filter=Q(status=True)),
                      unconfirm_total=Count('pk', filter=Q(status=False)),
                      weight_sum=Sum('weight', filter=Q(status=True)),
                      capacity_sum=Sum('capacity', filter=Q(status=True)))

        return Response({}, status=status.HTTP_200_OK)

