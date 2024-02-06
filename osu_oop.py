import pygame
import os
from math import dist
import json
from tkinter import filedialog
from hitobjects import HitObject
BASE_WIDTH = 512
BASE_HEIGHT = 384
FPS = 60

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BACKGROUND = (WHITE)


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
clock = pygame.time.Clock()
screen_width, screen_height = screen.get_size()
play_area_width = min(screen_width, int(screen_height * (4 / 3)))
play_area_height = int(play_area_width * (3 / 4))

json_file_path = str(filedialog.askopenfilename())
beatmap_dir = os.path.dirname(json_file_path)
with open(json_file_path, 'r') as j:
    beatmapProperties = json.loads(j.read())
music = f'/{beatmapProperties["general"]["AudioFilename"].strip()}'

class Game:
    def __init__(self):
        self.time_at_start = pygame.time.get_ticks()
        self.playing = False


hitObjectList = []

hitObjectList = []

for i in range(len(beatmapProperties["hitobjects"])):
    newHitObject = HitObject(
        int(beatmapProperties["hitobjects"][i]['x']),
        int(beatmapProperties["hitobjects"][i]['y']),
        int(beatmapProperties["hitobjects"][i]['time']),
        int(beatmapProperties["hitobjects"][i]['type']),
        BASE_HEIGHT,
        BASE_WIDTH,
        play_area_width,
        play_area_height
    )
    hitObjectList.append(newHitObject)


running = True
game = Game()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if not game.playing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                        game.playing = True
                        music.play()
                 
        # else:
        #     hit_time = hitObjectList[][2]
        #     time_elapsed = pygame.time.get_ticks()-time_at_start