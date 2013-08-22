# coding: UTF-8
import pygame

#キーボードの設定を置く場所です
#eventhandlerとflamehandlerを必ず書いてください



KEYDICT = {
"moveup" : "K_UP", "movedown" : "K_DOWN",
"moveright" : "K_RIGHT", "moveleft" : "K_LEFT",

"cameraup" : "K_w", "cameradown" : "K_s",
"cameraright" : "K_d", "cameraleft" : "K_a",

"cameralock" : "K_q",
"shot" : "K_z",
"jump" : "K_x",
"dash" : "K_c"
}

#data container

def reset():
    global move_up, move_down, move_right, move_left
    global camera_up, camera_down, camera_right, camera_left
    global cameralock, shot, jump, dash
    
    move_up = 0
    move_down = 0
    move_right = 0
    move_left = 0

    camera_up = 0
    camera_down = 0
    camera_right = 0
    camera_left = 0
    
    cameralock = 0
    shot = 0
    jump = 0
    dash = 0

def getpygameattr(attr):
    return getattr(pygame, KEYDICT[attr])

def eventhandler(event):
    global move, camera, cameralock, shot, jump, dash
    
    if event.type == pygame.KEYDOWN:
        if event.key == getpygameattr("moveup"):
            move_up = 1
        elif event.key == getpygameattr("movedown"):
            move_down = 1
        elif event.key == getpygameattr("moveright"):
            move_right = 1
        elif event.key == getpygameattr("moveleft"):
            move_left = 1
            
        elif event.key == getpygameattr("cameraup"):
            camera_up = 1
        elif event.key == getpygameattr("cameradown"):
            camera_down = 1
        elif event.key == getpygameattr("cameraright"):
            camera_cd = 1
        elif event.key == getpygameattr("cameraleft"):
            camera[1][1] = 1

        elif event.key == getpygameattr("cameralock"):
            cameralock = 1
        elif event.key == getpygameattr("shot"):
            shot = 1
        elif event.key == getpygameattr("jump"):
            jump = 1
        elif event.key == getpygameattr("dash"):
            dash = 1
            
    if event.type == pygame.KEYUP:
        if event.key == getpygameattr("moveup"):
            move[0][0] = 0
        elif event.key == getpygameattr("movedown"):
            move[0][1] = 0
        elif event.key == getpygameattr("moveright"):
            move[1][0] = 0
        elif event.key == getpygameattr("moveleft"):
            move[1][1] = 0
            
        elif event.key == getpygameattr("cameraup"):
            camera[0][0] = 0
        elif event.key == getpygameattr("cameradown"):
            camera[0][1] = 0
        elif event.key == getpygameattr("cameraright"):
            camera[1][0] = 0
        elif event.key == getpygameattr("cameraleft"):
            camera[1][1] = 0

        elif event.key == getpygameattr("cameralock"):
            cameralock = -1
        elif event.key == getpygameattr("shot"):
            shot = -1
        elif event.key == getpygameattr("jump"):
            jump = -1
        elif event.key == getpygameattr("dash"):
            dash = -1

def flamehandler(inputobject):
    global move, camera, cameralock, shot, jump, dash
    
    for item in [move, camera]:
        for item in [move, camera]:
            
            item[index] = 0
            
    inputobject.move = 0
