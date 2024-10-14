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


class QuizMusic:
    def __init__(self, id, name, url, description, thumb):
        self.id = id
        self.name = name
        self.url = url
        self.description = description
        self.thumb = thumb

    def __repr__(self):
        return f"QuizMusic(id = {self.id}, name={self.name}, url={self.url}, description={self.description},thumb={self.thumb})"


def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
            print(f"download ok: {save_path}")
    else:
        print(f"down load failed: {url}")


if __name__ == "__main__":

    fileName = "quiz_music.json"
    url = "https://raw.githubusercontent.com/xsalazar/emoji-kitchen-backend/main/app/metadata.json"
    download_image(url,f"data/metadata.json")
    # json_array = read_json(fileName)
    #
    # # Convert JSON array to list of Person objects
    # quizMusics = [QuizMusic(item["id"], item["name"], item["url"], item["description"], item["thumb"]) for item in
    #               json_array]
    #
    # index = 0
    # for quiz in quizMusics:
    #     index = index + 1
    #     id = quiz.id
    #     name = quiz.name
    #     url = quiz.url
    #     description = quiz.description
    #     thumb = quiz.thumb
    #     try:
    #         download_image(url, f"data/quiz/music/audio/music_{index}.mp3")
    #         download_image(thumb, f"data/quiz/music/thumb/music_thumb_{index}.jpg")
    #     except Exception:
    #         print(f"download {videoUrl} error")
