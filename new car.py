import pygame 
pygame.init()
Menu = 'Main Menu'
# stores the current menu
status = True
# if True then the game will run
Mode=''
#stores the game mode that the user has selected
Map=''
# stores the map that the user has selected
cars=[]
# stores all of the cars in an array so that it is easy to access and cycle through them
car_index=0
# this stores the index for the cars list. This is used when traversing through the list
Right = False
Left = False
Angle = 100
scrn = pygame.display.set_mode((0,0))
#creates a display which i can output my game
Menu_Visited=[]
#stores the order in which menus they have visited so that they can go to the previous menu
laps=0
# stores the amount of laps
clock=pygame.time.Clock()
clock.tick(60)
# sets a certain framerate 
set=False
# boolean value for setting the car in the right position
start_time =0
# stores the start time of the game
laps=3
complete = True
# determines if they have completed a lap
write=False
# determines if the file has been appended
# storing all the images as variables 
img = pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\speed_8252022_layout_14.jpg').convert()
title = pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\title.png').convert()
startf = pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\finish-flag.png').convert()
startf = pygame.transform.scale(startf, (100, 100))
compt = pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\compt.png').convert()
arct = pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\arct.png').convert()
buttonb=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\back button.png').convert()
buttonb=pygame.transform.scale(buttonb,(200,100))
mapt=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\mapt.png').convert()
car_select_text=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\car select.png').convert()
arrow_right=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\right-arrow_3058545.png')
arrow_left=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\right-arrow_3058545.png')
arrow_left=pygame.transform.rotate(arrow_left,180)
Track1=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\track 1.png')
Track1_Game=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\track 1.png')
Track1_Game=pygame.transform.scale(Track1_Game,(700,700))
Track1=pygame.transform.scale(Track1,(200,200))
Track2=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\track 2.png')
Track2_Game=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\track 2.png')
Track2_Game=pygame.transform.scale(Track2_Game,(700,700))
Track2=pygame.transform.scale(Track2,(200,200))
Track3=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\track 3.png')
Track3_Game=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\track 3.png')
Track3_Game=pygame.transform.scale(Track3_Game,(700,700))
Track3=pygame.transform.scale(Track3,(200,200))
Track_Text = pygame.font.SysFont('comicsansms',26)
# creates the text format for labelling the different tracks
Track1_Text=Track_Text.render('Track 1',False,(255,255,255))
Track2_Text=Track_Text.render('Track 2',False,(255,255,255))
Track3_Text=Track_Text.render('Track 3',False,(255,255,255))
# creates the actual text of the labelling of the different maps
# this loads all of the images and resizes them to the correct size
finish_line=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\finish line.jpeg')
finish_line=pygame.transform.scale(finish_line,(100,100))
finish_line=pygame.transform.rotate(finish_line,90)
finish_line2=finish_line
Car1=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\car.png')

up_arrow=pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\up arrow.png')
# loads the up arrow for the attributes
up_arrow=pygame.transform.scale(up_arrow,(20,20))
# sets it to the right size
down_arrow=pygame.transform.rotate(up_arrow,180)
# flips the up arrow to make the down arrow
leaderboard= pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\leader board font.png').convert()

class Button():
# creates buttons that the user can interact with
    def __init__(self, image, pos, text_input, font, base_color, hovering_color):
        self.image = image
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        #sets the x and y coordinates of the button
        self.font = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = self.font.render(self.text_input, True, self.base_color)
        if self.image is None:# if no image is given it creates the button out of the text instead
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))
# defines all of the attributes of my button class
    def update(self, screen):
        if self.image is not None:
        # if the button has an image it will output the image
            screen.blit(self.image, self.rect)
        # if it doesnt have an image it will output the text
        screen.blit(self.text, self.text_rect)
# outputs the button onto the screen
    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            return True
        return False
#checks if the user has clicked on the button by checking if the mouse is on the button
    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top, self.rect.bottom):
            self.text = self.font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = self.font.render(self.text_input, True, self.base_color)
