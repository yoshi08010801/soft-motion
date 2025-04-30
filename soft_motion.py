import pygame
import sys
import datetime
import math

pygame.init()
with open("gentle_quotes.txt", "r", encoding="utf-8") as f:
    messages = [line.strip() for line in f if line.strip()]
    
msg_index = 0
current_msg = messages[msg_index]

width, height = 500, 500
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
fade_duration =2000
display_duration =2000
total_duration = fade_duration * 2 + display_duration

last_switch_time = pygame.time.get_ticks()



blue = (100, 150, 255)
x = width // 2
y = height
speed = -1



font = pygame.font.SysFont(None, 36)
clock_font = pygame.font.SysFont(None, 32)

prev_sign = None

def get_fitting_font(text, max_width, max_size=48, min_size=12):
    for size in range(max_size, min_size - 1, -2):
        font = pygame.font.SysFont(None, size)
        surface = font.render(text, True, (0, 0, 0))
        if surface.get_width() <= max_width:
            return font
        
    return pygame.font.SysFont(None, min_size)    


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit
            sys.exit()
            
    screen.fill((245, 245, 245))
    
    pygame.draw.circle(screen, (100, 150, 255), (x, y), 30)
    pygame.draw.circle(screen, blue, (x, y), 30)
    
    current_time = pygame.time.get_ticks()
    elapsed = current_time - last_switch_time
    
    if elapsed >= total_duration:
        msg_index = (msg_index + 1) % len(messages)
        current_msg = messages[msg_index]
        last_switch_time = current_time
        elapsed = 0
    
    if elapsed < fade_duration:
        alpha = int((elapsed / fade_duration) * 255)
    elif elapsed < fade_duration + display_duration:
        alpha = 255
    else:
        fade_out_time = elapsed - (fade_duration + display_duration)
        alpha = int(255 - (fade_out_time / fade_duration) * 255)
    
   
    
    
                       
    max_text_width = width - 60
    font = get_fitting_font(current_msg, max_text_width)
    
    text_surface = font.render(current_msg, True, (80, 80, 80)).convert_alpha()
    text_surface.set_alpha(alpha)
    text_rect = text_surface.get_rect(center=(width // 2, height // 2))
    screen.blit(text_surface, text_rect)
    
    now = datetime.datetime.now()
    time_text = clock_font.render(now.strftime("%H:%M:%S"), True,(120, 120, 120))
    screen.blit(time_text, (width - 140, 20))
    
    
   
    
    
   
    
    
    y += speed
    if y < 50 or y > height:
        speed *= -1
        
    pygame.display.flip()
    clock.tick(60)