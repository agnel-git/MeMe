import pygame
from pygame import mixer
import os
import json

pygame.init()
mixer.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Keyboard Piano")

font = pygame.font.SysFont("Sans serif", 30)

WHITE_KEYS = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k']
WHITE_NOTES = ['C', 'D', 'E', 'F', 'G', 'A', 'B', 'C']
BLACK_KEYS = ['w', 'e', None, 't', 'y', 'u', None]
BLACK_NOTES = ['C#', 'D#', 'F#', 'G#', 'A#']

octave = 4  # Default octave

def load_sounds(octave):
    sounds = {}

    for i, key in enumerate(WHITE_KEYS):
        note = WHITE_NOTES[i] + str(octave)
        path = f"sounds/{note}.wav"
        if os.path.exists(path):
            sounds[pygame.key.key_code(key)] = mixer.Sound(path)

    black_note_index = 0
    for key in BLACK_KEYS:
        if key is not None:
            note = BLACK_NOTES[black_note_index] + str(octave)
            path = f"sounds/{note}.wav"
            if os.path.exists(path):
                sounds[pygame.key.key_code(key)] = mixer.Sound(path)
            black_note_index += 1

    return sounds

sounds = load_sounds(octave)

heatmap = {k: 0 for k in WHITE_KEYS + [k for k in BLACK_KEYS if k]}
sustain = False

running = True
while running:
    screen.fill((220, 210, 255))
    text = font.render("~ MELODY MAP! ~ ", True, (30, 30, 30))
    screen.blit(text, (50, 50))

    max_count = max(1, max(heatmap.values()))

    # Draw white keys
    for i, k in enumerate(WHITE_KEYS):
        x = 80 + i * 80
        y = 150
        w, h = 60, 100
        intensity = int((heatmap[k] / max_count) * 255)
        color = (intensity, 0, 255 - intensity)
        pygame.draw.rect(screen, color, (x, y, w, h))
        pygame.draw.rect(screen, (255, 255, 255), (x, y, w, h), 2)
        label = font.render(k.upper(), True, (255, 255, 255))
        screen.blit(label, (x + 20, y + 35))

    # Draw black keys
    for i, k in enumerate(BLACK_KEYS):
        if k is None:
            continue
        x = 120 + i * 80
        y = 150
        w, h = 40, 70
        intensity = int((heatmap[k] / max_count) * 255)
        color = (intensity, intensity, intensity)
        pygame.draw.rect(screen, color, (x, y, w, h))
        pygame.draw.rect(screen, (0, 0, 0), (x, y, w, h), 2)
        label = font.render(k.upper(), True, (0, 0, 0))
        screen.blit(label, (x + 12, y + 20))

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            with open("heatmap_data.json", "w") as f:
                json.dump(heatmap, f, indent=4)
            running = False

        if event.type == pygame.KEYDOWN:
            keyname = pygame.key.name(event.key)

            if event.key == pygame.K_SPACE:
                sustain = True

            elif event.key == pygame.K_z and octave > 3:
                octave -= 1
                sounds = load_sounds(octave)
                print(f"⬅️ Octave down: {octave}")
            elif event.key == pygame.K_x and octave < 5:
                octave += 1
                sounds = load_sounds(octave)
                print(f"➡️ Octave up: {octave}")

            elif event.key in sounds:
                if sustain:
                    sounds[event.key].play(fade_ms=700)
                else:
                    sounds[event.key].play()
                if keyname in heatmap:
                    heatmap[keyname] += 1

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                sustain = False

pygame.quit()
