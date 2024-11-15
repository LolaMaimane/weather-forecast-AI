# weather-forecast-AI

# Farm SWIIS-Drone Path Generator

Welcome to the Farm SWIIS-Drone Path Generator! This project helps generate a path for a drone to follow across different areas of a farm and fetches weather forecast data for the farm's location.

## Features

- **Drone Path Generation**: Generates a path for the drone to follow based on user-defined areas within the farm.
- **Weather Forecast**: Fetches and displays weather forecast data for the farm's location using the OpenWeatherMap API.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/your-username/farm-swiis-drone-path-generator.git
    cd farm-swiis-drone-path-generator
    ```

2. Install the required dependencies:
    ```bash
    pip install requests
    ```

## Usage

1. Run the script:
    ```bash
    python main.py
    ```

2. Follow the prompts to enter the farm size and areas.

3. The script will generate the drone path and display the weather forecast.

## Configuration

- Replace `YOUR_OPENWEATHERMAP_API_KEY` in the `get_weather_forecast` method with your actual OpenWeatherMap API key.



