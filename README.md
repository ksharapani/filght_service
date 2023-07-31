### Q1

    GET

    http://localhost:8000/transport/bookings?date=2023-07-30&start_location=1&end_location=2


    GET

    http://localhost:8000/transport/history?start_date=2023-07-30&end_date=2023-07-30

    GET 

    http://localhost:8000/transport/vip?date=2023-07-31&start_location=1&end_location=2&weight=10&capacity=20


### Q2

    POST

    http://localhost:8000/customer/customer
    {
        "full_name": "A B C",
        "full_phone_number": "+1 (202) 224-3121",
        "date_of_birth": "2023-06-01"
    }


    Assumptions

    phone number will be provide only in this format "+1 (202) 224-3121"

    Maximum 3 names can capture    
    if user provide 1 name it consider as first name
    if user provide 2 names it consider as frist and surnmae
    if user provide 3 names it consider as frist, middle and surname
    if user provide more than 3 names only 1st 3 names will capture

