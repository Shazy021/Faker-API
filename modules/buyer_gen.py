from faker import Faker
import reverse_geocoder as rg


def fake_buyer() -> dict[str, str]:
    """
    Generate fake buyers data

    :return: Dictionary, containing following information about fake buyer.
    """
    fake = Faker()
    lon, lat = fake.longitude(), fake.latitude()
    geo_rev = rg.search((lat, lon), mode=1, verbose=False)[0]

    res_dict = {
        'longitude': lon,
        'latitude': lat,
        'place': geo_rev['name'],
        'region': geo_rev['admin1']
    }

    return res_dict
