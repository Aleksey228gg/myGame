from symtable import Class

import pygame, random

FPS = 15
TILE_SIZE = 40
tile_w = tile_h = 40



def generation():
    map_g = []
    serset = ['0', '1', '1', '0', '0', '0']
    for i in range(20):
        map_g.append([])
        for e in range(35):
            if i == 0 or i == 19 or e == 0 or e == 34:
                map_g[i].append("1")
            else:
                map_g[i].append(random.choice(serset))
    map_g[6][6] = '0'
    f = open("maps/map0", "w")
    for i in range(20):
        f.write(' '.join(map_g[i]) + "\n")


generation()
all_sprites = pygame.sprite.Group()
tiles_group = pygame.sprite.Group()
player_group = pygame.sprite.Group()

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(tiles_group, all_sprites)
        self.x, self.y = pos_x, pos_y
        self.image = pygame.image.load("sprites/wall.jpg")
        screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))
        self.rect = self.image.get_rect().move(pos_x * tile_w + 5, pos_y * tile_h + 5)

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
                    Tile(x, y)
                elif self.map[y][x] == 3:
                    image = pygame.image.load("sprites/item.png")
                    screen.blit(image, (x * self.tile_size + 5, y * self.tile_size))


class Character(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.x, self.y = pos_x, pos_y
        self.image = pygame.image.load("sprites/character.png")
        self.rect = self.image.get_rect().move(pos_x * tile_w + 5, pos_y * tile_h + 5)

    def get_position(self):
        return self.x, self.y

    def set_position(self, position):
        self.x, self.y = position

    def render(self, screen):
        screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))



width, height = 600, 600

class Camera:
    def __init__(self):
        self.dx = 0
        self.dy = 0

    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)

camera = Camera()


if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('')
    size = width, height = 520, 520
    screen = pygame.display.set_mode(size)

    mapor = Map_editor("map0", [0, 2, 3], 2)
    charik = Character(6, 6)

    running = True
    clock = pygame.time.Clock()
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for sprite in all_sprites:
            camera.apply(sprite)
        screen.fill((0, 0, 0))
        mapor.render(screen)
        charik.render(screen)
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()
