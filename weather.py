import requests

def get_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(response.text)
        else:
            print("Could not fetch weather. Please try again.")
    except Exception as e:
        print("Error:", e)

def main():
    print("=== Weather App ===")
    city = input("Enter city name: ")
    get_weather(city)

if __name__ == "__main__":
    main()
