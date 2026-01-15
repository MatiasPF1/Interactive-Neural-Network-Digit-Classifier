import numpy as np
import pygame


                                    # Complete Game
def run_drawer():
    # Screen Dimensions 
    GRID_SIZE = 28          # 28x28 grid
    PIXEL_SIZE = 20         # each logical cell is drawn as a 20×20 block of actual screen pixels.
    WINDOW_SIZE = GRID_SIZE * PIXEL_SIZE # 28 * 20 = 560: 560×560 Visual Screen

    
    # Screen  Colors 
    WHITE = (255, 255, 255) #White pixels
    BLACK = (0, 0, 0) #Complete black Pixels
    DRAW_COLOR = WHITE  #White pixels drawn(0)
    BG_COLOR = BLACK #Black Background of Canvas(255)

    
    # Initialization: Game Loop
    pygame.init() #Initialization
    screen = pygame.display.set_mode((WINDOW_SIZE, WINDOW_SIZE)) #Dimension of the windows screened 
    pygame.display.set_caption("28x28 Digit Drawer") #Caption
    screen.fill(BG_COLOR) #Screen gets Filled with the Back Ground Color

    
    # Initialization: Screen 
    grid = np.zeros((GRID_SIZE, GRID_SIZE), dtype=np.uint8) #each pixel value is 8-bit integer (0–255): (0 = white, 255 = black)
    

    # Game Setup: It Runs? , It's Drawing?, Drawing Hisotry to erase later
    running = True
    drawing = False
    history = []

    
    # Main Loop Setup: Drawing Action, Quit and Screen.
    while running:
        for event in pygame.event.get(): #For all event that occur: mouse, keyboard, window actions
            if event.type == pygame.QUIT:    #Game Finishes 
                running = False          

            elif event.type == pygame.MOUSEBUTTONDOWN:   #If clicked: Drawing occurs
                drawing = True

            elif event.type == pygame.MOUSEBUTTONUP:    #If stop clicking: Drawing stops 
                drawing = False

            elif event.type == pygame.KEYDOWN:           #If key is pressed
                if event.key == pygame.K_RETURN:        #Press Enter to finish drawing
                    running = False
                elif event.key == pygame.K_z:           #Z key for undo
                    if history:                          #Check if there is something to undo
                        last_row, last_col = history.pop()  #Remove last drawn pixel from history
                        grid[last_row, last_col] = 0        #Erase it

        #-------------------------
        # Handling Drawing  
        #-------------------------
        if drawing:
            x, y = pygame.mouse.get_pos()    # Gets mouse coordinates in *physical* screen pixels (0–559)
            row = y // PIXEL_SIZE # Convert Y from 0–559 → 0–27 (grid row index)
            col = x // PIXEL_SIZE # Convert X from 0–559 → 0–27 (grid column index)
            if grid[row, col] == 0:         # Only draw if the pixel is currently off
                grid[row, col] = 255        # Mark the logical grid pixel as “on” (white)
                history.append((row, col))  # Save the action to history for undo

        #-------------------------
        # Handling Screen
        #-------------------------
        for row in range(GRID_SIZE): #Looping over rows
            for col in range(GRID_SIZE): #Looping over Collumns 
                color = DRAW_COLOR if grid[row, col] > 0 else BG_COLOR #if is 0, then color is black. if color>0, then is white.
                pygame.draw.rect(screen, color,(col * PIXEL_SIZE, row * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)) #Draw the filled square (logical pixel) at its physical location on screen

                #Draw grid lines
                pygame.draw.rect(screen, (200, 200, 200),
                                     (col * PIXEL_SIZE, row * PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE), 1) #Draw a thin grid line around this square (gray color, width=1 pixel)

        pygame.display.flip()

    pygame.quit()
    return grid

