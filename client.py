import pygame
from network import Network

# sets windows of height and width
width = 500
height = 500
win = pygame.display.set_mode((width, height))
# sets title on top of pygame window
pygame.display.set_caption("Client")

# defines drawing the screen. not called yet
def redrawWindow(win,player, player2):
    # makes background white
    win.fill((255,255,255))
    # draws players
    player.draw(win)
    player2.draw(win)
    pygame.display.update()

# defines the main function but not called yet
def main():
    run = True
    n = Network()
    # calls getP which returns everything the server is sending which is just the player
    p = n.getP()
    clock = pygame.time.Clock()

    while run:
        clock.tick(60)
        # send. sends info to server with your info and returns info on player2
        p2 = n.send(p)
        # checks if the x button is clicked and ends game
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
        # checks for your player moving
        p.move()
        # calls the function defined above
        redrawWindow(win, p, p2)
# calls the function defined above
main()
