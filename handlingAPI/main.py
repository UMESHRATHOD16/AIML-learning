import requests

def fetch_randomUser():
    url = "https://api.freeapi.app/api/v1/public/randomusers/13"
    response = requests.get(url)
    data = response.json()

    if data["success"] and "data" in data :
        user_data = data["data"]
        username = user_data["login"]["username"]
        country = user_data["location"]["country"]
        return username, country
    else:
        raise Exception("Failed to fetch User Data")

def main():
    try:
        username,country = fetch_randomUser()
        print(f"Username : {username} and Country {country}")
    except Exception as e:
        print(str(e))

if __name__ == "__main__":
    main()
