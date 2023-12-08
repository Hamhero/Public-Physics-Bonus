import pygame
import sys
import math
import numpy as np
from tkinter import Tk, filedialog
from moviepy.editor import VideoClip

# Initialize Pygame
pygame.init()

# Constants
FPS = 60
CANNON_LENGTH = 50
CANNONBALL_RADIUS = 10
GRAVITY = 0.5
COOLDOWN_TIME = 15
FLOOR_HEIGHT_RATIO = 1 / 20
WHITE = (255, 255, 255)
FONT_SIZE = 20
CANNON_BOTTOM_WIDTH = 30
CANNON_BOTTOM_HEIGHT = 15
ANGLE_BUTTON_WIDTH = 100
ANGLE_BUTTON_HEIGHT = 30
SPEED_BUTTON_WIDTH = 100
SPEED_BUTTON_HEIGHT = 30
GRAVITY_BUTTON_WIDTH = 100
GRAVITY_BUTTON_HEIGHT = 30
CLEAR_BUTTON_WIDTH = 100
CLEAR_BUTTON_HEIGHT = 30

# Set up the screen
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
pygame.display.set_caption("Cannon Game")
clock = pygame.time.Clock()
font = pygame.font.Font(None, FONT_SIZE)

# Cannon parameters
cannon_angle = 45
cannon_x = WIDTH // 4
cannon_y = HEIGHT - CANNONBALL_RADIUS - int(FLOOR_HEIGHT_RATIO * HEIGHT)

# Cannonball parameters
cannonball_speed = 10
cannonball_x = 0
cannonball_y = 0
cannonball_velocity_y = 0
cannonball_fired = False
cooldown_counter = 0

# HUD parameters
avg_velocity = 0
instant_velocity = 0
gravity = GRAVITY
timer = 0
displacement = 0
distance = 0
cannon_height = 0
cannonball_height = 0

# Recording parameters
recording = False
frame_list = []
video_filename = None

# Function to make frames for video recording
def make_frame(t):
    frame_index = int(t * FPS)
    if frame_index < len(frame_list):
        return np.transpose(frame_list[frame_index], (1, 0, 2))
    else:
        return np.transpose(frame_list[-1], (1, 0, 2))

# Function to show file dialog and save video
def save_video():
    global video_filename
    if frame_list:
        root = Tk()
        root.withdraw()  # Hide the main window
        video_filename = filedialog.asksaveasfilename(defaultextension=".avi",
                                                        filetypes=[("AVI files", "*.avi"), ("All files", "*.*")])
        root.destroy()  # Close the Tkinter window

        if video_filename:
            clip = VideoClip(make_frame, duration=len(frame_list) / FPS)
            clip.write_videofile(video_filename, fps=FPS, codec='mpeg4')
            print(f"Video saved at: {video_filename}")

