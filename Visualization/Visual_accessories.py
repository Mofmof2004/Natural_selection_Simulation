import pygame
from Visualization.Visual_general import *
import time
from Simulation.Display_settings import *
from Visualization.Zoom.Zoom_1 import zoom_1

def PLayer_show(msg,x,y,w,h,c, size):
    """
    Use to show a message in any place on the screen for an infinite time
    :param msg: message shown
    :param x: x position of the message
    :param y: y position of the message
    :param w: width of the message
    :param h: height of the message
    :param c: colour of the text
    :param size: size if the text
    """
    # Draw a rectangle
    pygame.draw.rect(gameDisplay, black, (x, y, w, h))
    # create the text settings use for the message
    smalltext = pygame.font.Font("freesansbold.ttf", size)
    textsurf, textrect = text_objects(msg, smalltext, c)
    # center the text in the rectangle and on the screen position
    textrect.center = (x + (w / 2), y + (h / 2))
    gameDisplay.blit(textsurf, textrect)

def text_objects(text, font, colour):
    """
    Use to render font and create the message
    :param text: message wanted to be displayed
    :param font: size of the message
    :param colour: the colour of the text
    :return: the message and the rectangle conatin the message
    """
    textSurface = font.render(text, True, colour)
    return textSurface, textSurface.get_rect()

def message_display(text, font_size, time_sleep, colour, x, y, w, h):
    """
    To display a message for a certain time but stops all other code running for a certain time
    :param text: message shown
    :param font_size: size of the text
    :param time_sleep: how long the message will be shown
    :param colour: colour of the text
    :param x: x position of the text
    :param y: y position of the text
    :param w: width of the text
    :param h: height of the text
    """

    # create the text settings used for the message display
    largeText = pygame.font.Font('freesansbold.ttf', font_size)

    # Create the message wanted
    textsurf, textrect = text_objects(text, largeText, colour)

    # position the message
    textrect.center = (x + (w / 2), y + (h / 2))

    # print message on the screen
    gameDisplay.blit(textsurf, textrect)

    # update the screen
    pygame.display.update()

    # show this message for a certain time
    time.sleep(time_sleep)

def button(msg, x, y, w, h, ic, ac, inf, action=None):
    """
    Use to create functional buttons
    :param msg: message display
    :param x: x position
    :param y: y position
    :param w: width of the button
    :param h: height of the button
    :param ic: inactive colour
    :param ac: active coulour
    :param inf: information the function needs
    :param action: call function
    """
    print("called")
    # Get the x, y mouse position
    mouse = pygame.mouse.get_pos()
    # Get the mouse clicks
    click = pygame.mouse.get_pressed()

    # check if the mouse is over the button
    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        # draw rectangle with the active coulour
        print("clicked")
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        # Check if the mouse clicks on the button
        if click[0] == 1 and action != None:
                # Call the function linked to the button
                action(inf)


    # mouse not over button
    else:
        # draw rectangle with the inactive colour
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    # Display button message
    smallText = pygame.font.Font("freesansbold.ttf", 20)
    textSurf, TextRect = text_objects(msg, smallText, black)
    # position the button message
    TextRect.center = (x + (w / 2), y + (h / 2))
    # add message to the screen
    gameDisplay.blit(textSurf, TextRect)