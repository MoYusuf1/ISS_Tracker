import requests
import datetime
# gets the present coordinates of the Space Station
iss_response = requests.get(url="http://api.open-notify.org/iss-now.json")
# if any error occurred it will tell us
iss_response.raise_for_status()

# stores the json data into a this variable
iss_data = iss_response.json()

# takes a wanted component from the data and stores it accordingly
iss_longitude = iss_data["iss_position"]["longitude"]
iss_latitude = iss_data["iss_position"]["latitude"]

# prints it out to the user
print(f"The International Space Station's Position - \n"
      f"Longitude: {iss_longitude}  "
      f"Latitude: {iss_latitude}")

parameters = {"lat": 44.931296, "long": -93.267662, "formatted": 0}

# gets the sunset and sunrise and stores it into this variable
sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# informs us in details which error occurred
sun_response.raise_for_status()

# stores the json data into into a variable
sun_data = sun_response.json()

# stores each information from the json data into each respective variable
sunrise = sun_data["results"]["sunrise"]
sunset = sun_data["results"]["sunset"]

time = datetime.datetime.now()

sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset_hour = sunset.split("T")[1].split(":")[0]

if int(sunset_hour) < int(time.hour) < int(sunrise_hour):
      print("It's not visible now")