# Function for input dialog
def input_dialog(message, initial_text):
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = pygame.font.Font(None, 32).render(initial_text, True, color)
    input_text = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return input_text
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                    text = pygame.font.Font(None, 32).render(input_text, True, color)

        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(text, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        clock.tick(30)

# Function for input dialog - angle adjustment
def input_dialog_angle(initial_text):
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = pygame.font.Font(None, 32).render(initial_text, True, color)
    input_text = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return input_text
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                    text = pygame.font.Font(None, 32).render(input_text, True, color)

        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(text, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        clock.tick(30)

# Function for input dialog - speed adjustment
def input_dialog_speed(initial_text):
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = pygame.font.Font(None, 32).render(initial_text, True, color)
    input_text = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return input_text
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                    text = pygame.font.Font(None, 32).render(input_text, True, color)

        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(text, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        clock.tick(30)

# Function for input dialog - gravity adjustment
def input_dialog_gravity(initial_text):
    input_box = pygame.Rect(100, 100, 140, 32)
    color_inactive = pygame.Color('lightskyblue3')
    color_active = pygame.Color('dodgerblue2')
    color = color_inactive
    active = False
    text = pygame.font.Font(None, 32).render(initial_text, True, color)
    input_text = ""

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return input_text
                    elif event.key == pygame.K_BACKSPACE:
                        input_text = input_text[:-1]
                    else:
                        input_text += event.unicode
                    text = pygame.font.Font(None, 32).render(input_text, True, color)

        screen.fill((30, 30, 30))
        pygame.draw.rect(screen, color, input_box, 2)
        screen.blit(text, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()
        clock.tick(30)


# Main game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not cannonball_fired and cooldown_counter == 0:
                cannonball_fired = True
                cannonball_x = cannon_x
                cannonball_y = cannon_y
                cannonball_velocity_y = -10
                cooldown_counter = COOLDOWN_TIME
            elif event.key == pygame.K_ESCAPE:
                if recording:
                    recording = False
                    save_video()  # Call the function to save the video
        elif event.type == pygame.VIDEORESIZE:
            WIDTH, HEIGHT = event.size
            screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.RESIZABLE)
            cannon_y = HEIGHT - CANNONBALL_RADIUS
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            # Check if the mouse click is within the record button
            if button_rect.collidepoint(event.pos):
                recording = not recording  # Toggle the recording state
                if recording:
                    frame_list = []  # Clear the frame list when starting a new recording
                else:
                    save_video()  # Call the function to save the video

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and cannon_angle < 90:
        cannon_angle += 1
    elif keys[pygame.K_RIGHT] and cannon_angle > 0:
        cannon_angle -= 1

    if cooldown_counter > 0:
        cooldown_counter -= 1

    if recording:
        frame = pygame.surfarray.array3d(screen.copy())  # Copy the screen surface to avoid overwriting
        frame_list.append(frame)

    if cannonball_fired:
        cannonball_x += cannonball_speed * math.cos(math.radians(cannon_angle))
        cannonball_y += cannonball_velocity_y
        cannonball_velocity_y += gravity

        if cannonball_y > HEIGHT - CANNONBALL_RADIUS:
            cannonball_y = HEIGHT - CANNONBALL_RADIUS
            cannonball_velocity_y = -cannonball_velocity_y * 0.8  # Bounce back up with damping

        if cannonball_x < 0 or cannonball_x > WIDTH or cannonball_y > HEIGHT:
            cannonball_fired = False

        avg_velocity = (cannonball_velocity_y + 10) / 2
        instant_velocity = cannonball_velocity_y

        displacement = cannonball_x - cannon_x
        distance = math.sqrt(displacement ** 2 + (HEIGHT - CANNONBALL_RADIUS - cannon_y) ** 2)

    cannon_height = HEIGHT - CANNONBALL_RADIUS - cannon_y

    screen.fill((0, 128, 128))

    # Draw the recording button
    button_rect = pygame.Rect(WIDTH - 110, 10, 100, 30)
    button_color = (0, 255, 0) if not recording else (255, 0, 0)
    pygame.draw.rect(screen, button_color, button_rect)
    button_text = font.render("Record", True, (255, 255, 255))
    screen.blit(button_text, (WIDTH - 100, 20))

    # Draw the angle adjustment button
    angle_button_rect = pygame.Rect(WIDTH - 110, 50, ANGLE_BUTTON_WIDTH, ANGLE_BUTTON_HEIGHT)
    pygame.draw.rect(screen, (0, 255, 0), angle_button_rect)
    angle_button_text = font.render("Adjust Angle", True, (255, 255, 255))
    screen.blit(angle_button_text, (WIDTH - 100, 60))

    # Draw the speed adjustment button
    speed_button_rect = pygame.Rect(WIDTH - 110, 90, SPEED_BUTTON_WIDTH, SPEED_BUTTON_HEIGHT)
    pygame.draw.rect(screen, (255, 255, 0), speed_button_rect)
    speed_button_text = font.render("Adjust Speed", True, (0, 0, 0))
    screen.blit(speed_button_text, (WIDTH - 100, 100))

    # Draw the gravity adjustment button
    gravity_button_rect = pygame.Rect(WIDTH - 110, 130, GRAVITY_BUTTON_WIDTH, GRAVITY_BUTTON_HEIGHT)
    pygame.draw.rect(screen, (0, 0, 255), gravity_button_rect)
    gravity_button_text = font.render("Adjust Gravity", True, (255, 255, 255))
    screen.blit(gravity_button_text, (WIDTH - 100, 140))

    # Draw the clear button
    clear_button_rect = pygame.Rect(WIDTH - 110, 170, CLEAR_BUTTON_WIDTH, CLEAR_BUTTON_HEIGHT)
    pygame.draw.rect(screen, (255, 0, 0), clear_button_rect)
    clear_button_text = font.render("Clear", True, (255, 255, 255))
    screen.blit(clear_button_text, (WIDTH - 100, 180))

    # Draw the cannon and cannonball
    pygame.draw.arc(screen, (0, 0, 0), (cannon_x - CANNON_BOTTOM_WIDTH // 2, cannon_y - CANNON_BOTTOM_HEIGHT,
                                       CANNON_BOTTOM_WIDTH, CANNON_BOTTOM_HEIGHT * 2), 0, math.pi, 5)
    cannon_end_x = cannon_x + CANNON_LENGTH * math.cos(math.radians(cannon_angle))
    cannon_end_y = cannon_y - CANNON_LENGTH * math.sin(math.radians(cannon_angle))
    pygame.draw.line(screen, (0, 0, 0), (cannon_x, cannon_y), (cannon_end_x, cannon_end_y), 5)

    if cannonball_fired:
        pygame.draw.circle(screen, (169, 169, 169), (int(cannonball_x), int(cannonball_y)), CANNONBALL_RADIUS)

    # Draw the floor
    pygame.draw.rect(screen, (255, 255, 0), (0, HEIGHT - CANNONBALL_RADIUS, WIDTH, CANNONBALL_RADIUS))

        # Handle button clicks
    mouse_x, mouse_y = pygame.mouse.get_pos()
    
    if button_rect.collidepoint(mouse_x, mouse_y) and event.type == pygame.MOUSEBUTTONDOWN:
        recording = not recording
        if recording:
            frame_list = []  # Clear the frame list when starting a new recording
        else:
            save_video()  # Call the function to save the video

    if angle_button_rect.collidepoint(mouse_x, mouse_y) and event.type == pygame.MOUSEBUTTONDOWN:
        input_text = input_dialog_angle(f'Adjust Angle: {cannon_angle}')
        try:
            cannon_angle = int(input_text)
        except ValueError:
            pass

    if speed_button_rect.collidepoint(mouse_x, mouse_y) and event.type == pygame.MOUSEBUTTONDOWN:
        input_text = input_dialog_speed(f'Adjust Speed: {cannonball_speed}')
        try:
            cannonball_speed = int(input_text)
        except ValueError:
            pass

    if gravity_button_rect.collidepoint(mouse_x, mouse_y) and event.type == pygame.MOUSEBUTTONDOWN:
        input_text = input_dialog_gravity(f'Adjust Gravity: {gravity}')
        try:
            gravity = float(input_text)
        except ValueError:
            pass

    if clear_button_rect.collidepoint(mouse_x, mouse_y) and event.type == pygame.MOUSEBUTTONDOWN:
        cannonball_fired = False  # Reset cannonball state

    # Draw the HUD text
    text_y = 10
    text_gap = 20

    text_render = font.render(f'Avg Velocity: {avg_velocity:.2f} m/s', True, (255, 255, 255))
    screen.blit(text_render, (10, text_y))
    text_y += text_gap

    text_render = font.render(f'Instant Velocity: {instant_velocity:.2f} m/s', True, (255, 255, 255))
    screen.blit(text_render, (10, text_y))
    text_y += text_gap

    text_render = font.render(f'Gravity: {gravity} m/s^2', True, (255, 255, 255))
    screen.blit(text_render, (10, text_y))
    text_y += text_gap

    text_render = font.render(f'Timer: {timer:.2f} s', True, (255, 255, 255))
    screen.blit(text_render, (10, text_y))
    text_y += text_gap

    text_render = font.render(f'Displacement: {displacement:.2f} m', True, (255, 255, 255))
    screen.blit(text_render, (10, text_y))
    text_y += text_gap

    text_render = font.render(f'Distance: {distance:.2f} m', True, (255, 255, 255))
    screen.blit(text_render, (10, text_y))
    text_y += text_gap

    text_render = font.render(f'Cannon Height: {cannon_height:.2f} m', True, (255, 255, 255))
    screen.blit(text_render, (10, text_y))
    text_y += text_gap

    text_render = font.render(f'Cannonball Height: {HEIGHT - CANNONBALL_RADIUS - cannonball_y:.2f} m', True,
                              (255, 255, 255))
    screen.blit(text_render, (10, text_y))

    pygame.display.flip()
    clock.tick(FPS)