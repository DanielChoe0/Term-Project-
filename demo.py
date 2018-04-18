import pygame 

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
pygame.init()
gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.update() 

pygame.display.set_caption("demo")

gameExit = False 

lead_x = 300 
lead_y = 300 

while not gameExit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameExit = True 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x -= 10
            if event.key == pygame.K_RIGHT:
                lead_x += 10 
            if event.key == pygame.K_UP:
                lead_y -= 10 
            if event.key == pygame.K_DOWN:
                lead_y += 10 
    gameDisplay.fill(white)
    pygame.draw.rect(gameDisplay, red, [lead_x, lead_y, 10, 10]) 
    
    
    pygame.display.update()
pygame.quit()
quit()



