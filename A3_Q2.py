import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Side-Scrolling 2D Game")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Player settings
PLAYER_WIDTH = 50
PLAYER_HEIGHT = 60
PLAYER_COLOR = (0, 0, 255)
PLAYER_SPEED = 5
PLAYER_JUMP_SPEED = 15
GRAVITY = 1
MAX_JUMP_HEIGHT = 200

# Projectile settings
PROJECTILE_SPEED = 10

# Enemy settings
ENEMY_SPEED = 3

# Collectible settings
COLLECTIBLE_SPEED = 2

# Game settings
NUM_LEVELS = 3
ENEMIES_PER_LEVEL = 5
COLLECTIBLES_PER_LEVEL = 3
MAX_HEALTH = 100
MAX_LIVES = 3

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
        self.image.fill(PLAYER_COLOR)
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
        self.speed_x = 0
        self.speed_y = 0
        self.is_jumping = False
        self.health = MAX_HEALTH
        self.lives = MAX_LIVES
        self.score = 0
        self.shoot_delay = 500  # Delay between shots in milliseconds
        self.last_shot = pygame.time.get_ticks()

    def update(self):
        self.speed_y += GRAVITY
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Prevent the player from falling through the ground
        if self.rect.bottom > SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT
            self.speed_y = 0
            self.is_jumping = False

    def move_left(self):
        self.speed_x = -PLAYER_SPEED

    def move_right(self):
        self.speed_x = PLAYER_SPEED

    def stop(self):
        self.speed_x = 0

    def jump(self):
        if not self.is_jumping and self.rect.bottom >= SCREEN_HEIGHT:
            self.speed_y = -PLAYER_JUMP_SPEED
            self.is_jumping = True

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            projectile = Projectile(self.rect.right, self.rect.centery)
            all_sprites.add(projectile)
            projectiles.add(projectile)

class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 5))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = PROJECTILE_SPEED

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.left > SCREEN_WIDTH:
            self.kill()

class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed_x = -ENEMY_SPEED

    def update(self):
        self.rect.x += self.speed_x
        if self.rect.right < 0:
            self.rect.left = SCREEN_WIDTH

class Collectible(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Create sprite groups
all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
collectibles = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

# Function to generate enemies
def create_enemies(level):
    for _ in range(ENEMIES_PER_LEVEL * level):
        enemy = Enemy(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2), SCREEN_HEIGHT - PLAYER_HEIGHT - 10)
        all_sprites.add(enemy)
        enemies.add(enemy)

# Function to generate collectibles
def create_collectibles(level):
    for _ in range(COLLECTIBLES_PER_LEVEL * level):
        collectible = Collectible(random.randint(SCREEN_WIDTH, SCREEN_WIDTH * 2), random.randint(SCREEN_HEIGHT // 2, SCREEN_HEIGHT - 50))
        all_sprites.add(collectible)
        collectibles.add(collectible)

# Main game loop
running = True
current_level = 1
player_alive = True

while running:
    if player_alive:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    player.move_left()
                elif event.key == pygame.K_RIGHT:
                    player.move_right()
                elif event.key == pygame.K_SPACE:
                    player.jump()
                elif event.key == pygame.K_x:
                    player.shoot()
            elif event.type == pygame.KEYUP:
                if event.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    player.stop()

        # Update all sprites
        all_sprites.update()

        # Check for collisions between projectiles and enemies
        hits = pygame.sprite.groupcollide(projectiles, enemies, True, True)
        for hit in hits:
            player.score += 10

        # Check for collisions between player and collectibles
        collectible_hits = pygame.sprite.spritecollide(player, collectibles, True)
        for collectible in collectible_hits:
            player.health += 20
            if player.health > MAX_HEALTH:
                player.health = MAX_HEALTH

        # Draw everything
        screen.fill(WHITE)
        all_sprites.draw(screen)

        # Draw player health bar
        pygame.draw.rect(screen, RED, (10, 10, player.health, 20))

        # Draw player score
        font = pygame.font.Font(None, 36)
        text = font.render("Score: " + str(player.score), True, BLACK)
        screen.blit(text, (SCREEN_WIDTH - 200, 10))

        # Flip the display
        pygame.display.flip()

        # Cap the frame rate
        pygame.time.Clock().tick(60)

        # Check if there are no enemies and create new ones
        if len(enemies) == 0:
            create_enemies(current_level)
            create_collectibles(current_level)
    else:
        # Game over screen
        screen.fill(WHITE)
        font = pygame.font.Font(None, 72)
        text = font.render("Game Over", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - 150, SCREEN_HEIGHT // 2 - 50))
        text = font.render("Press 'R' to restart", True, BLACK)
        screen.blit(text, (SCREEN_WIDTH // 2 - 250, SCREEN_HEIGHT // 2 + 50))
        pygame.display.flip()

        # Check for restart
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:  # Restart the game
                    player.health = MAX_HEALTH
                    player.lives -= 1
                    player_alive = True
                    if player.lives <= 0:
                        running = False
                    else:
                        current_level = 1
                        player.rect.x = 100
                        player.rect.y = SCREEN_HEIGHT - PLAYER_HEIGHT - 10
                        all_sprites.empty()
                        projectiles.empty()
                        enemies.empty()
                        collectibles.empty()
                        all_sprites.add(player)
                        create_enemies(current_level)
                        create_collectibles(current_level)

# Outside the main loop
pygame.quit()
sys.exit()