import pygame
import math

pygame.init()

WIDTH, HEIGHT = 900, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Gravitational Effect')

PLANET_MASS = 300
SHIP_MASS = 10
G = 10
FPS = 60
PLANET_SIZE = 50
OBJECT_SIZE = 10
VEL_SCALE = 100

BACKGROUND = pygame.transform.scale(pygame.image.load('background.jpg'), (WIDTH, HEIGHT))
PLANET = pygame.image.load('jupiter.png')
PLANET = pygame.transform.scale(PLANET, (PLANET_SIZE*4, PLANET_SIZE*4))
SPACESHIP = pygame.image.load('ufo.png')  
SPACESHIP = pygame.transform.scale(SPACESHIP, (OBJECT_SIZE * 6, OBJECT_SIZE * 6))


WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

class Planet:
    def __init__(self, x, y, mass):
        self.x = x
        self.y = y
        self.mass = mass

    def draw(self):
        window.blit(PLANET, (self.x - PLANET_SIZE, self.y - PLANET_SIZE))

class Spaceship:
    def __init__(self, x, y, vel_x, vel_y, mass):
        self.x = x
        self.y = y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.mass = mass
        
    def draw(self):
        #pygame.draw.circle(window, RED, (int(self.x), int(self.y)), OBJECT_SIZE)
        window.blit(SPACESHIP, (self.x - OBJECT_SIZE * 2, self.y - OBJECT_SIZE * 2))
        
    def move(self, planet=None):
        distance = math.sqrt((self.x - planet.x)**2 + (self.x - planet.y)**2)
        force = (G * self.mass * planet.mass) / distance**2
        acceleartion = force / self.mass
        angle = math.atan2(planet.y - self.y, planet.x - self.x)
        
        acceleation_x = acceleartion*math.cos(angle)
        acceleation_y = acceleartion*math.sin(angle)
        
        self.vel_x += acceleation_x
        self.vel_y += acceleation_y
        
        self.x += self.vel_x
        self.y += self.vel_y

def create_ship(location, mouse):
    t_x, t_y = location
    m_x, m_y = mouse
    vel_x = m_x - t_x  
    vel_x = vel_x/VEL_SCALE
    vel_y = m_y - t_y  
    vel_y = vel_y/VEL_SCALE
    obj = Spaceship(t_x, t_y, vel_x, vel_y, SHIP_MASS)
    return obj 

def main():
    running = True
    clock = pygame.time.Clock()
    
    planet = Planet(WIDTH //3 , HEIGHT//3 , PLANET_MASS)
    
    objects = []
    temp_obj_pos = None
    
    while running:
        clock.tick(FPS)
        
        mouse_pos = pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                if temp_obj_pos:
                    obj = create_ship(temp_obj_pos, mouse_pos)
                    objects.append(obj)
                    temp_obj_pos = None
                else:
                    temp_obj_pos = mouse_pos
                
        window.blit(BACKGROUND, (0,0))
        
        if temp_obj_pos:
            pygame.draw.line(window, WHITE, temp_obj_pos, mouse_pos, 2)
            #pygame.draw.circle(window, RED, temp_obj_pos, OBJECT_SIZE)
            window.blit(SPACESHIP, (temp_obj_pos[0] - OBJECT_SIZE * 2, temp_obj_pos[1] - OBJECT_SIZE * 2))
            
        for obj in objects[:]:
            obj.draw()
            obj.move(planet)
            off_screen = obj.x <0 or obj.x > WIDTH or obj.y< 0 or obj.y > HEIGHT
            collided = math.sqrt((obj.x - planet.x)**2 + (obj.y - planet.y)**2) <= PLANET_SIZE

            
            if off_screen or collided:
                objects.remove(obj)
            
        planet.draw()
        pygame.display.update()
    pygame.quit()
        

if __name__ == "__main__":
    main()