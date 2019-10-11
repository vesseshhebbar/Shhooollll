# -*- coding: utf-8 -*-
"""
Created on Fri Oct 11 09:22:06 2019

@author: student
"""

import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))  
pygame.display.set_caption("asd")

x = 50
y = 50
width = 40
height = 60
vel = 5

run=True
while(run):
    pygame.time.delay(30)
    
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            run = False;

    keys = pygame.key.get_pressed()
    
    if(keys[pygame.K_LEFT]):
        x -= vel
    if(keys[pygame.K_RIGHT]):
            x += vel
    if(keys[pygame.K_UP]):
            y -= vel
    if(keys[pygame.K_DOWN]):
            y += vel
    
    win.fill((0,0,0))          
    pygame.draw.rect(win, (255,0,0), (x,y,width,height))
    pygame.display.update()
            
pygame.quit()
        