import json
import os
from concurrent.futures import ThreadPoolExecutor

import requests


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

# Function to download multiple images with multithreading
def download_images(urls, names, save_dir):
    os.makedirs(save_dir, exist_ok=True)

    with ThreadPoolExecutor(max_workers=5) as executor:
        futures = []
        for i, url in enumerate(urls):
            save_path = os.path.join(save_dir, names[i])
            futures.append(executor.submit(download_image, url, save_path))

        # Wait for all futures to complete
        for future in futures:
            future.result()

# # Example list of image URLs
# image_urls = [
#     'https://example.com/image1.jpg',
#     'https://example.com/image2.jpg',
#     'https://example.com/image3.jpg',
#     # Add more URLs as needed
# ]
#
# # Directory to save downloaded images
# save_directory = 'downloaded_images'
#
# # Download images using multithreading
# download_images(image_urls, save_directory)

if __name__ == "__main__":
    # fileName = "emoji_merge_optimize.json"
    # json_array = read_json(fileName)
    #
    # # Convert JSON array to list
    # emojis = [Emoji(item["code"], item["url"]) for item in
    #           json_array]
    urls = []
    names = []

    urls.append("https://i.pinimg.com/originals/62/f6/0e/62f60eb00055ce5a3580bd91559f9f94.gif")
    names.append("Lofi_City.gif")

    urls.append("https://i.pinimg.com/originals/01/49/2d/01492d0c01b2a02b1591e73494ca9431.gif")
    names.append("Night_Wallpaper.gif")

    urls.append("https://i.pinimg.com/originals/4a/21/f4/4a21f4a8fb33db4fb4ca48df2a7fe333.gif")
    names.append("Lofi_City_2.gif")

    urls.append("https://i.pinimg.com/originals/bd/5f/c9/bd5fc94d79ee57853f06914ce27dd5b1.gif")
    names.append("Star_Wallpaper.gif")

    urls.append("https://i.pinimg.com/originals/7a/6e/9f/7a6e9f827f009db075bea9d6d3fbf2ca.gif")
    names.append("Pink_City_Lofi.gif")

    urls.append("https://i.pinimg.com/originals/be/83/99/be8399dea45fe029701391e017e0c72f.gif")
    names.append("Distant_City.gif")

    urls.append("https://i.pinimg.com/originals/08/ce/99/08ce99af0105df29a1981b7174e8d2fc.gif")
    names.append("Sky_Wallpaper.gif")

    urls.append("https://i.pinimg.com/originals/1f/82/ac/1f82ac98c7f93847cd8c0418bb67a500.gif")
    names.append("Sea_Wallpaper.gif")

    urls.append("https://i.pinimg.com/originals/8d/a3/a1/8da3a1d04e2d412ced79684a3e0bcd5f.gif")
    names.append("Bonfire_Wallpaper.gif")

    urls.append("https://i.pinimg.com/originals/d2/ac/82/d2ac82e47b68bf7e6d5635e063bb3a40.gif")
    names.append("Cat_On_Window.gif")

    urls.append("https://i.pinimg.com/originals/0f/c8/e9/0fc8e994023e22a3c1e74e0d18105548.gif")
    names.append("Lofi_Wallpaper.gif")

    urls.append("https://i.pinimg.com/originals/de/db/50/dedb50bf6afae010d08b83c3163b746e.gif")
    names.append("Anime_Wallpaper.gif")

    urls.append("https://i.pinimg.com/originals/7d/46/ea/7d46eaa76cddd5fd801661245d3ef1e8.gif")
    names.append("Anime_City.gif")

    urls.append("https://i.pinimg.com/originals/36/1d/5c/361d5cb71a00267045aa9d5acb747f44.gif")
    names.append("Anime_Wallpaper_2.gif")
    #
    # for emoji in emojis:
    #     urls.append(emoji.url)
    #     names.append(emoji.code)

    download_images(urls, names,f"data/transparent")
