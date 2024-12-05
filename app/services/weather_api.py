from app.config import API_KEY, BASE_URL
import requests

def fetch_weather(city: str):
    """
    Fetch the weather for a specific city.
    """
    params = {"q": city, "appid": API_KEY, "units": "metric"}

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        
        res = response.json()
        
        if "city" in res and "list" in res and len(res["list"]) > 0:
            city_name = res["city"]["name"]
            temperature = res["list"][0]["main"]["temp"]
            return {"city": city_name, "temperature": temperature}
        else:
            return {"error": "Unexpected response format"}
    except requests.exceptions.HTTPError as http_err:
        if response.status_code == 404:
            return {"error": "City not found"}
        else:
            return {"error": f"HTTP error occurred: {http_err}"}
    except Exception as err:
        return {"error": f"An error occurred: {err}"}




