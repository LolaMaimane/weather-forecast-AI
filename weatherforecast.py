import requests # type: ignore

class SWIISDrone:
    def __init__(self, starting_point):
        self.location = starting_point

class FarmLocation:
    def __init__(self, land_size, areas):
        self.land_size = land_size
        self.areas = areas

    def generate_swiis_drone_path(self, drone):
        path = []
        for area in self.areas:
            path.append((drone.location, area))
            drone.location = area
        return path

    def get_weather_forecast(self, lat, lon):
        api_key = "YOUR_OPENWEATHERMAP_API_KEY"
        url = f"http://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}"
        response = requests.get(url)
        weather_data = response.json()
        return weather_data

def main():
    print("Welcome to the Farm SWIIS-Drone Path Generator!")
    print("Please enter farm size (in meters):")

    while True:
        try:
            North = float(input("North: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            South = float(input("South: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            East = float(input("East: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        try:
            West = float(input("West: "))
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    land_size = {'North': North, 'South': South, 'East': East, 'West': West}

    print("Please enter the number of areas in the farm:")

    while True:
        try:
            num_areas = int(input())
            break
        except ValueError:
            print("Invalid input. Please enter a whole number.")

    areas = []
    for i in range(num_areas):
        print(f"Enter the coordinates (x,y) for area {i + 1}:")
        while True:
            try:
                x = float(input("x: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        while True:
            try:
                y = float(input("y: "))
                break
            except ValueError:
                print("Invalid input. Please enter a number.")

        areas.append((x, y))

    # Create objects of farm and SWIIS-Drone
    farm = FarmLocation(land_size, areas)
    drone = SWIISDrone((0, 0))

    # Get weather forecast data
    lat, lon = farm.land_size['North'], farm.land_size['East']
    weather_data = farm.get_weather_forecast(lat, lon)

    # Generate the SWIIS-Drone path
    path = farm.generate_swiis_drone_path(drone)

    print("Drone path:")
    for i, point in enumerate(path):
        print(f"Point {i + 1}:{point}")

    # Print weather forecast information
    print("\nWeather Forecast:")
    for forecast in weather_data['list']:
        print(f"Time: {forecast['dt_txt']}")
        print(f"Temperature: {forecast['main']['temp'] - 273.15:.2f}°C")
        print(f"Weather: {forecast['weather'][0]['description'].capitalize()}")
        print(f"Humidity: {forecast['main']['humidity']}%")
        print(f"Pressure: {forecast['main']['pressure']}hPa")
        print(f"Wind Speed: {forecast['wind']['speed']}m/s")
        print(f"Cloud Cover: {forecast['clouds']['all']}%")
        print("")

if __name__ == "__main__":
    main()
