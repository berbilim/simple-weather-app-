from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

API_KEY = 'your_openweather_api_key'

@app.route('/weather', methods=['GET'])
def weather():# Assisted by watsonx Code Assistant 
from flask import Flask, request, jsonify
import requests

# Initialize the Flask application
app = Flask(__name__)

# Set your OpenWeatherMap API key
API_KEY = 'your_openweather_api_key'

# Define the route for the weather data endpoint
@app.route('/weather', methods=['GET'])
def weather():
    """
    This function handles GET requests to the '/weather' endpoint.
    It expects a 'city' parameter in the query string and returns the current weather data for that city.
    """
    # Get the city name from the query string
    city = request.args.get('city')

    # Check if the city parameter is provided
    if not city:
        return jsonify({'error': 'City parameter required'}), 400

    # Construct the API request URL
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric'

    # Send a GET request to the OpenWeatherMap API
    res = requests.get(url)

    # Check if the request was successful (status code 200)
    if res.status_code != 200:
        return jsonify({'error': 'Failed to retrieve data'}), res.status_code

    # Parse the JSON response from the API
    data = res.json()

    # Extract the relevant weather information
    weather = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }

    # Return the weather data as a JSON response
    return jsonify(weather)

# Run the Flask application if this script is executed directly
if __name__ == '__main__':
    app.run(debug=True)

    city = request.args.get('city')
    if not city:
        return jsonify({'error': 'City parameter required'}), 400
    url = f'<http://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric>'
    res = requests.get(url)
    if res.status_code != 200:
        return jsonify({'error': 'Failed to retrieve data'}), res.status_code
    data = res.json()
    weather = {
        'city': city,
        'temperature': data['main']['temp'],
        'description': data['weather'][0]['description']
    }
    return jsonify(weather)

if __name__ == '__main__':
    app.run(debug=True)
