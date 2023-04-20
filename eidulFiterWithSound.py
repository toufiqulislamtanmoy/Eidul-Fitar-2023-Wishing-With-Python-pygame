import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set the screen dimensions
screen_width = 1200
screen_height = 600

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the background color
background_color = (0, 0, 0)




# Set the font and font size
font = pygame.font.Font(None, 60)

# Create the text surface with gradient effect
text_surface = font.render("Wish you Very Happy Eid Mubarak 2023", True, pygame.Color('#ff0000'))




text_rect = text_surface.get_rect(center=(screen_width//2, screen_height//2))

# Set the speed of the text
text_speed = -5


# Set the font and font size for the developer name
developer_font = pygame.font.Font(None, 35)

# Create the developer name text surface
developer_surface = developer_font.render("Tanmoy", True, pygame.Color('#d2b48c'))

# Get the rect for the developer name surface
developer_rect = developer_surface.get_rect()

# Set the position of the developer name
developer_rect.bottomright = (screen_width - 10, screen_height - 10)

# Draw the developer name onto the main text surface




# Set the fireworks colors
fireworks_colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 255, 255)]
fireworks_particles = []

# Firework particle class
class FireworkParticle:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.size = 5
        self.speed = random.randint(5, 10)
        self.angle = random.uniform(0, 2 * math.pi)
        
    def update(self):
        self.x += self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        self.speed -= 0.2
        self.size -= 0.05
        
    def draw(self, surface):
        pygame.draw.circle(surface, self.color, (int(self.x), int(self.y)), int(self.size))

# Load and play the music
pygame.mixer.music.load('romzan_ar_rozar_ses.mp3')
pygame.mixer.music.play(-1)

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move the text
    text_rect.move_ip(text_speed, 0)
    
    # Check if the text has gone off the screen
    if text_rect.right < 0:
        text_rect.left = screen_width
    
    # Draw the background
    screen.fill(background_color)
    
    # Draw the text
    screen.blit(text_surface, text_rect)
    screen.blit(developer_surface, developer_rect)
    
    # Create fireworks particles
    if random.randint(0, 100) < 5:
        x = random.randint(0, screen_width)
        y = random.randint(screen_height // 2, screen_height)
        color = random.choice(fireworks_colors)
        fireworks_particles.extend([FireworkParticle(x, y, color) for i in range(100)])
    
    # Update and draw fireworks particles
    for particle in fireworks_particles:
        particle.update()
        particle.draw(screen)
    
    fireworks_particles = [particle for particle in fireworks_particles if particle.size > 0]
    
    # Update the screen
    pygame.display.update()
    
    # Set the frame rate
    pygame.time.Clock().tick(60)

# Quit Pygame
pygame.quit()
