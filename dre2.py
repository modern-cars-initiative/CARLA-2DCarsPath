"""Control cars path by tick"""
# pylint: disable=no-member
# Up line to ignore pygame
# pylint: disable=line-too-long
import shutil
import pygame
from initdre2 import image1, image2, center_origin, center_origin2, data1input, data2input
from funcdre2 import screenfill, rightleftclickordrawagain, drawcar, drawpath, textmult, screendistance, infoscreen, forplay, distancemouseclick, playspeed, textchangespeedmodplay, infocar
from funcdre2 import screen, textstop
from funcdre2 import color, font, textinfcar1, textinfcar2, textinfocontroltick, textchangetickvalue, textmode, textplay

# Keypress dentro do for pygame.event.get() so avaça mais um mesmo que a tecla continue precionada
# Keypress fora do for avança muitos valores de uma vez
def loop():
    """Main code"""
    try:
        # Control vars
        totaltick = data1input["readtick1"][-1]
        multtick = 1
        multplay = 1
        modedit = False
        run = True
        click = 0
        i = 0
        addplay = 0
        event = None
        # Loop
        while run:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    # Options Play
                    if event.key == pygame.K_p:
                        play = True
                        addplay = 0
                    elif event.key == pygame.K_s:
                        play = False
                        i = addplay
                        screen.fill((0, 0, 0))
                        rightleftclickordrawagain(screen, data1input, data2input, image1, image2, center_origin, center_origin2, i)
                    # Exit
                    if event.key == pygame.K_ESCAPE:
                        run = False
                    # Avançar/recuar tick
                    if event.key == pygame.K_RIGHT and i < (len(data1input["readx"]))+1:
                        try:
                            screenfill(screen)
                            i += multtick
                            rightleftclickordrawagain(screen, data1input, data2input, image1, image2, center_origin, center_origin2, i)
                        except IndexError:
                            i = (len(data1input["readx"]))+1
                    # voltar o tick
                    elif event.key == pygame.K_LEFT and i >= 0:
                        screenfill(screen)
                        i -= multtick
                        rightleftclickordrawagain(screen, data1input, data2input, image1, image2, center_origin, center_origin2, i)
                    # Alterar valor tick
                    if event.key == pygame.K_1 and multtick != 1:
                        multtick = 1
                        screenfill(screen)
                        rightleftclickordrawagain(screen, data1input, data2input, image1, image2, center_origin, center_origin2, i)
                        drawcar(screen, data1input, data2input, image1, center_origin, center_origin2, i)
                    elif event.key == pygame.K_2 and multtick != 2:
                        multtick = 2
                        screenfill(screen)
                        rightleftclickordrawagain(screen, data1input, data2input, image1, image2, center_origin, center_origin2, i)
                        drawcar(screen, data1input, data2input, image1, center_origin, center_origin2, i)
                    elif event.key == pygame.K_4 and multtick != 4:
                        multtick = 4
                        screenfill(screen)
                        rightleftclickordrawagain(screen, data1input, data2input, image1, image2, center_origin, center_origin2, i)
                        drawcar(screen, data1input, data2input, image1, center_origin, center_origin2, i)
                    # Alterar valor do play
                    if event.key == pygame.K_1 and multplay!= 1 and play is True:
                        multplay = 1
                    elif event.key == pygame.K_3 and multplay!= 3 and play is True:
                        multplay = 3
                    elif event.key == pygame.K_7 and multplay!= 7 and play is True:
                        multplay = 7
                # click ecra mostrar distancia
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    click += 1
                    screen.fill((0, 0, 0))
                    rightleftclickordrawagain(screen, data1input, data2input, image1, image2, center_origin, center_origin2, i)
                    drawcar(screen, data1input, data2input, image1, center_origin, center_origin2, i)
                if click == 1:
                    pos1 = pos
                elif click == 2:
                    pos2 = pos
                    distancemouseclick(screen, color, font, pos1, pos2)
                    click = 0
                    pygame.display.flip()
            # Texto que aparece em ambos os modos
            screen.blit(textmode, (0, 700))
            # Modo normal de ambos os trajeto
            if not modedit:
                play = False
                for i in range(len(data1input["readx"])):
                    if i == (len(data1input["readx"])-1):
                        # Desenha car na ultima posição que ficou no play
                        drawcar(screen, data1input, data2input, image1, center_origin, center_origin2, i)
                    else:
                        drawpath(screen, data1input, data2input, image2, center_origin, center_origin2, i)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        modedit = True
                        i = 0
                        screenfill(screen)
                        drawcar(screen, data1input, data2input, image1, center_origin, center_origin2, i)
                # break
            # Modo de edição
            elif modedit is True:
                if i <= 0:
                    i = 0
                    drawcar(screen, data1input, data2input, image1, center_origin, center_origin2, i)
                elif i >= len(data1input["readx"]):
                    i = data1input["readtick1"][-1]-1
                    drawcar(screen, data1input, data2input, image1, center_origin, center_origin2, i)
                textmult(screen, color, font, totaltick, multtick, i)
                screendistance(screen, data1input, data2input, color, font, i)
                # car 1
                infocar(0,screen, data1input, color, font, textinfcar1, i)
                # car 2
                infocar(160,screen, data2input, color, font, textinfcar2, i)
                # Info ecra edição
                infoscreen(screen, textinfocontroltick, textchangetickvalue, textplay)
                # play
                if play is True and addplay != totaltick:
                    screenfill(screen)
                    screen.blit(textstop, (500, 700))
                    forplay(screen, data1input, data2input, image1, image2, center_origin, center_origin2, addplay)
                    addplay += multplay
                    i = addplay
                    playspeed(multplay)
                    textchangespeedmodplay()
                    if addplay == totaltick:
                        screen.fill((0, 0, 0))
                        rightleftclickordrawagain(screen, data1input, data2input, image1, image2, center_origin, center_origin2, i)
                    elif addplay > totaltick:
                        # Quando o play chega ao valor final
                        addplay = data1input["readtick1"][-1]-1
                        play = False
                        screenfill(screen)
                # Ir para o modo do trajeto completo
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        modedit = False
                        screenfill(screen)
            # Refresh info on screen
            pygame.display.update()
    finally:
        # Delete folder tmp
        shutil.rmtree("tmp", ignore_errors=False, onerror=None)

if __name__ == '__main__':
    loop()
