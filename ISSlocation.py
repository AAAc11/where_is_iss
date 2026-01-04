import time
import requests
import folium
from geopy import Nominatim

url = "http://api.open-notify.org/iss-now.json"
file_name = "whereisiss.html"

def reading_coordinates(url_name):
    try:
        response = requests.get(url_name)
        data = response.json()

        longitude = data['iss_position']['longitude']
        latitude = data['iss_position']['latitude']
        print(f"Coordinates: {latitude}, {longitude}")
        return latitude, longitude

    except requests.exceptions.Timeout:
        print("No response. ")
    except Exception as e:
        print(f"Error: {e}")

def checking_country(lat, lon):
    try:
        geolocator = Nominatim(user_agent="learning_apis")
        coordinates = f"{lat}, {lon}"
        location = geolocator.reverse(coordinates, language='en')
        if location:
            address = location.raw['address']
            country = address.get('country')
            print(f"ISS is currently over {country}")
        else:
            print("ISS is probably over the Ocean")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("=" * 30)

def creating_map(lat, lon):
    m = folium.Map(location = (lat, lon), zoom_start = 4, tiles="cartodb positron")
    folium.Marker((lat, lon), popup="ISS",
                  icon=folium.Icon(color="red", icon="rocket", prefix="fa")).add_to(m)
    m.save(file_name)

    with open(file_name, "r") as file:
        html_content = file.read()

    refresh_tag = '<meta http-equiv="refresh" content="10">'
    html_content = html_content.replace('<head>', '<head>' + refresh_tag)

    with open(file_name, "w") as file:
        file.write(html_content)

def main_function():
    while True:
        try:
            latitude, longitude = reading_coordinates(url)
            checking_country(latitude, longitude)
            creating_map(latitude, longitude)
            time.sleep(10)
        except Exception as e:
            print(f"Error: {e}")

main_function()
