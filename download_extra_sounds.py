import os
import requests

# Make sure the 'sounds' folder exists
os.makedirs("sounds", exist_ok=True)

# Base URL for the WAV files (change if needed)
base_url = "https://github.com/abdelazizelsherbiny/piano-sound-files/raw/main/wav/"

# Notes for C5 to B5
notes = [
    "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5"
]

# Optionally, add this if you also want to support octave down (C3–B3)
notes = [
   "C3", "C#3", "D3", "D#3", "E3", "F3", "F#3", "G3", "G#3", "A3", "A#3", "B3",
    "C5", "C#5", "D5", "D#5", "E5", "F5", "F#5", "G5", "G#5", "A5", "A#5", "B5"
]

for note in notes:
    url = f"{base_url}{note}.wav"
    path = os.path.join("sounds", f"{note}.wav")

    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise error for bad status
        with open(path, "wb") as f:
            f.write(response.content)
        print(f"✅ Downloaded: {note}.wav")
    except Exception as e:
        print(f"❌ Failed to download {note}: {e}")
