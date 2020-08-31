import pygame

class Block(pygame.sprite.Sprite):
    def __init__(self, image, pos):
        pygame.sprite.Sprite.__init__(self)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.center = pos

class Hero(Block):
    pass

class Monster(Block):
    pass

def main():
    width = 512
    height = 480
    

    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('Sean\'s Monster Game')
    
    clock = pygame.time.Clock()
    

    # Load Images
    background_image = pygame.image.load('images/background.png').convert_alpha()
    hero_image = pygame.image.load('images/hero.png').convert_alpha()
    monster_image = pygame.image.load('images/monster.png').convert_alpha()

    # Our hero
    player = Hero(hero_image, [250, 250])
    player.move = [pygame.K_LEFT, pygame.K_RIGHT, pygame.K_UP, pygame.K_DOWN]
    player.vx = 5
    player.vy = 5

    player_group = pygame.sprite.Group()
    player_group.add(player)

    # Our monster
    monster = Monster(monster_image, [50, 100])
    monsters_group = pygame.sprite.Group()
    monsters_group.add(monster)

    # Game initialization

    running = True
    while running:
        for event in pygame.event.get():

            # Event handling
            if event.type == pygame.QUIT:
                running = False

        # Game logic
        
        
        key = pygame.key.get_pressed()

        for i in range(2):
            if key[player.move[i]]:
                player.rect.x += player.vx * [-1, 1][i]

        for i in range(2):
            if key[player.move[2:4][i]]:
                player.rect.y += player.vy * [-1, 1][i]
        
        monster.rect.x += 3 
        monster.rect.y += 3  
        # first parameter takes a single sprite
        # second parameter takes sprite groups
        # third parameter is a do kill commad if true
        # all group objects colliding with the first parameter object will be
        # destroyed. 
        hit = pygame.sprite.spritecollide(player, monsters_group, True)

        if hit:
            # if collision is detected call a function
            monster.kill()

        # Draw background
        screen.blit(background_image, [0, 0])
        
        # Game display
        player_group.draw(screen)
        monsters_group.draw(screen)
        
        pygame.display.update()
        clock.tick(60)

    pygame.quit()

if __name__ == '__main__':
    main()
