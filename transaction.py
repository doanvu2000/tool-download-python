import json
import os

import requests


def read_json(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    return data


def read_json_array(filename):
    with open(filename, 'r') as f:
        json_array = json.load(f)
    return json_array


class Transaction:
    def __init__(self, date, amount,notes,code):
        self.date = date
        self.amount = amount
        self.notes = notes
        self.code = code

    def __repr__(self):
        return f"Transaction(date={self.date}, amount={self.amount}, notes={self.amount}, code={self.code})"


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
    fileName = "transactions.json"
    json_array = read_json(fileName)

    # Convert JSON array to list
    transactions = [Transaction(item["date"], item["amount"], item["notes"],item["code"]) for item in
              json_array]
    total = 0

    for trans in transactions:
        total += trans.amount
    money = "{:,}".format(total)
    print(f"total = {money}")
