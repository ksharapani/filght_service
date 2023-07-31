from rest_framework.response import Response
from rest_framework import generics, serializers
from rest_framework.status import HTTP_400_BAD_REQUEST, HTTP_201_CREATED

from customer.serializers import CustomerSerializer


class CustomerView(generics.CreateAPIView):
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            try:
                serializer.save()
            except serializers.ValidationError as sv:
                return Response({"status": 0, "message": sv.detail[0], "data": None}, status=HTTP_400_BAD_REQUEST)
            except Exception as ex:
                return Response({"status": 0, "message": str(ex), "data": None}, status=HTTP_400_BAD_REQUEST)

            return Response({"status": 1, "message": "Customer created successfully", "data": serializer.data},
                            status=HTTP_201_CREATED)

        return Response({"status": 0, "message": serializer.errors, "data": None}, status=HTTP_400_BAD_REQUEST)
