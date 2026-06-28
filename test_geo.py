from services.geocode_service import GeocodeService


geo = GeocodeService()

print(

    geo.get_coordinates(

        "Mogadishu"

    )

)