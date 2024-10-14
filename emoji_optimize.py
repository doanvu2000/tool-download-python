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


class Emoji:
    def __init__(self, code, url):
        self.code = code
        self.url = url

    def __repr__(self):
        return f"Emoji(code={self.code}, url={self.url})"


def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
            print(f"download ok: {save_path}")
    else:
        print(f"down load failed: {url}")


if __name__ == "__main__":
    fileName = "emoji_optimize.json"
    json_array = read_json(fileName)

    # Convert JSON array to list
    emojis = [Emoji(item["code"], item["url"]) for item in
              json_array]

    for emoji in emojis:
        name = f'u{emoji.code}.svg'
        try:
            download_image(emoji.url, f"data/emoji/root/{name}")
        except Exception:
            print(f"download {emoji.url} error")
