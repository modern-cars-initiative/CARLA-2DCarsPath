"""Global functions dre2 file"""
import math
import pygame

def pygamestringstyles():
    """Styles"""
    colorin = (255,0,0)
    fontin = pygame.font.SysFont("Verdana", 20)
    return colorin,fontin

#Mudar cor carro
def tint(surf, tint_color):
    """Adds tint_color onto surf"""
    surf = surf.copy()
    surf.fill((0, 0, 0, 255), None, pygame.BLEND_RGBA_MULT)
    surf.fill(tint_color[0:3] + (0,), None, pygame.BLEND_RGBA_ADD)
    return surf

def distancia2d(xval1,yval1,xval2,yval2):
    """Calc Distance"""
    xval = xval2 - xval1
    yval = yval2 - yval1
    return round(math.sqrt(math.pow(xval, 2) + math.pow(yval, 2)),1)

def screendistance(screenin, readx, ready, readx2, ready2, colorin, fontin, i):
    """Distance"""
    distance = distancia2d(readx[i],ready[i],readx2[i],ready2[i])
    textdistancia = fontin.render(f"Distance between the cars is: {distance}", False, colorin)
    screenin.blit(textdistancia, (0,670))

def textmult(screenin, colorin, fontin, totaltick, multtick, i):
    """Change tick text"""
    if multtick == 1:
        texttick = fontin.render(f"Tick: {i}/{totaltick-1}", False, colorin)
        screenin.blit(texttick, (0,40))
    elif multtick == 2:
        texttick = fontin.render(f"Tick x2: {i}/{totaltick-1}", False, colorin)
        screenin.blit(texttick, (0,40))
    elif multtick == 4:
        texttick = fontin.render(f"Tick x4: {i}/{totaltick-1}", False, colorin)
        screenin.blit(texttick, (0,40))

def playspeed(multplay):
    """Change text of speed play"""
    if multplay == 1:
        textspeed = font.render("Speed: 1x", False, color)
        screen.blit(textspeed, (0,40))
    elif multplay == 3:
        textspeed = font.render("Speed: 3x", False, color)
        screen.blit(textspeed, (0,40))
    elif multplay == 7:
        textspeed = font.render("Speed: 7x", False, color)
        screen.blit(textspeed, (0,40))

def textchangespeedmodplay():
    """Text speed"""
    textchangespeedvalue = font.render("Click on 1 -> Speed x1 | Click on 3 -> Speed x3 | Click on 7 -> Speed x7", False, color)
    screen.blit(textchangespeedvalue, (0, 0))

def textonscreen(colorin, fontin):
    """Text on screen"""
    textmodein = fontin.render("Arrow up -> Edit Mode | Arrow down -> Car Trajectory", False, colorin)
    textinfcar1in = fontin.render("Data car 1:", False, colorin)
    textinfcar2in = fontin.render("Data car 2:", False, colorin)
    textinfocontroltickin = fontin.render("Left arrow -> next tick | Right arrow -> return tick", False, colorin)
    textchangetickvaluein = fontin.render("Click on 1 -> Tick x1 | Click on 2 -> Tick x2 | Click on 4 -> Tick x4", False, colorin)
    textplayin = fontin.render("Press P to play", False, colorin)
    textstopin = fontin.render("Press S to stop", False, colorin)
    return textmodein,textinfcar1in,textinfcar2in,textinfocontroltickin,textchangetickvaluein,textplayin,textstopin

def distancemouseclick(screenin, colorin, fontin, pos1, pos2):
    """Click on two points in screen to see distance between points"""
    pygame.draw.line(screenin, (255, 255, 255), (pos1[0],pos1[1]), (pos2[0],pos2[1]))
    newx = (pos1[0]+pos2[0])/2
    newy = (pos1[1]+pos2[1])/2
    textdistance = distancia2d(pos1[0],pos1[1],pos2[0],pos2[1])
    showdistance = fontin.render(str(textdistance), False, colorin)
    screenin.blit(showdistance, (newx,newy))

def forplay(screenin, readx, ready, readx2, ready2, image1, image2, center_origin, center_origin2, addplay):
    """Loop press P"""
    for j in range(0, addplay):
        if j != addplay-1:
            screenin.blit(image2, center_origin([readx[j], ready[j]]))
            screenin.blit(image2, center_origin2([readx2[j], ready2[j]]))
        else:
            screenin.blit(image1, center_origin([readx[j], ready[j]]))
            screenin.blit(tint(image1,(124,252,0)), center_origin2([readx2[j], ready2[j]]))

