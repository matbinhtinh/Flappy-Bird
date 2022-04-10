import pygame, sys,random
def draw_floor():
    screen.blit(floor,(floor_x_pos,600))
    screen.blit(floor,(floor_x_pos+432,600))
def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(500,random_pipe_pos ))
    top_pipe = pipe_surface.get_rect(midtop=(500,random_pipe_pos-650 ))
    return bottom_pipe,top_pipe 
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -=5
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >= 700 :
            screen.blit(pipe_surface,pipe)
        else :
            flip_pipe = pygame.transform.flip(pipe_surface,False,True)
            screen.blit(flip_pipe,pipe)
pygame.init()
screen=pygame.display.set_mode((432,750))
clock = pygame.time.Clock()
#add background
bg = pygame.image.load('assets/background-night.png')
bg=pygame.transform.scale2x(bg)
#add floor
floor = pygame.image.load('assets/floor.png')
floor = pygame.transform.scale2x(floor)
floor_x_pos = 0
#add bird
bird = pygame.image.load('assets/yellowbird-midflap.png')
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100,384))
#create pipe
pipe_surface = pygame.image.load('assets/pipe-green.png') 
pipe_surface = pygame.transform.scale2x(pipe_surface)
pipe_list =[]
#create timer 
spawpipe = pygame.USEREVENT
pygame.time.set_timer(spawpipe,1200)
pipe_height = [400,200,300]

gravity = 0.25
bird_movement = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird_movement=0
                bird_movement-=8
        if event.type == spawpipe:
            pipe_list.extend(create_pipe())
    screen.blit(bg,(0,0))
    #bird's
    bird_movement +=gravity
    bird_rect.centery+=bird_movement
    screen.blit(bird,bird_rect)
    #pipe
    pipe_list = move_pipe(pipe_list)
    draw_pipe(pipe_list)
    #floor's
    floor_x_pos-=1
    draw_floor()
    if floor_x_pos <= -432 :
        floor_x_pos=0
    pygame.display.update()
    clock.tick(70)