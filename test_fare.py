from services.fare_services import FareService


fare = FareService()

print(

    fare.estimate_fare(

        480,

        "Bus"
    )

)