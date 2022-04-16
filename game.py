
import pygame,sys,random
pygame.init()
def create_pipe():
    pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_Surface.get_rect(midtop = (500,pipe_pos))
    top_pipe = pipe_Surface.get_rect(midtop = (500,pipe_pos -650))
    return bottom_pipe,top_pipe
def move_pipe(pipes):
    for pipe in pipes:
        pipe.centerx -=4
    return pipes
def draw_pipe(pipes):
    for pipe in pipes:
        if pipe.bottom >=700:
            screen.blit(pipe_Surface,pipe)
        else :
            flip_pipe = pygame.transform.flip(pipe_Surface,False,True)
            screen.blit(flip_pipe,pipe)
def draw_floor():
    screen.blit(floor,(floor_pos_x,600))
    screen.blit(floor,(floor_pos_x+432,600))
def checkCollision(pipes):
    for pipe in pipes:
        if bird_rect.colliderect(pipe):
            return False
    if bird_rect.top <-75 or bird_rect.bottom >=600:
        return False
    return True
def score_display():
    score_surface = game_font.render(str(score),True,(255,255,255))
    score_rect = score_surface.get_rect(center = (216,100))
    screen.blit(score_surface,score_rect)
def high_score_display():
    high_score_surface = game_font.render('High score :'+str(high_score),True,(255,255,255))
    high_score_rect = high_score_surface.get_rect(center = (216,500))
    screen.blit(high_score_surface,high_score_rect)
screen = pygame.display.set_mode((432,750))
#create a background
bg = pygame.image.load('assets/background-night.png').convert()
bg = pygame.transform.scale2x(bg)
#create floor
floor = pygame.image.load('assets/floor.png').convert()
floor = pygame.transform.scale2x(floor)
floor_pos_x = 0
#create fps
clock = pygame.time.Clock()

game_font = pygame.font.Font('04b_19.ttf',40)
#create bird 
bird = pygame.image.load('assets/yellowbird-midflap.png').convert()
bird = pygame.transform.scale2x(bird)
bird_rect = bird.get_rect(center = (100,384))
#game variable 
score = 0
high_score = 0
gravity = 0.1
bird_movement = 0
#create pipe 
pipe_Surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_Surface = pygame.transform.scale2x(pipe_Surface)
pipe_list = []
pipe_height  = [400,350,300,250,200]
#set timer 
swap_pipe = pygame.USEREVENT
pygame.time.set_timer(swap_pipe,1200)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and game_active:
                bird_movement = 0
                bird_movement-=5
            if event.key == pygame.K_SPACE and game_active == False:
                game_active = True
                pipe_list.clear()
                bird_movement = 0
                bird_rect.center = (100,384)
        if event.type == swap_pipe and game_active:
            pipe_list.extend(create_pipe())
    screen.blit(bg,(0,0))
    game_active = checkCollision(pipe_list)
    if game_active:
        pipe_list = move_pipe(pipe_list)
        draw_pipe(pipe_list)
        bird_movement +=gravity
        bird_rect.centery += bird_movement
        screen.blit(bird,bird_rect)
        score_display()
        score = score//1
        for pipe in pipe_list:
            if pipe.centerx == bird_rect.centerx:
                score += 0.5
    else:
        if score > high_score:
            high_score = score
        score_display()
        high_score_display()
        score = 0
    draw_floor()
    floor_pos_x-=1
    if floor_pos_x <-432:
        floor_pos_x =0
    clock.tick(120)
    pygame.display.update()
