

import pygame, random

FPS = 15
TILE_SIZE = 40
tile_w = tile_h = 40



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
                    Tile(y, x)
                elif self.map[y][x] == 3:
                    image = pygame.image.load("sprites/item.png")
                    screen.blit(image, (x * self.tile_size + 5, y * self.tile_size + 5))

    def is_free(self, pos_x, pos_y):
        return int(self.map[pos_x][pos_y]) in self.free_tiles


class Character(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.invtntory = []
        self.armor = 20
        self.hp = 100
        self.damage = 15
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
    # зададим начальный сдвиг камеры
    def __init__(self):
        self.dx = 0
        self.dy = 0

    # сдвинуть объект obj на смещение камеры
    def apply(self, obj):
        obj.rect.x += self.dx
        obj.rect.y += self.dy

    # позиционировать камеру на объекте target
    def update(self, target):
        self.dx = -(target.rect.x + target.rect.w // 2 - width // 2)
        self.dy = -(target.rect.y + target.rect.h // 2 - height // 2)

class Game:
    def __init__(self, mapp, character):
        self.mapp = mapp
        self.character = character

    def rendr(self):
        self.mapp.render(screen)
        self.character.render(screen)

    def update_character(self):
        next_x, next_y = self.character.get_position()
        if pygame.key.get_pressed()[pygame.K_LEFT]:
            next_x -= 1
        if pygame.key.get_pressed()[pygame.K_RIGHT]:
            next_x += 1
        if pygame.key.get_pressed()[pygame.K_UP]:
            next_y -= 1
        if pygame.key.get_pressed()[pygame.K_DOWN]:
            next_y += 1
        if self.mapp.is_free(next_x, next_y):
            self.character.set_position((next_x, next_y))




camera = Camera()

if __name__ == '__main__':
    pygame.init()
    pygame.display.set_caption('')
    size = width, height = (1500, 800)
    screen = pygame.display.set_mode(size)

    mapor = Map_editor("map0", [0, 2, 3], 2)
    charik = Character(1, 1)
    game = Game(mapor, charik)
    image = pygame.image.load("sprites/item.png")
    screen.blit(image, (80, 80))

    running = True
    clock = pygame.time.Clock()
    camera.update(charik)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        for sprite in all_sprites:
            camera.apply(sprite)
        game.update_character()
        screen.fill((0, 0, 0))
        image = pygame.image.load("sprites/fon.jpg")
        screen.blit(image, (1000, 20))
        image = pygame.image.load("sprites/char_inventory.png")
        screen.blit(image, (1000, 20))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1040, 250))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1390, 250))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1150, 40))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1130, 370))
        game.rendr()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()