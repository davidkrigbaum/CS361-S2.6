import requests

BASE_URL = 'https://valid-url.adaptable.app/'

def test_flask_app():
    try:
        response = requests.get(BASE_URL)
        if response.status_code == 200:
            data = response.json()
            if 'url' in data:
                print("First result URL:", data['url'])
            elif 'error' in data:
                print("Error:", data['error'])
            else:
                print("Unexpected response format")
        else:
            print("Failed to fetch URL. Status code:", response.status_code)
    except requests.RequestException as e:
        print("Request failed:", e)

if __name__ == '__main__':
    test_flask_app()