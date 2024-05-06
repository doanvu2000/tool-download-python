import json

import requests


def download_data(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Failed to download data. Status code: {response.status_code} -- url failed: {url}")
        return None


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def read_json_array(filename):
    with open(filename, 'r') as f:
        json_array = json.load(f)
    return json_array


class Audio:
    def __init__(self, title, urlSound):
        self.title = title
        self.urlSound = urlSound

    def __repr__(self):
        return f"Audio(title={self.title}, urlSound={self.urlSound})"


def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
            print(f"download ok: {save_path}")
    else:
        print(f"down load failed: {url}")


if __name__ == "__main__":
    fileName = "audio.json"
    json_array = read_json(fileName)

    # Convert JSON array to list
    audios = [Audio(item["title"], item["urlSound"]) for item in
              json_array]

    for audio in audios:
        name = f'{audio.title}.mp3'
        try:
            download_image(audio.urlSound, f"data/audio/{name}")
        except Exception:
            print(f"download {audio.urlSound} error")