#changes the text if you are hovering over the button
startf = Button(startf, [scrn.get_rect().centerx, scrn.get_rect().centery], '.', pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
compt = Button(compt, [scrn.get_rect().centerx, scrn.get_rect().centery+100], '.', pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
arct = Button(arct, [scrn.get_rect().centerx, scrn.get_rect().centery-100], '.', pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
buttonb=Button(buttonb, [150,620], '.', pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
Track1= Button(Track1,[200,300],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
Track2=Button(Track2,[500,300],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
Track3=Button(Track3,[800,300],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
arrow_right=Button(arrow_right,[scrn.get_rect().centerx+400,scrn.get_rect().centery],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
arrow_left=Button(arrow_left,[scrn.get_rect().centerx-400,scrn.get_rect().centery],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
Attributes_button=Button(pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\black rect.png'),[scrn.get_rect().centerx,scrn.get_rect().centery+100],'Change The Attributes',pygame.font.SysFont("comicsansms", 20), 'White', 'Blue')
Select_car_button=Button(pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\black rect.png'),[scrn.get_rect().centerx,scrn.get_rect().centery+300],'Select Car',pygame.font.SysFont("comicsansms", 20), 'White', 'Blue')
finish_line=Button(finish_line,[700,250],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
power_up_arrow=Button(up_arrow,[scrn.get_rect().centerx,200],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
power_down_arrow=Button(down_arrow,[scrn.get_rect().centerx,225],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
weight_up_arrow=Button(up_arrow,[scrn.get_rect().centerx,250],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
weight_down_arrow=Button(down_arrow,[scrn.get_rect().centerx,275],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
breaks_up_arrow=Button(up_arrow,[scrn.get_rect().centerx,300],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
breaks_down_arrow=Button(down_arrow,[scrn.get_rect().centerx,325],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
tyre_up_arrow=Button(up_arrow,[scrn.get_rect().centerx+50,350],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
tyre_down_arrow=Button(down_arrow,[scrn.get_rect().centerx+50,375],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
leader_board_button=Button(pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\black rect.png'),[scrn.get_rect().centerx,scrn.get_rect().centery+300],'Leader Board',pygame.font.SysFont("comicsansms", 20), 'White', 'Blue')
Home_button=Button(pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\black rect.png'),[scrn.get_rect().centerx-300,scrn.get_rect().centery+300],'Home',pygame.font.SysFont("comicsansms", 20), 'White', 'Blue')
# creating and storing all of the buttons


class Car:
    def __init__(self,img,weight,power,tyrehealth,breaks,x,y):
        self.img=img
        self.img=pygame.transform.scale(self.img,(100,50))
        self.weight=weight
        self.power=power
        self.tyrehealth=tyrehealth
        self.breaks=breaks
        self.speed=50*(self.power/100)*(self.tyrehealth/100)*((100-self.weight)/100)
        self.x=x
        self.y=y
        self.rect = self.img.get_rect(center=(self.x, self.y))
        # defines all of the attributes 
    def get_x(self):
        return self.x
    # returns the x coordinate of the car
    def get_y(self):
        return self.y 
    # returns the y coordinate of the car
    def set_x(self,x):
        self.x=x
    # sets a new x coordinate of the car
        self.rect = self.img.get_rect(center=(self.x, self.y))
        # creates a new rect at the coordinates
    def set_y(self,y):
        self.y=y
        # sets a new y coordinate for the car
        self.rect = self.img.get_rect(center=(self.x, self.y))
        # creates a new rect at that coordinate 
    def get_power(self):
        return self.power
    # returns the power of the car
    def set_power(self,power):
        self.power=power
    # sets a new power of the car
    def get_tyrehealth(self):
        return self.tyrehealth
# returns the tyrehealth of the car
    def set_tyrehealth(self,tyrehealth):
        self.tyrehealth=tyrehealth
    # sets a new tyrehealth of the car
    def get_weight(self):
        return self.weight
    # returns the weight of the car
    def set_weight(self,weight):
        self.weight=weight
        # sets a new weight for the car
    def get_breaks(self):
        return self.breaks
    # returns the breaks of the car
    def set_breaks(self,breaks):
        self.breaks=breaks#
    # sets new breaks for the car

    def output(self,scrn):
        scrn.blit(self.img,self.rect)
        # outputs the car
        pygame.display.update()
    def Move_Forward(self,scrn):
        scrn.fill((0,255,0))
        # changes the background to green to resemble grass
        if Angle == 100:
            # angle is used to determine which way the car is facing. The car will then move according.
             self.rect.move_ip(self.speed,0)
        if Angle == 190:
             self.rect.move_ip(0,self.speed)
        if Angle == 10:
             self.rect.move_ip(0,-self.speed)
        if Angle == 280:
             self.rect.move_ip(-self.speed,0)
        if Angle == 370:
             self.rect.move_ip(0,-self.speed)
        if Angle == -80:
             self.rect.move_ip(-self.speed,0)
        if Angle == -170:
             self.rect.move_ip(0,self.speed)
             
        pygame.display.update() 
    def Move_Backwards(self,scrn):
        scrn.fill((0,255,0))
        # moves the car backwards and in the correct direction based on the position of the car
        if Angle == 100:
             self.rect.move_ip(-self.speed*(self.breaks/100),0)
        if Angle == 190:
             self.rect.move_ip(0,-self.speed*(self.breaks/100))
        if Angle == 10:
             self.rect.move_ip(0,self.speed*(self.breaks/100))
        if Angle == 280:
             self.rect.move_ip(self.speed*(self.breaks/100),0)
        if Angle == 370:
             self.rect.move_ip(0,self.speed*(self.breaks/100))
        if Angle == -80:
             self.rect.move_ip(self.speed*(self.breaks/100),0)
        if Angle == -170:
             self.rect.move_ip(0,-self.speed*(self.breaks/100))
        pygame.display.update()
    def Move_Right(self,scrn):
         global Right
         # right is used to determine if the car has turned right to stop the constant rotating of the image
         global Angle
         scrn.fill((0,255,0))
         self.x = self.rect.centerx
         self.y=self.rect.centery
         if Right == False and Angle<370:
              self.img=pygame.transform.rotate(self.img,-90)
              Right=True
            
              Angle+=90
              # updates the angle as the car will be facing a different direction
        
         self.rect.move_ip(0,50*(self.power/100)*((100-self.weight)/100)*(self.breaks/100))
         # moves the car
         pygame.display.update()
         
    def Move_Left(self,scrn):
        global Left
        # left is used to determine if the car has turned left to prevent the image from constantly rotating 
        global Angle
        scrn.fill((0,255,0))
        if Left == False and Angle>-160:
             self.img=pygame.transform.rotate(self.img,90)
             Left = True
             
             Angle-=90
             # updates the angle as it will be facing a different direction
        self.rect.move_ip(0,-50*(self.power/100)*((100-self.weight)/100)*(self.breaks/100))
        pygame.display.update()
Car1=Car(pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\car.png'),20,50,100,20,scrn.get_rect().centerx,scrn.get_rect().centery)
cars.append(Car1)
Car2=Car(pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\car2.png'),20,50,100,20,scrn.get_rect().centerx,scrn.get_rect().centery)
cars.append(Car2)
Car3=Car(pygame.image.load(r'C:\Users\valih\OneDrive\Documents\python projects\NEA\car3.png'),20,50,100,20, scrn.get_rect().centerx,scrn.get_rect().centery)
cars.append(Car3)

def mergeSort(arr):
    if len(arr) <= 1:# checks if the list only has 1 item
        return arr# if only one item already sorted
    mid = len(arr) // 2    #Split the array into halves
    left_half = arr[:mid] #separates the array into the left half
    right_half = arr[mid:]#separates array into right half
    left_half = mergeSort(left_half)#sort left half
    right_half = mergeSort(right_half)#sort right half
    return merge(left_half, right_half) #merges the two halfs together 
def merge(left, right):
    merged = []# creates a new list
    i = j = 0# sets i and j to 0
    while i < len(left) and j < len(right): # checks the items of each array against each other
        if left[i] < right[j]:
            merged.append(left[i])# adds the left item to the array as it is smaller
            i += 1# increments the i varaible. index for the left
        else:
            merged.append(right[j])# adds the item in right to new array
            j += 1# increments j which is the index for left
    #Add whats let from left and right subarrays
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged# returns the sorted list
def main_menu(img, title, startf, scrn):
    #subroutine for creating the main menu
    scrn.blit(img, (0, 0))
    #outputs the background 
    scrn.blit(title, (200, 10))
    #outputs the title
    startf.update(scrn)
    #outputs the start button
    pygame.display.update()
    #updates the screen so that everything shows up in the screen

def mode_select(img, scrn, compt, arct):
    # subroutine for creating the mode select menu
    scrn.blit(img, (0, 0))
    #outputs the background
    compt.update(scrn)
    #outputs the competitive button
    arct.update(scrn)
    #outputs the arcade button
    buttonb.update(scrn)
    #outputs the back button
    pygame.display.update()
    #updtes the screen so that everything is outputted
def map_select(img,scrn,mapt,Track1_Text,Track2_Text,Track3_Text):
    #subroutine for creating the map select menu
    scrn.blit(img,(0,0))
    #outputs the background 
    scrn.blit(mapt,(300,10))
    #outputs the map select title
    buttonb.update(scrn)
    #outputs the back button
    Track1.update(scrn)
    # outputs the track 1 button
    Track2.update(scrn)
    # outputs the track 2 button
    Track3.update(scrn)
    # outputs the track 3 button
    scrn.blit(Track1_Text,(200,400))
    #outputs the track 1 label
    scrn.blit(Track2_Text,(500,400))
    #outputs the track 2 label
    scrn.blit(Track3_Text,(800,400))
    # outputs the track 3 label
    pygame.display.update()
    # updates the screen so that everything shows up on the screen

def car_select(img,scrn,car_select_text,arrow_right,arrow_left,car,buttonb,attributes_button,select_car):
    scrn.blit(img,(0,0))
    # outputs the background 
    scrn.blit(car_select_text,(300,10))
    # outputs the title
    arrow_right.update(scrn)
    # outputs the right arrow
    arrow_left.update(scrn)
    # outputs the lef arrow
    car.output(scrn)
    # outputs the current car
    buttonb.update(scrn)
    # outputs the back button
    attributes_button.update(scrn)
    # outputs the button to change the cars attributes
    select_car.update(scrn)
    # outputs the button to the select the car you want
    pygame.display.update()

def attributes_menu(car):
    total= car.get_power()+car.get_weight()+car.get_breaks()+car.get_tyrehealth()
    # stores the total amount of attribites used
    remaining = 200-total
    # stores how many attributes they have left to add
    
    pygame.draw.rect(scrn,[0,0,0],[400,100,600,600],0)
    # displays a blank screen
    font=pygame.font.SysFont('comicsansms',16)
    # creates the font for displaying the attributes
    scrn.blit(font.render('Power '+str(car.get_power()),False,(255,255,255)),(scrn.get_rect().centerx-100,200))
    scrn.blit(font.render('Weight '+str(car.get_weight()),False,(255,255,255)),(scrn.get_rect().centerx-100,250))
    scrn.blit(font.render('Breaks '+str(car.get_breaks()),False,(255,255,255)),(scrn.get_rect().centerx-100,300))
    scrn.blit(font.render('Tyre Health '+str(car.get_tyrehealth()),False,(255,255,255)),(scrn.get_rect().centerx-100,350))
    scrn.blit(font.render('Remaining Skill Points '+str(remaining),False,(255,255,255)),(scrn.get_rect().centerx-100,100))
    # outoputs the name of the attribute and the value of the attribute
    power_up_arrow.update(scrn)
    power_down_arrow.update(scrn)
    weight_up_arrow.update(scrn)
    weight_down_arrow.update(scrn)
    breaks_up_arrow.update(scrn)
    breaks_down_arrow.update(scrn)
    tyre_up_arrow.update(scrn)
    tyre_down_arrow.update(scrn)
    Select_car_button.update(scrn)
    # outputs the up and down buttons used to adjust the attributes
    pygame.display.update()

def game(Map,car):
    global Menu
    global set
    global start_time
    global laps
    global complete
    global Mode
    global finish_line
    global finish_line2
    global time
    pygame.display.update()

    if Map == 'Track 1' and Mode == 'comp':
        # checks what the map and game mode is
        scrn.blit(Track1_Game,(scrn.get_rect().centerx-350,scrn.get_rect().centery-300))
        # outputs the map
        if not set:###########error had set set to false in while loop same with time ######fixed
            # makes sure that the car isnt always at the original coordinates
            car.set_x(800)
            car.set_y(250)
            # sets the starting coordinates of the car
            set=True
            start_time=pygame.time.get_ticks()
            # this is the intial time which will help calculate the actual time.       
        car.output(scrn)
        # outputs the car
        finish_line.update(scrn)
        # outputs the finish line
        pygame.display.update()
        font=pygame.font.SysFont('comicsansms',26)
        # creates the font for the information in the banner
        time=(pygame.time.get_ticks() - start_time)/1000
        # gets the time you have taken in seconds
        text=font.render(str(time),False,(255,255,255))
        # creates the text to display the time
        lap_font=font.render(str(laps)+'/3',False,(255,255,255))
        # creates the text to output how many laps left
        scrn.blit(text,(scrn.get_rect().centerx,0))
        scrn.blit(lap_font,(scrn.get_rect().centerx+150,0))
        # outputs the text generated above
        tyre_font=font.render('Tyre health '+str(car.get_tyrehealth()),False,(255,255,255))
        # creates the text for the tyre health
        scrn.blit(tyre_font,(scrn.get_rect().centerx+300,0))
        # outputs the text
        pygame.display.update()
        if finish_line.rect.colliderect(car) and laps >0 and complete == True:# error when on line keeps registering lap being done 
           # checks if the car has completed a lap
            laps=laps-1
            complete = False
        if not finish_line.rect.colliderect(car):
            complete = True
        # checks if the car has gone passed the finish line and started the next lap

        if finish_line.rect.colliderect(car) and laps==0:
            # checks if the user has finished the game
            scrn.fill((0,0,0))
            # creates a blank screen
            Menu='Result'
            # sets the current menu to result
            pygame.display.update()
    if Map == 'Track 1' and Mode == 'arc':
        # checks the map and gamemode 
        scrn.blit(Track1_Game,(scrn.get_rect().centerx-350,scrn.get_rect().centery-300))
        if not set:###########error had set set to false in while loop same with time. fixed 
            car.set_x(800)
            car.set_y(250)
            set=True
            start_time=pygame.time.get_ticks()
        
        car.output(scrn)
        finish_line.update(scrn)
        pygame.display.update()

        font=pygame.font.SysFont('comicsansms',26)
        
        
        time=(pygame.time.get_ticks() - start_time)/1000
        
        text=font.render(str(time),False,(255,255,255))
        lap_font=font.render(str(laps)+'/3',False,(255,255,255))
        scrn.blit(text,(scrn.get_rect().centerx,0))
        scrn.blit(lap_font,(scrn.get_rect().centerx+150,0))
        tyre_font=font.render('Tyre health '+str(car.get_tyrehealth()),False,(255,255,255))
        scrn.blit(tyre_font,(scrn.get_rect().centerx+300,0))
        pygame.display.update()
        if finish_line.rect.colliderect(car) and laps >0 and complete == True:# error when on line keeps registering lap being done /// resolved 
            laps=laps-1
            complete = False
        if not finish_line.rect.colliderect(car):
            complete = True
        if finish_line.rect.colliderect(car) and laps==0:
            scrn.fill((0,0,0))
            Menu='Result'
            pygame.display.update()

    if Map == 'Track 2' and Mode == 'comp':
        # checks the map and game mode 
        scrn.blit(Track2_Game,(scrn.get_rect().centerx-350,scrn.get_rect().centery-270))
        # outputs the map
        pygame.display.update()
        if not set:
            car.set_x(800)
            car.set_y(750)
            # sets car coordinates for track 2
            set=True
            start_time=pygame.time.get_ticks()
        car.output(scrn)
        finish_line=Button(finish_line2,[scrn.get_rect().centerx-50,750],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
        # creates finish line for second map. has to use finish line 2 as finish line is now a button not an image
        finish_line.update(scrn)
        pygame.display.update()
        font=pygame.font.SysFont('comicsansms',26)
        
        
        time=(pygame.time.get_ticks() - start_time)/1000
        
        text=font.render(str(time),False,(255,255,255))
        lap_font=font.render(str(laps)+'/3',False,(255,255,255))
        scrn.blit(text,(scrn.get_rect().centerx,0))
        scrn.blit(lap_font,(scrn.get_rect().centerx+150,0))
        tyre_font=font.render('Tyre health '+str(car.get_tyrehealth()),False,(255,255,255))
        scrn.blit(tyre_font,(scrn.get_rect().centerx+300,0))
        pygame.display.update()
        if finish_line.rect.colliderect(car) and laps >0 and complete == True:# error when on line keeps registering lap being done// resolved
            laps=laps-1
            complete = False
        if not finish_line.rect.colliderect(car):
            complete = True

        if finish_line.rect.colliderect(car) and laps==0:
            scrn.fill((0,0,0))
            Menu='Result'
            pygame.display.update()
    if Map == 'Track 2' and Mode == 'arc':
        scrn.blit(Track2_Game,(scrn.get_rect().centerx-350,scrn.get_rect().centery-270))
        pygame.display.update()
        if not set:
            car.set_x(800)
            car.set_y(750)
            set=True
            start_time=pygame.time.get_ticks()
        car.output(scrn)
        finish_line=Button(finish_line2,[scrn.get_rect().centerx-50,750],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
        finish_line.update(scrn)
        pygame.display.update()
        font=pygame.font.SysFont('comicsansms',26)
        
        
        time=(pygame.time.get_ticks() - start_time)/1000
        
        text=font.render(str(time),False,(255,255,255))
        lap_font=font.render(str(laps)+'/3',False,(255,255,255))
        scrn.blit(text,(scrn.get_rect().centerx,0))
        scrn.blit(lap_font,(scrn.get_rect().centerx+150,0))
        tyre_font=font.render('Tyre health '+str(car.get_tyrehealth()),False,(255,255,255))
        scrn.blit(tyre_font,(scrn.get_rect().centerx+300,0))
        pygame.display.update()
        if finish_line.rect.colliderect(car) and laps >0 and complete == True:# error when on line keeps registering lap being done // resolved
            laps=laps-1
            complete = False
        if not finish_line.rect.colliderect(car):
            complete = True

        if finish_line.rect.colliderect(car) and laps==0:
            scrn.fill((0,0,0))
            Menu='Result'
            pygame.display.update()

    if Map=='Track 3' and Mode == 'comp':
        # checkc the map and game mode
        scrn.blit(Track3_Game,(scrn.get_rect().centerx-350,scrn.get_rect().centery-270))
        pygame.display.update()
        if not set:
            car.set_x(600)
            car.set_y(250)
            # sets the cars starting coordinates for map 3
            set=True
            start_time=pygame.time.get_ticks()
        car.output(scrn)
        finish_line=Button(finish_line2,[500,250],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
        # creates finish line for map 3
        finish_line.update(scrn)
        pygame.display.update()
        font=pygame.font.SysFont('comicsansms',26)
        time=(pygame.time.get_ticks() - start_time)/1000
        
        text=font.render(str(time),False,(255,255,255))
        lap_font=font.render(str(laps)+'/3',False,(255,255,255))
        scrn.blit(text,(scrn.get_rect().centerx,0))
        scrn.blit(lap_font,(scrn.get_rect().centerx+150,0))
        tyre_font=font.render('Tyre health '+str(car.get_tyrehealth()),False,(255,255,255))
        scrn.blit(tyre_font,(scrn.get_rect().centerx+300,0))
        pygame.display.update()
        if finish_line.rect.colliderect(car) and laps >0 and complete == True:# error when on line keeps registering lap being done // resolved
            laps=laps-1
            complete = False
        if not finish_line.rect.colliderect(car):
            complete = True

        if finish_line.rect.colliderect(car) and laps==0:
            scrn.fill((0,0,0))
            Menu='Result'
            pygame.display.update()
    if Map == 'Track 3' and Mode == 'arc':
        scrn.blit(Track3_Game,(scrn.get_rect().centerx-350,scrn.get_rect().centery-270))
        pygame.display.update()
        if not set:
            car.set_x(600)
            car.set_y(250)
            set=True
            start_time=pygame.time.get_ticks()
        car.output(scrn)
        finish_line=Button(finish_line2,[500,250],'.',pygame.font.SysFont("comicsansms", 1), 'Black', 'White')
        finish_line.update(scrn)
        pygame.display.update()
        font=pygame.font.SysFont('comicsansms',26)
        time=(pygame.time.get_ticks() - start_time)/1000
        
        text=font.render(str(time),False,(255,255,255))
        lap_font=font.render(str(laps)+'/3',False,(255,255,255))
        scrn.blit(text,(scrn.get_rect().centerx,0))
        scrn.blit(lap_font,(scrn.get_rect().centerx+150,0))
        tyre_font=font.render('Tyre health '+str(car.get_tyrehealth()),False,(255,255,255))
        scrn.blit(tyre_font,(scrn.get_rect().centerx+300,0))
        pygame.display.update()
        if finish_line.rect.colliderect(car) and laps >0 and complete == True:# error when on line keeps registering lap being done 
            laps=laps-1
            complete = False
        if not finish_line.rect.colliderect(car):
            complete = True

        if finish_line.rect.colliderect(car) and laps==0:
            scrn.fill((0,0,0))
            Menu='Result'
            pygame.display.update()


def result(time):
    font=pygame.font.SysFont('comicsansms',26)
    result=font.render('Time '+str(time)+' Seconds',False,(255,255,255))
    scrn.blit(result,(scrn.get_rect().centerx,scrn.get_rect().centery))
    # outputs the time it took them
    leader_board_button.update(scrn)
    # outputs the button that will show the leaderboard
    pygame.display.update()

def Leader_board(list):
    scrn.blit(leaderboard,(100,10))
    font=pygame.font.SysFont('comicsansms',26) 
    if len(list)<=10:
        # checks the size of the list of scores
        for i in range (0,len(list)):
            result=font.render(str(i+1)+': '+str(list[i])+' Seconds',False,(255,255,255))
            scrn.blit(result,(scrn.get_rect().centerx,(scrn.get_rect().centery-200)+(i*50)))
            pygame.display.update()
            # outputs all of the scores
    else:
        for i in range (0,10):
            result=font.render(str(i+1)+': '+str(list[i])+' Seconds',False,(255,255,255))
            scrn.blit(result,(scrn.get_rect().centerx,(scrn.get_rect().centery-200)+(i*50)))
            pygame.display.update()
            # outputs the first 10 scores
    Home_button.update(scrn)
    # outputs the button to take you to the home screen
def add_and_sort(map):
    global write
    global list
    file=open(map+'.txt','a')
      # opens the corresponding file to append
    file.write(str(time)+'\n')
     # adds the score to the file \n makes the next score be on the next line
    write = True
    #now that they have added it is set to true
    file.close()
    #closes the file
    file=open(map+'.txt','r')
    # opens the file to read
    list=file.readlines()
     # stores each line in file as an element in an array
    for i in range(0,len(list)):
        list[i]=float(list[i])
     # converts each element in array to a float data type
    list=mergeSort(list)
     #sorts the array
    file.close()





# the main game loop
while status:
    pygame.display.update()
    for i in pygame.event.get():
    #runs through every input in pygame
        if pygame.mouse.get_pressed()[0] and Menu == 'Main Menu' and startf.checkForInput(pygame.mouse.get_pos()):
            #checks if the start button is pressed
            scrn.fill((0, 0, 0))
            #covers everything on the screen so that they can output a new menu
            pygame.display.update()
            # updates the display so that the screen is blank
            Menu = 'Mode Select'
            # changes the current menu to the next menu which is mode select
            Menu_Visited.append('Main Menu')
            # adds main menu to the previous menus that the user has visited so that they can go back to it using the back button
        if pygame.mouse.get_pressed()[0] and Menu == 'Mode Select' and compt.checkForInput(pygame.mouse.get_pos()):
            #checks if the competitve button is pressed
            Menu = 'Map Select'
            #changes the current menu to the next menu map select
            Mode='comp'
            # sets the game mode to competitive
            scrn.fill((0,0,0))
            #creates a balnk screen
            pygame.display.update()
            #updates the screen so that it is blank
            Menu_Visited.append('Mode Select')
            #adds mode select to the menu visited stack so that it can be returned to using the back button
        if pygame.mouse.get_pressed()[0] and Menu == 'Mode Select' and arct.checkForInput(pygame.mouse.get_pos()):
            # checks if the arcade button is pressed
            Menu='Map Select'
            # sets the current menu to the next menu which is map select
            Mode='arc'
            # sets the current game mode to arcade
            scrn.fill((255,0,0))
            # creates a blank red screen. Only different to help with testing between the two modes
            pygame.display.update()
            # updates the display to create the blank screen
            Menu_Visited.append('Mode Select')
            # adds mode select to the previous menus stack so that the user can return to it when they use the back button
        if pygame.mouse.get_pressed()[0] and buttonb.checkForInput(pygame.mouse.get_pos()):
            # checks if the back button is pressed
            if len(Menu_Visited) != 0:
                # makes sure that the stack is not empty
                Menu = Menu_Visited.pop()
                # stores the removed menu as the current menu
                scrn.fill((0,0,0))
                # creates a blank screen
            else:
                pass
            # if it is empty the button does nothing
        if pygame.mouse.get_pressed()[0] and Menu == 'Map Select' and Track1.checkForInput(pygame.mouse.get_pos()):
            # checks if the track 1 button is pressed
            Map = 'Track 1'
            # sets the map to track 1 
            Menu = 'Car Select'
            # sets the current menu to car select
            Menu_Visited.append('Map Select')
            # adds map select to the menus visited stack 
            scrn.fill((0,0,0))
            # creates a black screen which will be used to test that the different buttons work independantly 
            pygame.display.update()
        if pygame.mouse.get_pressed()[0] and Menu == 'Map Select' and Track2.checkForInput(pygame.mouse.get_pos()):
            # checks if the track 2 button is pressed
            Map = 'Track 2'
            # sets the current map to track 2
            Menu = 'Car Select'
            # sets the current menu to car select
            Menu_Visited.append('Map Select')
            # adds map select to the stack of the previous menus
            scrn.fill((255,0,0))
            # sets the screen to red which will be used when testing.       
            pygame.display.update()
        if pygame.mouse.get_pressed()[0] and Menu == 'Map Select' and Track3.checkForInput(pygame.mouse.get_pos()):
            # checks if the track 3 button is pressed
            Map = 'Track 3'
            # sets the current map to track 3
            Menu = 'Car Select'
            # sets the current menu to car select
            Menu_Visited.append('Map Select')
            # adds map select to the prevoius menus so that it can be accessed by pressing the back button
            scrn.fill((0,255,0))
            # sets the screen to green so that I can tell that the track 3 button works independantly to the other buttons on the screen 
            pygame.display.update()
        if pygame.mouse.get_pressed()[0] and Menu == 'Car Select' and arrow_right.checkForInput(pygame.mouse.get_pos()):
            #checks if the user has clicked the right arrow
            if car_index<len(cars)-1:
                # checks that the index does not exceed the last item in the list
                car_index+=1
                # adds 1 to the index so that the next car in the list is shown
            else:
                pass
            # if it is at the end of the list nothing happens to prevent the index from being out of range producing an error
        if pygame.mouse.get_pressed()[0] and Menu == 'Car Select' and arrow_left.checkForInput(pygame.mouse.get_pos()):
            # checks if the left arrow has been pressed
            if car_index>0:
                # checks that the index is bigger than 0 to prevent a minus index
                car_index-=1
                # minuses one from the car index to show the previous car
            else:
                pass
            # if the index is 0 or less nothing happens to prevent an error
        if (Menu == 'Car Select' or Menu == 'Attributes') and pygame.mouse.get_pressed()[0] and Select_car_button.checkForInput(pygame.mouse.get_pos()):
            # checks if the select car button is pressed
            car=cars[car_index]
            #sets the car to the current car on the screen
            Menu = 'Game'
            # sets the current menu to game which will be the actual game 
            Menu_Visited.append('Car Select')
            # adds car select to the previous menus visited 
            scrn.fill((0,0,255))
            # creates a blank blue screen for testing which will provide a blank canvas for the game menu
            pygame.display.update()
        if Menu == 'Car Select' and pygame.mouse.get_pressed()[0] and Attributes_button.checkForInput(pygame.mouse.get_pos()):
            Menu='Attributes'
            car=cars[car_index]
            attributes_menu(car)
        if Menu == 'Attributes' and pygame.mouse.get_pressed()[0] and power_up_arrow.checkForInput(pygame.mouse.get_pos()):
            # checks if the power up arrow has been pressed
            total= car.get_power()+car.get_weight()+car.get_breaks()+car.get_tyrehealth()
            remaining = 200-total
            # calculates the remaining attributes
            if remaining>=5:
                # checks that there is at least 5
                car.set_power(car.get_power()+5)
                # adds 5 to the power
                attributes_menu(car)# wasnt updating test so added this to update
                pygame.display.update()
        if Menu == 'Attributes' and pygame.mouse.get_pressed()[0] and power_down_arrow.checkForInput(pygame.mouse.get_pos()):
            # checks if the power down arrow has been pressed
            if car.get_power()>=5:
                # checks that their is at least 5 power
                car.set_power(car.get_power()-5)
                # minuses 5 from the power
                attributes_menu(car)
                # updates the screen
        if Menu == 'Attributes' and pygame.mouse.get_pressed()[0] and weight_up_arrow.checkForInput(pygame.mouse.get_pos()):
            # checks if the weight up arrow has been pressed 
            total= car.get_power()+car.get_weight()+car.get_breaks()+car.get_tyrehealth()
            remaining = 200-total
            if remaining>=5:
                # checks that there is at least 5 attributes left
                car.set_weight(car.get_weight()+5)
                # adds 5 to the power 
                attributes_menu(car)# updates the menu
        if  Menu == 'Attributes' and pygame.mouse.get_pressed()[0] and weight_down_arrow.checkForInput(pygame.mouse.get_pos()):
            # checks if the weight down arrow is presssed 
            if car.get_weight()>=5:
                # checks that the car weight is at least 5
                car.set_weight(car.get_weight()-5)
                # subtracts 5
                attributes_menu(car)
                # updates the menu
        if  Menu == 'Attributes' and pygame.mouse.get_pressed()[0] and breaks_up_arrow.checkForInput(pygame.mouse.get_pos()):
            # checks if the breaks up arrow is pressed
            total= car.get_power()+car.get_weight()+car.get_breaks()+car.get_tyrehealth()
            remaining = 200-total
            if remaining>=5:
                car.set_breaks(car.get_breaks()+5)
                # adds 5 to breaks 
                attributes_menu(car)
                # updates the screen
        if Menu == 'Attributes' and pygame.mouse.get_pressed()[0] and breaks_down_arrow.checkForInput(pygame.mouse.get_pos()):
            # checks if the breaks down is pressed
            if car.get_breaks()>=5:
                car.set_breaks(car.get_breaks()-5)
                # subtracts 5 from breaks
                attributes_menu(car)
        if Menu == 'Attributes' and pygame.mouse.get_pressed()[0] and tyre_up_arrow.checkForInput(pygame.mouse.get_pos()):
            # checks if the tyrehealth up arrow has been pressed
            total= car.get_power()+car.get_weight()+car.get_breaks()+car.get_tyrehealth()
            remaining = 200-total
            if remaining>=5:
                car.set_tyrehealth(car.get_tyrehealth()+5)
                # adds 5 to tyre health attribute 
                attributes_menu(car)
        if Menu == 'Attributes' and pygame.mouse.get_pressed()[0] and tyre_down_arrow.checkForInput(pygame.mouse.get_pos()):
            # checks if the tyre health down arrow has been pressed 
            if car.get_tyrehealth()>=5:
                car.set_tyrehealth(car.get_tyrehealth()-5)
                # subtracts 5 fromt the tyre health
                attributes_menu(car)
        if Menu == 'Result' and pygame.mouse.get_pressed()[0] and leader_board_button.checkForInput(pygame.mouse.get_pos()):
            # checks if the leaderboard button has been pressed
            Menu = 'Leader Board'
            # sets the current menu to leaderboard 
            scrn.fill((0,0,0))
            # creates a blank screen to display the leaderboard onto
            pygame.display.update()
        if Menu == 'Leader Board' and pygame.mouse.get_pressed()[0] and Home_button.checkForInput(pygame.mouse.get_pos()):
            Menu= 'Main Menu'
            scrn.fill((0,0,0))
            pygame.display.update()
        keys=pygame.key.get_pressed()
        # stores the keys that the user presses
        if keys[pygame.K_w] and Menu == 'Game':
                # checks if they have pressed the w key
                car.Move_Forward(scrn)
                # car moves forward
                car.output(scrn)
                # outputs the new car
                Right = False
                # they have not turned right so false
                Left=False
                # not turned left so false
                if car.get_tyrehealth()>0 and Mode == 'comp':
                    # checks that the tyre health is above 0
                    car.set_tyrehealth(car.get_tyrehealth()-2)
                    # reduces the tyre health in the competitve game mode
        if keys[pygame.K_s] and Menu == 'Game':
                # checks if s key is pressed 
                car.Move_Backwards(scrn)
                # car moves backwards 
                car.output(scrn)
                Right=False
                # car not turned right so false 
                Left=False
                # car not turned left so false
        if keys[pygame.K_d] and Menu == 'Game':
             # checks if d key is pressed 
             car.Move_Right(scrn)
             #rotates the car to the right 
             car.output(scrn)
             Right=True
             # car has turned right so set to true 
             Left=False
             # car not turned left so set to false
        if keys[pygame.K_a] and Menu == 'Game':
             # checks if a key is pressed 
             car.Move_Left(scrn)
             # rotates the car to the left
             car.output(scrn)
             Right=False
             # not turned right so false
             Left=True
             # turned left so True 
        
        
        
        if Menu == 'Mode Select':
            # checks if the current menu is mode select
            mode_select(img, scrn, compt, arct)
            # sets the screen to ouptput the mode select menu

        if i.type == pygame.QUIT:
            # checks if the user has quit the application 
            pygame.quit()
            # closes the game
            status = False
            # stops the game loop from running

        if Menu == 'Main Menu':
            # checks if the current menu is the main menu
            main_menu(img, title, startf, scrn)
            # outputs the main menu
        if Menu == 'Map Select':
            # checks if the current menu is map select
            map_select(img,scrn,mapt,Track1_Text,Track2_Text,Track3_Text)
            # outputs the map selct screen
        if Menu == 'Car Select':
            car_select(img,scrn,car_select_text,arrow_right,arrow_left,cars[car_index],buttonb,Attributes_button,Select_car_button)
        if Menu == 'Game':
            pygame.display.update()
            game(Map,car)
            pygame.display.update()
        if Menu == 'Result':
            result(time)
            if write == False:
                # checks if the score has already been added
                add_and_sort(Map)

                    

        if Menu == 'Leader Board':
            Leader_board(list)


                


pygame.quit()
#closes the game