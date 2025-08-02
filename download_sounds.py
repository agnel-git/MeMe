import os
import requests

# Folder to save sounds
os.makedirs("sounds", exist_ok=True)

# Base GitHub URL for raw .wav files
base_url = "https://raw.githubusercontent.com/parisjava/wav-piano-sound/master/wav/"

# List of .wav filenames in the repo
filenames = [
    "a1.wav", "a1s.wav", "b1.wav",
    "c1.wav", "c1s.wav", "c2.wav",
    "d1.wav", "d1s.wav", "e1.wav",
    "f1.wav", "f1s.wav", "g1.wav", "g1s.wav"
]

# Download each file
for name in filenames:
    url = base_url + name
    response = requests.get(url)
    if response.status_code == 200:
        with open(os.path.join("sounds", name), "wb") as f:
            f.write(response.content)
        print(f"Downloaded: {name}")
    else:
        print(f"Failed to download: {name}")
