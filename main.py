

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
        image = pygame.image.load("sprites/fon.jpg")
        screen.blit(image, (1000, 20))
        image = pygame.image.load("sprites/char_inventory.png")
        screen.blit(image, (1000, 20))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1040, 180))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1390, 180))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1215, 40))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1215, 370))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1215, 150))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1000, 550))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1070, 550))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1140, 550))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1210, 550))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1280, 550))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1350, 550))
        image = pygame.image.load("sprites/pole_inventori.png")
        screen.blit(image, (1420, 550))
        image = pygame.image.load("sprites/heart.png")
        screen.blit(image, (1000, 650))
        image = pygame.image.load("sprites/armor.png")
        screen.blit(image, (1250, 630))
        image = pygame.image.load("sprites/damage.png")
        screen.blit(image, (1250, 700))
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] == 1:
                    Tile(y, x)
                elif self.map[y][x] == 3:
                    image = pygame.image.load("sprites/item.png")
                    screen.blit(image, (y * self.tile_size + 5, x * self.tile_size + 5))

    def is_free(self, pos_x, pos_y):
        return int(self.map[pos_x][pos_y]) in self.free_tiles


class Character(pygame.sprite.Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__(player_group, all_sprites)
        self.invtntory = []
        self.eqwipment = []
        self.head = True
        self.bady = True
        self.legs = True
        self.left_hand = True
        self.right_hand = True
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
        for i in range(len(self.eqwipment)):
            self.hp += self.eqwipment[i].get_state()[1]
            self.damage += self.eqwipment[i].get_state()[2]
            self.armor += self.eqwipment[i].get_state()[3]
        screen.blit(self.image, (self.x * TILE_SIZE, self.y * TILE_SIZE))

    def add_item(self, item):
        if len(self.invtntory) <= 7:
            self.invtntory.append(item)

    def eqwip_item(self, item):
        if item.get_state()[0] == "head":
            if self.head:
                self.eqwipment.append(item)
                del self.invtntory[self.invtntory.index(item)]
                self.head = False
        if item.get_state()[0] == "bady":
            if self.bady:
                self.eqwipment.append(item)
                del self.invtntory[self.invtntory.index(item)]
                self.bady = False
        if item.get_state()[0] == "legs":
            if self.legs:
                self.eqwipment.append(item)
                del self.invtntory[self.invtntory.index(item)]
                self.legs = False
        if item.get_state()[0] == "right_hand" or item.get_state()[0] == "left_hand":
            if self.left_hand:
                self.eqwipment.append(item)
                del self.invtntory[self.invtntory.index(item)]
                self.left_hand = False
            elif self.right_hand:
                self.eqwipment.append(item)
                del self.invtntory[self.invtntory.index(item)]
                self.right_handd = False

    def remove_item(self,item):
        del self.invtntory[self.invtntory.index(item)]

    def aneqwip_item(self, item):
        if item.get_state()[0] == "head":
            if self.head:
                self.invtntory.append(item)
                del self.eqwipment[self.eqwipment.index(item)]
                self.head = False
        if item.get_state()[0] == "bady":
            if self.bady:
                self.invtntory.append(item)
                del self.eqwipment[self.eqwipment.index(item)]
                self.bady = False
        if item.get_state()[0] == "legs":
            if self.legs:
                self.invtntory.append(item)
                del self.eqwipment[self.eqwipment.index(item)]
                self.legs = False
        if item.get_state()[0] == "right_hand" or item.get_state()[0] == "left_hand":
            if self.left_hand:
                self.invtntory.append(item)
                del self.eqwipment[self.eqwipment.index(item)]
                self.left_hand = False
            elif self.right_hand:
                self.invtntory.append(item)
                del self.eqwipment[self.eqwipment.index(item)]
                self.right_handd = False



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


class Item:
    def __init__(self, pos, hp, damage, armore, image):
        self.image = pygame.image.load(image)
        self.pos = pos
        self.hp = hp
        self.damage = damage
        self.armore = armore

    def get_state(self):
        return [self.pos, self.hp, self.damage, self.armore]




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
        game.rendr()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()