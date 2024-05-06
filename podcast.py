import json
import requests


def download_data(url, token):
    headers = {"Authorization": f"Token {token}"}
    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to download data. Status code: {response.status_code} -- url failed: {url}")
        return None


def save_to_json(data, filename):
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def read_json_array(filename):
    with open(filename, 'r') as f:
        json_array = json.load(f)
    return json_array


class Country:
    def __init__(self, stationcount, name, iso_3166_1):
        self.stationcount = stationcount
        self.name = name
        self.iso_3166_1 = iso_3166_1

    def __repr__(self):
        return f"Country(name={self.name}, isoCode={self.iso_3166_1.lower()})"


if __name__ == "__main__":

    fileName = "countries.json"
    json_array = read_json(fileName)

    # Convert JSON array to list of Person objects
    countries = [Country(item["stationcount"], item["name"], item["iso_3166_1"]) for item in json_array]

    token = "N1BefE9e6GYBRGBqwg8zXBRen1yjtwmt4qw0mdKO"
    for country in countries:
        countryCode = country.iso_3166_1.lower()
        url = f"https://api2.mytuner.mobi/api/v2/ituner/podcasts/tops?country_code={countryCode}"
        downloaded_data = download_data(url, token)
        if downloaded_data:
            # Save data to a JSON file
            save_to_json(downloaded_data, f"data/{countryCode}.json")
            print(f"Data {countryCode}.json downloaded successfully.")