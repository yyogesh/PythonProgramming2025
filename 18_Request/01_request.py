import os
import requests

# python -m pip install requests
# m for module and pip for package installer

base_url = "https://xyz.com/xyz/xyz/files/mobile/"
save_folder = "images"

os.makedirs(save_folder, exist_ok=True)
# Create the folder if it doesn't exist

headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "User-Agent": "Mozilla/5.0"
}

for i in range(1, 150):
    image_url = f"{base_url}{i}.jpg"
    print(image_url)
    response = requests.get(image_url, headers=headers)

    if response.status_code == 200:
        file_path = os.path.join(save_folder, f"{i}.jpg")
        with open(file_path, "wb") as file:
            file.write(response.content)
    else:
        print(f"Failed to download image {i}: {response.status_code}")
        # print(f"Failed to download image {i}: {response.content}")