def infoscreen(screenin, textinfocontroltickin, textchangetickvaluein, textplayin):
    """Some info on screen"""
    screenin.blit(textinfocontroltickin, (0,0))
    screenin.blit(textchangetickvaluein, (450,0))
    screenin.blit(textplayin, (500,700))

def infocar2(screenin, readvel2, readbrake2, readthrottle2, readsteer2, readgear2, colorin, fontin, textinfcar2in, i):
    """Info about car2 on screen"""
    screenin.blit(textinfcar2in, (0,240))
    textspeed = fontin.render(f"Speed: {readvel2[i]}", False, colorin)
    screenin.blit(textspeed, (0,260))
    textbrake = fontin.render(f"Brake: {readbrake2[i]}", False, colorin)
    screenin.blit(textbrake, (0,280))
    textthrottle = fontin.render(f"Throttle: {readthrottle2[i]}", False, colorin)
    screenin.blit(textthrottle, (0,300))
    if readsteer2[i] < 0:
        textsteer = fontin.render(f"Steer: L {readsteer2[i]:.1f}", False, colorin)
    elif readsteer2[i] > 0:
        textsteer = fontin.render(f"Steer: R {readsteer2[i]:.1f}", False, colorin)
    else:
        textsteer = fontin.render(f"Steer: {readsteer2[i]:.1f}", False, colorin)
    screenin.blit(textsteer, (0,320))
    if readgear2[i] == 0:
        textgear = fontin.render("Gear: N", False, colorin)
    elif readgear2[i] == -1:
        textgear = fontin.render("Gear: R", False, colorin)
    else:
        textgear = fontin.render(f"Gear: {readgear2[i]}", False, colorin)
    screenin.blit(textgear, (0,340))

def infocar1(screenin, readvel, readbrake, readthrottle, readsteer, readgear, colorin, fontin, textinfcar1in, i):
    """Info about car1 on screen"""
    screenin.blit(textinfcar1in, (0,80))
    textspeed = fontin.render(f"Speed: {readvel[i]}", False, colorin)
    screenin.blit(textspeed, (0,100))
    textbrake = fontin.render(f"Brake: {readbrake[i]}", False, colorin)
    screenin.blit(textbrake, (0,120))
    textthrottle = fontin.render(f"Throttle: {readthrottle[i]}", False, colorin)
    screenin.blit(textthrottle, (0,140))
    if readsteer[i] < 0:
        textsteer = fontin.render(f"Steer: L {readsteer[i]:.1f}", False, colorin)
    elif readsteer[i] > 0:
        textsteer = fontin.render(f"Steer: R {readsteer[i]:.1f}", False, colorin)
    else:
        textsteer = fontin.render(f"Steer: {readsteer[i]:.1f}", False, colorin)
    screenin.blit(textsteer, (0,160))
    if readgear[i] == 0:
        textgear = fontin.render("Gear: N", False, colorin)
    elif readgear[i] == -1:
        textgear = fontin.render("Gear: R", False, colorin)
    else:
        textgear = fontin.render(f"Gear: {readgear[i]}", False, colorin)
    screenin.blit(textgear, (0,180))

def rightleftclickordrawagain(screenin, readx, ready, readx2, ready2, image1, image2, center_origin, center_origin2, i):
    """Draw path and car on right or left click"""
    for j in range(0, i):
        if j != i-1:
            screenin.blit(image2, center_origin([readx[j], ready[j]]))
            screenin.blit(image2, center_origin2([readx2[j], ready2[j]]))
        else:
            screenin.blit(image1, center_origin([readx[j], ready[j]]))
            screenin.blit(tint(image1,(124,252,0)), center_origin2([readx2[j], ready2[j]]))

def drawcar(screenin, readx, ready, readx2, ready2, image1, center_origin, center_origin2, i):
    """Draw car"""
    screenin.blit(image1, center_origin([readx[i], ready[i]]))
    screenin.blit(tint(image1,(124,252,0)), center_origin2([readx2[i], ready2[i]]))

def drawpath(screenin, readx, ready, readx2, ready2, image2, center_origin, center_origin2, i):
    """Draw path"""
    screenin.blit(image2, center_origin([readx[i], ready[i]]))
    screenin.blit(image2, center_origin2([readx2[i], ready2[i]]))

def screenfill(screenin):
    """Clear screen"""
    screenin.fill((0,0,0))

pygame.init()
screen = pygame.display.set_mode([1280, 720], 0, 32)
color, font = pygamestringstyles()
textmode, textinfcar1, textinfcar2, textinfocontroltick, textchangetickvalue, textplay, textstop = textonscreen(color, font)
