import json
import os
import threading

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


class Category:
    def __init__(self, preview, link):
        self.preview = preview
        self.link = link

    def __repr__(self):
        return f"Category(preview={self.preview}, link={self.link})"


class Link:
    def __init__(self, portrait, landscape):
        self.portrait = portrait
        self.landscape = landscape

    def __repr__(self):
        return f"Link(portrait={self.portrait}, landscape={self.landscape})"


def download_image(url, save_path):
    response = requests.get(url)
    if response.status_code == 200:
        with open(save_path, 'wb') as file:
            file.write(response.content)
            print(f"download ok: {save_path}")
    else:
        print(f"down load failed: {url}")


# Function to download multiple images with multithreading
def download_images(urls, save_dir, prefix):
    os.makedirs(save_dir, exist_ok=True)
    threads = []
    for i, url in enumerate(urls):
        save_path = os.path.join(save_dir, f"{prefix}_{i + 1}.jpg")
        thread = threading.Thread(target=download_image, args=(url, save_path))
        thread.start()
        threads.append(thread)

    # Wait for all threads to finish
    for thread in threads:
        thread.join()


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
    fileName = "wallpaper_tag.json"
    json_array = read_json(fileName)

    # Convert JSON array to list
    categories = [Category(item["preview"], item["links"]) for item in
                  json_array]

    previewUrls = []
    portraitUrls = []
    landscapeUrls = []

    index = 0
    for category in categories:
        index = index + 1
        temp_json = json.dumps(category.link)
        link_obj = json.loads(temp_json)
        portraitUrl = link_obj["portrait"]
        landscapeUrl = link_obj["landscape"]
        print(f"preview[{index}] = {category.preview}")
        print(f"portrait[{index}] = {portraitUrl}")
        print(f"landscape[{index}] = {landscapeUrl}")
        previewUrls.append(category.preview)
        portraitUrls.append(portraitUrl)
        landscapeUrls.append(landscapeUrl)
        previewName = f"preview_{index}.jpg"
        portraitName = f"portrait_{index}.jpg"
        landscapeName = f"landscape_{index}.jpg"

        # try:
        #     download_image(category.preview, f"data/wallpaper/preview/1/{previewName}")
        #     download_image(portraitUrl, f"data/wallpaper/portrait/1/{portraitName}")
        #     download_image(landscapeUrl, f"data/wallpaper/landscape/1/{landscapeName}")
        # except Exception:
        #     print(f"download {category.background} error")

    # download_images(previewUrls,f"data/wallpaper/preview/2","preview")
    # download_images(portraitUrls,f"data/wallpaper/portrait/2","portrait")
    download_images(landscapeUrls,f"data/wallpaper/landscape/2","landscape")
