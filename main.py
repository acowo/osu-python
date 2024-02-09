import pygame
from modules.hitobjects import HitObject
from modules.json_import import getBeatmapData
from game import Game
import os

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

beatmapPath, beatmapProperties = getBeatmapData()
beatmapDir = os.path.dirname(beatmapPath)
audioFileName = beatmapProperties["general"]["AudioFilename"].strip()
audioDir = f'{beatmapDir}\{audioFileName}'.replace("/", "\\")

music = pygame.mixer.Sound(audioDir)

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
game = Game(hitObjectList, music, screen)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            game.handle_event(event)
    if game.playing:
        game.render()
    
    pygame.display.flip()
