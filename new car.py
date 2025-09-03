import pygame
import os

pygame.init()

# --- Setup for Relative Paths ---
script_dir = os.path.dirname(os.path.abspath(__file__))
assets_dir = os.path.join(script_dir, 'assets')

def load_image(file_name):
    return pygame.image.load(os.path.join(assets_dir, file_name))

# --- Game Variables ---
Menu = 'Main Menu'
status = True
Mode=''
Map=''
cars=[]
car_index=0
Right = False
Left = False
Angle = 100
infoObject = pygame.display.Info()
screen_width = infoObject.current_w
screen_height = infoObject.current_h
scrn = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
Menu_Visited=[]
laps=3
clock=pygame.time.Clock()
set=False
start_time =0
complete = True
write=False

# --- Loading all the images ---
img = load_image('speed_8252022_layout_14.jpg').convert()
img = pygame.transform.scale(img, (screen_width, screen_height))
title = load_image('title.png').convert()
startf_img = load_image('finish-flag.png').convert()
startf_img = pygame.transform.scale(startf_img, (100, 100))
compt_img = load_image('compt.png').convert()
arct_img = load_image('arct.png').convert()
buttonb_img = load_image('back button.png').convert()
buttonb_img = pygame.transform.scale(buttonb_img,(200,100))
mapt = load_image('mapt.png').convert()
car_select_text = load_image('car select.png').convert()
arrow_right_img = load_image('right-arrow_3058545.png')
arrow_left_img = load_image('right-arrow_3058545.png')
arrow_left_img = pygame.transform.rotate(arrow_left_img,180)
Track1_Game = load_image('track 1.png')
Track1_Game = pygame.transform.scale(Track1_Game,(900,900))
Track1_thumb = pygame.transform.scale(Track1_Game,(200,200))
Track2_Game = load_image('track 2.png')
Track2_Game = pygame.transform.scale(Track2_Game,(900,900))
Track2_thumb = pygame.transform.scale(Track2_Game,(200,200))
Track3_Game = load_image('track 3.png')
Track3_Game = pygame.transform.scale(Track3_Game,(900,900))
Track3_thumb = pygame.transform.scale(Track3_Game,(200,200))
Track_Text = pygame.font.SysFont('comicsansms',26)
Track1_Text=Track_Text.render('Track 1',False,(255,255,255))
Track2_Text=Track_Text.render('Track 2',False,(255,255,255))
Track3_Text=Track_Text.render('Track 3',False,(255,255,255))
finish_line_img = load_image('finish line.jpeg')
finish_line_img = pygame.transform.scale(finish_line_img,(10, 80))
finish_line_img = pygame.transform.rotate(finish_line_img,90)
Car1_base_img = load_image('car.png')
Car2_base_img = load_image('car2.png')
Car3_base_img = load_image('car3.png')
up_arrow_img = load_image('up arrow.png')
up_arrow_img = pygame.transform.scale(up_arrow_img,(20,20))
down_arrow_img = pygame.transform.rotate(up_arrow_img,180)
leaderboard = load_image('leader board font.png').convert()
black_rect_img = load_image('black rect.png')


class Button():
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos, self.y_pos = pos[0], pos[1]
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos)) if self.image else self.text.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
    def update(self, screen):
        if self.image: screen.blit(self.image, self.rect)
        screen.blit(self.text, self.text_rect)
    def checkForInput(self, position):
        return self.rect.collidepoint(position)
    def changeColor(self, position):
        color = self.hovering_color if self.rect.collidepoint(position) else self.base_color
        self.text = self.font.render(self.text_input, True, color)

