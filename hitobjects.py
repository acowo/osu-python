class HitObject:
    def __init__(self, x, y, time, objectType, play_area_width, play_area_height):
        self.scaled_x, self.scaled_y = self.scale_coordinates(x, y, play_area_width, play_area_height)
        self.type = objectType
        self.time = time
        
    def scale_coordinates(self, x, y, base_width, base_height, play_area_width, play_area_height):
        scaled_x = int((x / base_width) * play_area_width)
        scaled_y = int((y / base_height) * play_area_height)
        return scaled_x, scaled_y
