# Dynamic Weather-Based Wallpaper Changer 🌦️🌞❄️

## Overview
Welcome to the Dynamic Weather-Based Wallpaper Changer! This Python application automatically updates your desktop wallpaper based on the current weather conditions in your location. Whether it's sunny, rainy, snowy, or cloudy, this app fetches beautiful, high-quality images from Unsplash to match the weather and update your wallpaper in real-time. 🌦️🌞❄️

## Key Features
- **Real-time Weather Updates:** Fetches real-time weather data using the OpenWeather API.
- **Stunning Wallpapers:** Sources high-quality images from Unsplash that match the current weather conditions.
- **Seamless Integration:** Automatically updates your desktop background without any manual intervention.

## Technologies Used
- **Python:** The backbone of the application.
- **OpenWeather API:** For real-time weather data.
- **Unsplash API:** For fetching beautiful wallpapers.

## Installation

### Prerequisites
- Python 3.x
- Pip (Python package installer)

### Steps
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/weather-wallpaper-changer.git
    cd weather-wallpaper-changer
    ```

2. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Get your API keys:
    - Sign up for an API key at [OpenWeather](https://openweathermap.org/api).
    - Sign up for an API key at [Unsplash](https://unsplash.com/developers).

4. Create a `.env` file in the root directory and add your API keys:
    ```env
    OPENWEATHER_API_KEY=your_openweather_api_key
    UNSPLASH_API_KEY=your_unsplash_api_key
    ```

## Usage
To run the application, simply execute:
```bash
python main.py