screen_center_x, screen_center_y = scrn.get_rect().center
startf = Button(startf_img, [screen_center_x, screen_center_y + 50], '.', pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
compt = Button(compt_img, [screen_center_x, screen_center_y], '.', pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
arct = Button(arct_img, [screen_center_x, screen_center_y - 100], '.', pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
buttonb=Button(buttonb_img, [150, screen_height - 100], '.', pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
Track1= Button(Track1_thumb,[screen_center_x - screen_width // 4, screen_center_y - 50],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
Track2=Button(Track2_thumb,[screen_center_x, screen_center_y - 50],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
Track3=Button(Track3_thumb,[screen_center_x + screen_width // 4, screen_center_y - 50],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
arrow_right=Button(arrow_right_img,[screen_center_x + 400, screen_center_y],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
arrow_left=Button(arrow_left_img,[screen_center_x - 400, screen_center_y],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
Attributes_button=Button(black_rect_img,[screen_center_x, screen_center_y + 100],'Change The Attributes',pygame.font.SysFont("comicsansms", 20), 'White', 'Blue')
Select_car_button=Button(black_rect_img,[screen_center_x, screen_center_y + 200],'Select Car',pygame.font.SysFont("comicsansms", 20), 'White', 'Blue')
power_up_arrow=Button(up_arrow_img,[screen_center_x + 100,200],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
power_down_arrow=Button(down_arrow_img,[screen_center_x + 100,225],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
weight_up_arrow=Button(up_arrow_img,[screen_center_x + 100,250],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
weight_down_arrow=Button(down_arrow_img,[screen_center_x + 100,275],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
breaks_up_arrow=Button(up_arrow_img,[screen_center_x + 100,300],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
breaks_down_arrow=Button(down_arrow_img,[screen_center_x + 100,325],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
tyre_up_arrow=Button(up_arrow_img,[screen_center_x + 100,350],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
tyre_down_arrow=Button(down_arrow_img,[screen_center_x + 100,375],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
leader_board_button=Button(black_rect_img,[screen_center_x - 150, screen_center_y+100],'Leader Board',pygame.font.SysFont("comicsansms", 20), 'White', 'Blue')
Home_button=Button(black_rect_img,[screen_center_x + 150, screen_center_y + 100],'Home',pygame.font.SysFont("comicsansms", 20), 'White', 'Blue')

class Car:
    def __init__(self,img,weight,power,tyrehealth,breaks,x,y):
        self.base_img = img
        self.img = pygame.transform.scale(self.base_img,(60,30))
        self.weight=weight
        self.power=power
        self.tyrehealth=tyrehealth
        self.breaks=breaks
        self.speed = 12 * (self.power/100) * (self.tyrehealth/100) * ((100-self.weight)/100)
        self.x, self.y = x, y
        self.rect = self.img.get_rect(center=(self.x, self.y))
    def set_x(self, x): self.x = x; self.rect.centerx = self.x
    def set_y(self, y): self.y = y; self.rect.centery = self.y
    def get_power(self): return self.power
    def set_power(self,power): self.power=power
    def get_tyrehealth(self): return self.tyrehealth
    def set_tyrehealth(self,tyrehealth): self.tyrehealth=tyrehealth
    def get_weight(self): return self.weight
    def set_weight(self,weight): self.weight=weight
    def get_breaks(self): return self.breaks
    def set_breaks(self,breaks): self.breaks=breaks
    def output(self,scrn): scrn.blit(self.img, self.rect)

    def Move_Forward(self):
        if Angle == 100: self.rect.move_ip(self.speed,0)
        elif Angle == 190: self.rect.move_ip(0,self.speed)
        elif Angle == 10: self.rect.move_ip(0,-self.speed)
        elif Angle == 280: self.rect.move_ip(-self.speed,0)
        elif Angle == 370: self.rect.move_ip(0,-self.speed)
        elif Angle == -80: self.rect.move_ip(-self.speed,0)
        elif Angle == -170: self.rect.move_ip(0,self.speed)

    def Move_Backwards(self):
        reverse_speed = self.speed * 0.4
        if Angle == 100: self.rect.move_ip(-reverse_speed, 0)
        elif Angle == 190: self.rect.move_ip(0, -reverse_speed)
        elif Angle == 10: self.rect.move_ip(0, reverse_speed)
        elif Angle == 280: self.rect.move_ip(reverse_speed, 0)
        elif Angle == 370: self.rect.move_ip(0, reverse_speed)
        elif Angle == -80: self.rect.move_ip(reverse_speed, 0)
        elif Angle == -170: self.rect.move_ip(0, -reverse_speed)

    def Move_Right(self):
        global Right, Angle
        if not Right and Angle < 370:
            self.img = pygame.transform.rotate(self.img, -90)
            Right, Angle = True, Angle + 90
        turn_speed = 12 * (self.power/100) * ((100-self.weight)/100) * (self.breaks/100)
        self.rect.move_ip(0, turn_speed)

    def Move_Left(self):
        global Left, Angle
        if not Left and Angle > -160:
            self.img = pygame.transform.rotate(self.img, 90)
            Left, Angle = True, Angle - 90
        turn_speed = 12 * (self.power/100) * ((100-self.weight)/100) * (self.breaks/100)
        self.rect.move_ip(0, -turn_speed)

Car1=Car(Car1_base_img,20,50,100,20,screen_center_x,screen_center_y)
cars.append(Car1)
Car2=Car(Car2_base_img,20,50,100,20,screen_center_x,screen_center_y)
cars.append(Car2)
Car3=Car(Car3_base_img,20,50,100,20, screen_center_x,screen_center_y)
cars.append(Car3)

def mergeSort(arr):
    if len(arr) <= 1: return arr
    mid = len(arr) // 2
    return merge(mergeSort(arr[:mid]), mergeSort(arr[mid:]))
def merge(left, right):
    merged, i, j = [], 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]: merged.append(left[i]); i += 1
        else: merged.append(right[j]); j += 1
    merged.extend(left[i:]); merged.extend(right[j:])
    return merged

def main_menu(img, title, startf, scrn):
    scrn.blit(img, (0, 0)); scrn.blit(title, title.get_rect(center=(screen_center_x, screen_center_y - 150))); startf.update(scrn)
def mode_select(img, scrn, compt, arct):
    scrn.blit(img, (0, 0)); compt.update(scrn); arct.update(scrn); buttonb.update(scrn)
def map_select(img,scrn,mapt,Track1_Text,Track2_Text,Track3_Text):
    scrn.blit(img,(0,0)); scrn.blit(mapt, mapt.get_rect(center=(screen_center_x, 50)))
    buttonb.update(scrn); Track1.update(scrn); Track2.update(scrn); Track3.update(scrn)
    scrn.blit(Track1_Text, Track1_Text.get_rect(center=(Track1.x_pos, Track1.y_pos + 150)))
    scrn.blit(Track2_Text, Track2_Text.get_rect(center=(Track2.x_pos, Track2.y_pos + 150)))
    scrn.blit(Track3_Text, Track3_Text.get_rect(center=(Track3.x_pos, Track3.y_pos + 150)))
def car_select(img,scrn,car_select_text,arrow_right,arrow_left,car,buttonb,attributes_button,select_car):
    scrn.blit(img,(0,0)); scrn.blit(car_select_text, car_select_text.get_rect(center=(screen_center_x, 50)))
    arrow_right.update(scrn); arrow_left.update(scrn); car.output(scrn)
    buttonb.update(scrn); attributes_button.update(scrn); select_car.update(scrn)
def attributes_menu(car):
    total = sum([car.get_power(), car.get_weight(), car.get_breaks(), car.get_tyrehealth()])
    remaining = 200 - total
    pygame.draw.rect(scrn,[0,0,0],[screen_center_x - 300, 50, 600, 600],0)
    font=pygame.font.SysFont('comicsansms',16); text_x = screen_center_x - 100
    scrn.blit(font.render(f'Power {car.get_power()}',0,(255,255,255)),(text_x,200))
    scrn.blit(font.render(f'Weight {car.get_weight()}',0,(255,255,255)),(text_x,250))
    scrn.blit(font.render(f'Breaks {car.get_breaks()}',0,(255,255,255)),(text_x,300))
    scrn.blit(font.render(f'Tyre Health {car.get_tyrehealth()}',0,(255,255,255)),(text_x,350))
    scrn.blit(font.render(f'Remaining Skill Points {remaining}',0,(255,255,255)),(text_x,100))
    power_up_arrow.update(scrn); power_down_arrow.update(scrn); weight_up_arrow.update(scrn)
    weight_down_arrow.update(scrn); breaks_up_arrow.update(scrn); breaks_down_arrow.update(scrn)
    tyre_up_arrow.update(scrn); tyre_down_arrow.update(scrn); Select_car_button.update(scrn)

def game(Map, car):
    global Menu, set, start_time, laps, complete, time
    map_display_size = 900
    map_x = screen_center_x - map_display_size // 2
    map_y = screen_center_y - map_display_size // 2
    current_finish_line = None

    scrn.fill((0, 128, 0))

    if Map == 'Track 1':
        scrn.blit(Track1_Game,(map_x, map_y))
        if not set:
            car.set_x(map_x + 500); car.set_y(map_y + 150)
            set, start_time = True, pygame.time.get_ticks()
        current_finish_line = Button(pygame.transform.rotate(finish_line_img,90), [map_x + 550, map_y + 130], '.', pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
    elif Map == 'Track 2':
        scrn.blit(Track2_Game,(map_x, map_y))
        if not set:
            car.set_x(map_x + 450); car.set_y(map_y + 700)
            set, start_time = True, pygame.time.get_ticks()
        horizontal_finish_line = pygame.transform.rotate(finish_line_img, 90)
        current_finish_line = Button(horizontal_finish_line, [map_x + 450, map_y + 700], '.', pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
    elif Map == 'Track 3':
        scrn.blit(Track3_Game,(map_x, map_y))
        if not set:
            car.set_x(map_x + 450); car.set_y(map_y + 750)
            set, start_time = True, pygame.time.get_ticks()
        horizontal_finish_line = pygame.transform.rotate(finish_line_img, 90)
        current_finish_line = Button(horizontal_finish_line, [map_x + 450, map_y + 750], '.', pygame.font.SysFont("comicsansms", 1), 'Black', 'White')

    if current_finish_line: current_finish_line.update(scrn)
    car.output(scrn)

    font=pygame.font.SysFont('comicsansms',26)
    time=(pygame.time.get_ticks() - start_time)/1000
    pygame.draw.rect(scrn, (200, 200, 200), [0, 0, screen_width, 40])
    scrn.blit(font.render(f"Time: {time:.2f}",0,(0,0,0)),(screen_center_x - 200, 10))
    scrn.blit(font.render(f"Laps: {laps}/3",0,(0,0,0)),(screen_center_x, 10))
    scrn.blit(font.render(f'Tyre health {car.get_tyrehealth()}',0,(0,0,0)),(screen_center_x + 200, 10))

    if current_finish_line and current_finish_line.rect.colliderect(car.rect):
        if laps > 0 and complete: laps, complete = laps - 1, False
        elif laps == 0: Menu = 'Result'
    if current_finish_line and not current_finish_line.rect.colliderect(car.rect): complete = True

def result(time):
    font=pygame.font.SysFont('comicsansms',26)
    result_text=font.render(f'Time {time:.2f} Seconds',False,(255,255,255))
    scrn.blit(result_text,result_text.get_rect(center=(screen_center_x, screen_center_y - 50)))
    leader_board_button.update(scrn); Home_button.update(scrn)
def Leader_board(list_data):
    scrn.blit(leaderboard, leaderboard.get_rect(center=(screen_center_x, 50)))
    font=pygame.font.SysFont('comicsansms',26)
    for i, score in enumerate(list_data[:10]):
        text = font.render(f"{i+1}: {score:.2f} Seconds",False,(255,255,255))
        scrn.blit(text, text.get_rect(center=(screen_center_x, screen_center_y - 200 + (i*50))))
    Home_button.update(scrn)
def add_and_sort(map_name):
    global write, list, time
    file_path = os.path.join(script_dir, f'{map_name}.txt')
    try:
        with open(file_path, 'a') as f: f.write(f"{time}\n")
        with open(file_path, 'r') as f: list = [float(line) for line in f]
        list=mergeSort(list)
    except (FileNotFoundError, ValueError): list = [time]
    write = True

# --- MAIN GAME LOOP ---
while status:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            status = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if Menu == 'Main Menu' and startf.checkForInput(mouse_pos): Menu, Menu_Visited = 'Mode Select', ['Main Menu']
            elif Menu == 'Mode Select':
                if compt.checkForInput(mouse_pos): Menu, Mode, Menu_Visited = 'Map Select', 'comp', Menu_Visited + ['Mode Select']
                elif arct.checkForInput(mouse_pos): Menu, Mode, Menu_Visited = 'Map Select', 'arc', Menu_Visited + ['Mode Select']
            elif buttonb.checkForInput(mouse_pos) and Menu_Visited: Menu = Menu_Visited.pop()
            elif Menu == 'Map Select':
                if Track1.checkForInput(mouse_pos): Map, Menu, Menu_Visited = 'Track 1', 'Car Select', Menu_Visited + ['Map Select']
                elif Track2.checkForInput(mouse_pos): Map, Menu, Menu_Visited = 'Track 2', 'Car Select', Menu_Visited + ['Map Select']
                elif Track3.checkForInput(mouse_pos): Map, Menu, Menu_Visited = 'Track 3', 'Car Select', Menu_Visited + ['Map Select']
            elif Menu == 'Car Select':
                if arrow_right.checkForInput(mouse_pos) and car_index < len(cars) - 1: car_index += 1
                elif arrow_left.checkForInput(mouse_pos) and car_index > 0: car_index -= 1
                elif Attributes_button.checkForInput(mouse_pos): Menu = 'Attributes'
                elif Select_car_button.checkForInput(mouse_pos):
                    car = cars[car_index]; Menu, Menu_Visited = 'Game', Menu_Visited + ['Car Select']
                    set, laps, write = False, 3, False
            elif Menu == 'Attributes':
                current_car = cars[car_index]
                total_attrs = sum([current_car.get_power(), current_car.get_weight(), current_car.get_breaks(), current_car.get_tyrehealth()])
                if power_up_arrow.checkForInput(mouse_pos) and (200 - total_attrs) >= 5:
                    current_car.set_power(current_car.get_power() + 5)
                elif power_down_arrow.checkForInput(mouse_pos) and current_car.get_power() >= 5:
                    current_car.set_power(current_car.get_power() - 5)
                elif weight_up_arrow.checkForInput(mouse_pos) and (200 - total_attrs) >= 5:
                    current_car.set_weight(current_car.get_weight() + 5)
                elif weight_down_arrow.checkForInput(mouse_pos) and current_car.get_weight() >= 5:
                    current_car.set_weight(current_car.get_weight() - 5)
                elif breaks_up_arrow.checkForInput(mouse_pos) and (200 - total_attrs) >= 5:
                    current_car.set_breaks(current_car.get_breaks() + 5)
                elif breaks_down_arrow.checkForInput(mouse_pos) and current_car.get_breaks() >= 5:
                    current_car.set_breaks(current_car.get_breaks() - 5)
                elif tyre_up_arrow.checkForInput(mouse_pos) and (200 - total_attrs) >= 5:
                    current_car.set_tyrehealth(current_car.get_tyrehealth() + 5)
                elif tyre_down_arrow.checkForInput(mouse_pos) and current_car.get_tyrehealth() >= 5:
                    current_car.set_tyrehealth(current_car.get_tyrehealth() - 5)
                elif Select_car_button.checkForInput(mouse_pos):
                    car = cars[car_index]; Menu, Menu_Visited = 'Game', Menu_Visited + ['Car Select']
                    set, laps, write = False, 3, False
            elif (Menu == 'Result' or Menu == 'Leader Board'):
                if Home_button.checkForInput(mouse_pos):
                    Menu, Menu_Visited = 'Main Menu', []
                    for car_obj in cars:
                        car_obj.set_x(screen_center_x)
                        car_obj.set_y(screen_center_y)
                if Menu == 'Result' and leader_board_button.checkForInput(mouse_pos): Menu = 'Leader Board'

    if Menu == 'Game':
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]: car.Move_Forward(); Right, Left = False, False
        elif keys[pygame.K_s]: car.Move_Backwards(); Right, Left = False, False
        elif keys[pygame.K_d]: car.Move_Right(); Right, Left = True, False
        elif keys[pygame.K_a]: car.Move_Left(); Right, Left = False, True

    scrn.fill((0,0,0))
    if Menu == 'Main Menu': main_menu(img, title, startf, scrn)
    elif Menu == 'Mode Select': mode_select(img, scrn, compt, arct)
    elif Menu == 'Map Select': map_select(img,scrn,mapt,Track1_Text,Track2_Text,Track3_Text)
    elif Menu == 'Car Select': car_select(img,scrn,car_select_text,arrow_right,arrow_left,cars[car_index],buttonb,Attributes_button,Select_car_button)
    elif Menu == 'Attributes': attributes_menu(cars[car_index])
    elif Menu == 'Game': game(Map,car)
    elif Menu == 'Result':
        result(time)
        if not write: add_and_sort(Map)
    elif Menu == 'Leader Board':
        Leader_board(list if 'list' in locals() else [])

    pygame.display.flip()

pygame.quit()