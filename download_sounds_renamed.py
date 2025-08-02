# download_sounds_renamed.py

import os
import requests

# Folder to save sounds
os.makedirs("sounds", exist_ok=True)

# Base GitHub URL for raw .wav files
base_url = "https://raw.githubusercontent.com/parisjava/wav-piano-sound/master/wav/"

# Original filenames in GitHub
filenames = [
    "a1.wav", "a1s.wav", "b1.wav",
    "c1.wav", "c1s.wav", "d1.wav", "d1s.wav",
    "e1.wav", "f1.wav", "f1s.wav", "g1.wav", "g1s.wav"
]

# Mapping to rename files to C4–B4 format
note_map = {
    "a1.wav": "A4.wav", "a1s.wav": "A#4.wav", "b1.wav": "B4.wav",
    "c1.wav": "C4.wav", "c1s.wav": "C#4.wav", "d1.wav": "D4.wav",
    "d1s.wav": "D#4.wav", "e1.wav": "E4.wav", "f1.wav": "F4.wav",
    "f1s.wav": "F#4.wav", "g1.wav": "G4.wav", "g1s.wav": "G#4.wav"
}

# Download and rename each file
for name in filenames:
    url = base_url + name
    new_name = note_map.get(name, name)
    filepath = os.path.join("sounds", new_name)

    response = requests.get(url)
    if response.status_code == 200:
        with open(filepath, "wb") as f:
            f.write(response.content)
        print(f"✅ Downloaded: {new_name}")
    else:
        print(f"❌ Failed to download: {new_name}")
