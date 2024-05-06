import json

import requests


def download_data(url):
    # headers = {"Authorization": f"Token {token}"}
    # response = requests.get(url, headers=headers)
    response = requests.get(url)
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


class Video:
    def __init__(self, videoId, thumbnail, videoUrl):
        self.videoId = videoId
        self.thumbnail = thumbnail
        self.videoUrl = videoUrl
    def __repr__(self):
        return f"Video(videoId={self.videoId}, thumbnail={self.thumbnail}, videoUrl=${self.videoUrl})"


def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
            print(f"download ok: {save_path}")
    else:
        print(f"down load failed: {url}")


if __name__ == "__main__":

    fileName = "videos.json"
    json_array = read_json(fileName)

    # Convert JSON array to list of Person objects
    videos = [Video(item["videoId"], item["thumbnail"], item["videoUrl"]) for item in json_array]

    for video in videos:
        id = video.videoId
        videoUrl = video.videoUrl
        thumbnailUrl = video.thumbnail
        videoName = f"videoUrl_{id}.m3u8"
        thumbnailName = f"thumbnail_{id}.jpg"
        try:
            download_image(videoUrl, f"data/download/video/{videoName}")
            download_image(thumbnailUrl,f"data/download/thumbnail/{thumbnailName}")
        except Exception:
            print(f"download {videoUrl} error")
