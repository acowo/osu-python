import pygame

class Game:
    def __init__(self, hitobjects, music, screen):
        self.hitObjects = hitobjects
        self.playing = False
        self.music = music
        self.screen = screen
        self.currentObject = 0

    def handle_event(self, event):
        if not self.playing:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.time_at_start = pygame.time.get_ticks()
                    self.playing = True
                    self.music.play()
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pass

    def render(self):
        self.screen.fill((255,255,255))
        for hitObject in self.hitObjects:
            time_elapsed = pygame.time.get_ticks()-self.time_at_start
            time_difference = hitObject.time - time_elapsed
            approach_circle_radius = max(0, 50 + time_difference / 9)
            if -125 <= time_difference <= 600:  # Object is within the hit window
                pygame.draw.circle(self.screen, (0,0,0), (hitObject.scaled_x, hitObject.scaled_y), 35)
                pygame.draw.circle(self.screen, (255, 0, 0), (hitObject.scaled_x, hitObject.scaled_y), approach_circle_radius, 2)
            elif time_difference < -125:
                approach_circle_radius = 0