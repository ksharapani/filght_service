from django.db.models import Sum, Count, Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from transport.models import Booking


class BookingView(APIView):

    def get(self, request, format=None):
        date = request.query_params.get('date', None)
        start_location = request.query_params.get('start_location', None)
        end_location = request.query_params.get('end_location', None)

        query = Booking.objects.filter(date=date, start_location_id=start_location, end_location_id=end_location).\
            aggregate(confirm_total=Count('pk', filter=Q(status=True)),
                      unconfirm_total=Count('pk', filter=Q(status=False)),
                      weight_sum=Sum('weight', filter=Q(status=True)),
                      capacity_sum=Sum('capacity', filter=Q(status=True)))

        return Response({
            "confirm_total": query['confirm_total'],
            "unconfirm_total": query['unconfirm_total'],
            "weight": query['weight_sum'],
            "capacity": query['capacity_sum']
        }, status=status.HTTP_200_OK)


class BookingHistoryView(APIView):

    def get(self, request, format=None):
        start_date = request.query_params.get('start_date', None)
        end_date = request.query_params.get('end_date', None)

        query = Booking.objects.filter(date__gte=start_date, date__lte=end_date). \
            values('start_location__name', 'end_location__name').order_by('start_location'). \
            annotate(weight_sum=Sum('weight'), capacity_sum=Sum('capacity'))

        data = []
        for q in query:
            data.append({
                'start_location': q['start_location__name'], 'end_location': q['end_location__name'],
                'weight': q['weight_sum'], 'capacity': q['capacity_sum']
            })

        return Response(data, status=status.HTTP_200_OK)


class VipView(APIView):

    def get(self, request, format=None):
        date = request.query_params.get('date', None)
        start_location = request.query_params.get('start_location', None)
        end_location = request.query_params.get('end_location', None)
        weight = float(request.query_params.get('weight', None))
        capacity = float(request.query_params.get('capacity', None))

        query = Booking.objects.filter(date=date, start_location_id=start_location, end_location_id=end_location).\
            order_by('-created_at')

        remove_list = []
        for q in query:
            if q.status:
                if q.weight <= weight and q.capacity <= capacity:
                    remove_list.append(q)
                    weight -= q.weight
                    capacity -= q.capacity

        return Response({"remove_count": len(remove_list)}, status=status.HTTP_200_OK)
