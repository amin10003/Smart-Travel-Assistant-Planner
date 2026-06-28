from services.distance_services import DistanceService


service = DistanceService()

print(

    service.get_distance(

        "Nairobi",

        "Mombasa"
    )

)