from symtable import Class

import pygame

FPS = 15
TILE_SIZE = 40

class Map_editor:
    def __init__(self, map_name, free_tile, finish_tile):
        self.map = []
        with open("maps/" + map_name) as map_file:
            for line in map_file:
                self.map.append(list(map(int, line.split())))
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.tile_size = TILE_SIZE
        self.free_tiles = free_tile
        self.finish_tile = finish_tile

    def render(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == 1:
                    image = pygame.image.load("sprites/wall.jpg")
                    screen.blit(image, (x * self.tile_size, y * self.tile_size))
                elif self.map[y][x] == 3:
                    image = pygame.image.load("sprites/item.png")
                    screen.blit(image, (x * self.tile_size + 5, y * self.tile_size))


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('')
    size = width, height = 1200, 800
    screen = pygame.display.set_mode(size)

    mapor = Map_editor("map0", [0, 2, 3], 2)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        screen.fill((0, 0, 0))
        mapor.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()