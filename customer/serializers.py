from rest_framework import serializers

from customer.models import Customer


class CustomerSerializer(serializers.ModelSerializer):
    full_name = serializers.CharField(write_only=True)
    full_phone_number = serializers.CharField(write_only=True)

    class Meta:
        model = Customer
        fields = '__all__'
        extra_kwargs = {
            'first_name': {'read_only': True},
            'middle_name': {'read_only': True},
            'surname': {'read_only': True},
            'date_of_birth': {'write_only': True},
            'country_code': {'read_only': True},
            'phone_number': {'read_only': True}
        }

    def create(self, validated_data):
        splits = validated_data['full_name'].split(' ')

        middle_name = None
        surname = None

        if len(splits) == 1:
            first_name = splits[0]
        elif len(splits) == 2:
            first_name = splits[0]
            surname = splits[1]
        else:
            first_name = splits[0]
            middle_name = splits[1]
            surname = splits[2]

        splits = validated_data['full_phone_number'].split(' ')

        country_code = splits[0]
        phone_number = validated_data['full_phone_number'].replace(country_code, '').strip()

        customer = Customer.objects.create(
            first_name=first_name,
            middle_name=middle_name,
            surname=surname,
            date_of_birth=validated_data['date_of_birth'],
            country_code=country_code,
            phone_number=phone_number
        )

        return customer
