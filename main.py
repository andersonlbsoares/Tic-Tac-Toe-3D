import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import socket
import subprocess

pygame.init()
display = (800, 600)

tela = pygame.display.set_mode(display, DOUBLEBUF | OPENGL | OPENGLBLIT)

matriz = [
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0, 0], [0, 0, 0], [0, 0, 0]],
    [[0, 0 ,0], [0 ,0 ,0], [0, 0, 1]]
]

input_text = ""
PORT = 1234
HOST = input_text
exibir = 0
player = 1
cor_player = 1  



def iluminacao():
    glEnable(GL_DEPTH_TEST)
    glEnable(GL_LIGHTING)
    glEnable(GL_LIGHT0)
    glLightfv(GL_LIGHT0, GL_POSITION, (0.0, 1.0, 1.0, 0.0))
    glLightfv(GL_LIGHT0, GL_AMBIENT, (0.2, 0.2, 0.2, 1.0))
    glLightfv(GL_LIGHT0, GL_DIFFUSE, (1.0, 1.0, 1.0, 1.0))

def desligaIluminacao():
    glDisable(GL_LIGHTING)
    glDisable(GL_LIGHT0)
    glDisable(GL_DEPTH_TEST)

def broadcast():
    BROADCAST_IP = "255.255.255.255"
    BROADCAST_PORT = 1234  
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #Cria um socket UDP
    client_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1) #Configura o socket para broadcast
    client_socket.bind(("", 0))  # O cliente usa uma porta aleatória, Ip vazio para receber mensagens de qualquer endereço (SO toma de conta)
    client_socket.sendto(b"broadcast", (BROADCAST_IP, BROADCAST_PORT)) #Envia a mensagem de broadcast
    data, server_address = client_socket.recvfrom(1024) #Recebe a resposta do servidor
    server_ip = data.decode() #Decodifica a mensagem
    client_socket.close() #Fecha o socket
    return server_ip #Retorna o IP do servidor
    
def menuInferior(): 
    glMatrixMode(GL_PROJECTION)
    glPushMatrix()
    glLoadIdentity()
    gluOrtho2D(0, 800, 0, 600)

    glMatrixMode(GL_MODELVIEW)
    glPushMatrix()
    glLoadIdentity()

    glColor3f(0.4, 0.4, 0.4)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 120)
    glVertex2f(120, 120)
    glVertex2f(120, 0)
    glEnd()
    
    # Quadrado 1

    if (matriz[3][2][2] != player):
        glColor3f(0.7,0.7,0.7)
    else:
        glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(30, 30)
    glVertex2f(30, 0)
    glEnd()

    # Quadrado 2
    if (matriz[3][2][2] != player):
        glColor3f(0.7,0.7,0.7)
    else:
        glColor3f(1, 1, 1)
    glTranslatef(40, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(30, 30)
    glVertex2f(30, 0)
    glEnd()

    # Quadrado 3
    if (matriz[3][2][2] != player):
        glColor3f(0.7,0.7,0.7)
    else:
        glColor3f(0, 0, 0)
    glTranslatef(40, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(30, 30)
    glVertex2f(30, 0)
    glEnd()

    glLoadIdentity()
    glTranslatef(0, 40, 0)

    # Quadrado 4

    if (matriz[3][2][2] != player):
        glColor3f(0.7,0.7,0.7)
    else:
        glColor3f(1, 1, 1)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(30, 30)
    glVertex2f(30, 0)
    glEnd()

    # Quadrado 5
    if (matriz[3][2][2] != player):
        glColor3f(0.7,0.7,0.7)
    else:
        glColor3f(0, 0, 0)
    glTranslatef(40, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(30, 30)
    glVertex2f(30, 0)
    glEnd()

    # Quadrado 6
    if (matriz[3][2][2] != player):
        glColor3f(0.7,0.7,0.7)
    else:
        glColor3f(1, 1, 1)
    glTranslatef(40, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(30, 30)
    glVertex2f(30, 0)
    glEnd()

    glLoadIdentity()
    glTranslatef(0, 80, 0)

    # Quadrado 7
    if (matriz[3][2][2] != player):
        glColor3f(0.7,0.7,0.7)
    else:
        glColor3f(0, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(30, 30)
    glVertex2f(30, 0)
    glEnd()

    # Quadrado 8

    if (matriz[3][2][2] != player):
        glColor3f(0.7,0.7,0.7)
    else:
        glColor3f(1, 1, 1)
    glTranslatef(40, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(30, 30)
    glVertex2f(30, 0)
    glEnd()

    # Quadrado 9
    if (matriz[3][2][2] != player):
        glColor3f(0.7,0.7,0.7)
    else:
        glColor3f(0, 0, 0)
    glTranslatef(40, 0, 0)
    glBegin(GL_QUADS)
    glVertex2f(0, 0)
    glVertex2f(0, 30)
    glVertex2f(30, 30)
    glVertex2f(30, 0)
    glEnd()

    if player != 0:
        if cor_player == 1:
            desenhar_texto("Player " + str(player), (-65, 50, 0), (0, 0, 255), 32)
        else:
            desenhar_texto("Player " + str(player), (-65, 50, 0), (255, 0, 0), 32)
    glPopMatrix()
    glMatrixMode(GL_PROJECTION)
    glPopMatrix()
    glMatrixMode(GL_MODELVIEW)

def desenhar_esferas(matriz):
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if matriz[i][j][k] != 0:  # Verifica se o valor é diferente de 0
                    if matriz[i][j][k] == 1:
                        glColor3f(0.0, 0.0, 1.0)
                        glPushMatrix()
                        glTranslatef(i+.55, j, k+.55)
                        glEnable(GL_COLOR_MATERIAL)  # Habilita o uso de cor do material
                        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)  # Define as faces frontais e traseiras para receber a cor do material
                        quadradic = gluNewQuadric()
                        gluSphere(quadradic, 0.25, 20, 20)
                        glDisable(GL_COLOR_MATERIAL)
                        glPopMatrix()
                        glClearColor(0.4, 0.4, 0.4, 1.0)

                    elif matriz[i][j][k] == 2:
                        glColor3f(1.0, 0.0, 0.0)
                        glPushMatrix()
                        glTranslatef(i+.55, j, k+.55)
                        glEnable(GL_COLOR_MATERIAL)  # Habilita o uso de cor do material
                        glColorMaterial(GL_FRONT_AND_BACK, GL_AMBIENT_AND_DIFFUSE)  # Define as faces frontais e traseiras para receber a cor do material
                        quadradic = gluNewQuadric()
                        gluSphere(quadradic, 0.25, 20, 20)
                        glDisable(GL_COLOR_MATERIAL)
                        glPopMatrix()
                        glClearColor(0.4, 0.4, 0.4, 1.0)

def plano():
    # Desenha um chão dividido em 9 partes com cores diferentes
    for i in range(3):
        for j in range(3):
            x_start = i 
            x_end = i + 1
            y_start = j 
            y_end = j + 1
            
            # Define a cor do quadrado com base na posição
            if (i + j) % 2 == 0:
                glColor3f(0, 0, 0)  # Cor 1
            else:
                glColor3f(1, 1, 1)  # Cor 2
            
            glBegin(GL_QUADS)
            glVertex3f(x_start, -.3, y_start)
            glVertex3f(x_start, -.3, y_end)
            glVertex3f(x_end, -.3, y_end)
            glVertex3f(x_end, -.3, y_start)
            glEnd()

def desenhar_texto(text, position, fundo, tamanho):
    font = pygame.font.Font(None, tamanho)
    text_surface = font.render(text, True, (255, 255, 255), fundo)
    text_data = pygame.image.tostring(text_surface, "RGBA", True)
    width, height = text_surface.get_size()

    glRasterPos3f(position[0], position[1], position[2])
    glDrawPixels(width, height, GL_RGBA, GL_UNSIGNED_BYTE, text_data)

def checar_zeros():
    for i in range(3):
        for j in range(3):
            for k in range(3):
                if matriz[i][j][k] == 0:
                    return True
    return False

def checar_vitoria():
    count_1 = 0
    count_2 = 0

    # Verificar arestas nas linhas, colunas e profundidades
    for i in range(3):
        for j in range(3):
            # Verificar arestas nas linhas
            if matriz[i][j][0] == matriz[i][j][1] == matriz[i][j][2]:
                if matriz[i][j][0] == 1:
                    count_1 += 1
                elif matriz[i][j][0] == 2:
                    count_2 += 1

            # Verificar arestas nas colunas
            if matriz[j][i][0] == matriz[j][i][1] == matriz[j][i][2]:
                if matriz[j][i][0] == 1:
                    count_1 += 1
                elif matriz[j][i][0] == 2:
                    count_2 += 1

            # Verificar arestas nas profundidades
            if matriz[0][j][i] == matriz[1][j][i] == matriz[2][j][i]:
                if matriz[0][j][i] == 1:
                    count_1 += 1
                elif matriz[0][j][i] == 2:
                    count_2 += 1

    # Verificar arestas nas diagonais
    for i in range(3):
        if matriz[0][i][0] == matriz[1][i][1] == matriz[2][i][2]:
            if matriz[0][i][0] == 1:
                count_1 += 1
            elif matriz[0][i][0] == 2:
                count_2 += 1

        if matriz[2][i][0] == matriz[1][i][1] == matriz[0][i][2]:
            if matriz[2][i][0] == 1:
                count_1 += 1
            elif matriz[2][i][0] == 2:
                count_2 += 1

    # Verificar arestas nas diagonais das profundidades
    if matriz[0][0][0] == matriz[1][1][1] == matriz[2][2][2]:
        if matriz[0][0][0] == 1:
            count_1 += 1
        elif matriz[0][0][0] == 2:
            count_2 += 1

    if matriz[2][0][0] == matriz[1][1][1] == matriz[0][2][2]:
        if matriz[2][0][0] == 1:
            count_1 += 1
        elif matriz[2][0][0] == 2:
            count_2 += 1

    if matriz[0][2][0] == matriz[1][1][1] == matriz[2][0][2]:
        if matriz[0][2][0] == 1:
            count_1 += 1
        elif matriz[0][2][0] == 2:
            count_2 += 1

    if matriz[2][2][0] == matriz[1][1][1] == matriz[0][0][2]:
        if matriz[2][2][0] == 1:
            count_1 += 1
        elif matriz[2][2][0] == 2:
            count_2 += 1

    # Determinar o número vencedor
    if count_1 > count_2:
        vencedor = 1
    elif count_2 > count_1:
        vencedor = 2
    else:
        vencedor = None

    return vencedor, count_1, count_2

def main():
    global input_text
    global exibir
    global player
    global matriz
    global cor_player
    global PORT
    global HOST

    abrir_conexao = 0
    camera_rotation_x = 0
    camera_rotation_y = 0
    camera_translation_x = 0
    camera_translation_y = 0
    camera_translation_z = 0
    background_color = (0.5, 0.5, 0.5)
    abrir_servidor = True

    checar_vencedor = 1
    
    glMatrixMode(GL_PROJECTION)
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(-1, -1, -7)
    
    while True:

        glRotatef(camera_rotation_x*10, 1, 0, 0)
        glRotatef(camera_rotation_y*10, 0, 1, 0)
        glTranslatef(camera_translation_x, camera_translation_y, camera_translation_z)
      
        for event in pygame.event.get(): # Interações com a janela

            if event.type == pygame.QUIT: #Quitar
                pygame.quit()
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exibir == 2 and matriz[3][2][2] == player: #Selecionar jogada no menu
                

                if event.pos[0] >= 0 and event.pos[0] <= 30 and event.pos[1] >= 490 + 0 and event.pos[1] <= 490 + 30:
                    if (matriz[0][0][0] == 0):matriz[0][0][0] = cor_player 
                    elif (matriz[0][1][0] == 0):matriz[0][1][0] = cor_player
                    elif (matriz[0][2][0] == 0):matriz[0][2][0] = cor_player


                elif event.pos[0] >= 40 and event.pos[0] <= 70 and event.pos[1] >= 490 + 0 and event.pos[1] <= 490 + 30:
                    if (matriz[1][0][0] == 0):matriz[1][0][0] = cor_player
                    elif (matriz[1][1][0] == 0):matriz[1][1][0] = cor_player
                    elif (matriz[1][2][0] == 0):matriz[1][2][0] = cor_player

                elif event.pos[0] >= 80 and event.pos[0] <= 110 and event.pos[1] >= 490 + 0 and event.pos[1] <= 490 + 30:
                    if (matriz[2][0][0] == 0):matriz[2][0][0] = cor_player
                    elif (matriz[2][1][0] == 0):matriz[2][1][0] = cor_player
                    elif (matriz[2][2][0] == 0):matriz[2][2][0] = cor_player

                elif event.pos[0] >= 0 and event.pos[0] <= 30 and event.pos[1] >= 490 + 40 and event.pos[1] <= 490 + 70:
                    if (matriz[0][0][1] == 0):matriz[0][0][1] = cor_player
                    elif (matriz[0][1][1] == 0):matriz[0][1][1] = cor_player
                    elif (matriz[0][2][1] == 0):matriz[0][2][1] = cor_player
                
                elif event.pos[0] >= 40 and event.pos[0] <= 70 and event.pos[1] >= 490 + 40 and event.pos[1] <= 490 + 70:
                    if (matriz[1][0][1] == 0):matriz[1][0][1] = cor_player
                    elif (matriz[1][1][1] == 0):matriz[1][1][1] = cor_player
                    elif (matriz[1][2][1] == 0):matriz[1][2][1] = cor_player

                elif event.pos[0] >= 80 and event.pos[0] <= 110 and event.pos[1] >= 490 + 40 and event.pos[1] <= 490 + 70:
                    if (matriz[2][0][1] == 0):matriz[2][0][1] = cor_player
                    elif (matriz[2][1][1] == 0):matriz[2][1][1] = cor_player
                    elif (matriz[2][2][1] == 0):matriz[2][2][1] = cor_player

                elif event.pos[0] >= 0 and event.pos[0] <= 30 and event.pos[1] >= 490 + 80 and event.pos[1] <= 490 + 110:
                    if (matriz[0][0][2] == 0):matriz[0][0][2] = cor_player
                    elif (matriz[0][1][2] == 0):matriz[0][1][2] = cor_player
                    elif (matriz[0][2][2] == 0):matriz[0][2][2] = cor_player

                elif event.pos[0] >= 40 and event.pos[0] <= 70 and event.pos[1] >= 490 + 80 and event.pos[1] <= 490 + 110:
                    if (matriz[1][0][2] == 0):matriz[1][0][2] = cor_player
                    elif (matriz[1][1][2] == 0):matriz[1][1][2] = cor_player
                    elif (matriz[1][2][2] == 0):matriz[1][2][2] = cor_player

                elif event.pos[0] >= 80 and event.pos[0] <= 110 and event.pos[1] >= 490 + 80 and event.pos[1] <= 490 + 110:
                    if (matriz[2][0][2] == 0):matriz[2][0][2] = cor_player
                    elif (matriz[2][1][2] == 0):matriz[2][1][2] = cor_player
                    elif (matriz[2][2][2] == 0):matriz[2][2][2] = cor_player

                #checa se apertou um dos 9 quadrados
                if event.pos[0] >= 0 and event.pos[0] <= 110 and event.pos[1] >= 490 and event.pos[1] <= 490 + 110:
                    if (matriz[3][2][2] == 1):
                        matriz[3][2][2] = 2
                    else:
                        matriz[3][2][2] = 1
                   
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exibir == 0: #Botao hospedar ou conectar
                if event.pos[0] >= 50 and event.pos[0] <= 300 and event.pos[1] >= 340 and event.pos[1] <= 380:
                    exibir = 4
                elif event.pos[0] >= 450 and event.pos[0] <= 550 and event.pos[1] >= 340 and event.pos[1] <= 380:
                    exibir = 1

            elif event.type == pygame.MOUSEMOTION: #Rotação e translação da camera
                x, y = event.rel

                if event.buttons[0] == 1:  # Botão esquerdo
                    camera_rotation_x -= y / 100
                    camera_rotation_y += x / 100
                elif event.buttons[2] == 1:  # Botão direito
                    camera_translation_x += x / 100
                    camera_translation_y -= y / 100
                
            elif event.type == pygame.MOUSEBUTTONDOWN:#Zoom da camera (translação no eixo z)
                if event.button == 4:  # Scroll para cima
                    camera_translation_z += 0.1
                elif event.button == 5:  # Scroll para baixo
                    camera_translation_z -= 0.1
            
            elif event.type == pygame.KEYDOWN and exibir == 1:# Tela de conexão, digitar o ip
                if event.key == pygame.K_RETURN:
                    ip_server = broadcast()
                    exibir = 2
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode
            
            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and exibir == 1: #Botao conectar automaticamente
                if event.pos[0] >= 140 and event.pos[0] <= 600 and event.pos[1] >= 466 and event.pos[1] <= 500:
                    ip_server = broadcast()
                    input_text = ip_server
                    exibir = 2

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT) #Limpa a tela

        #Telas do jogo

        if (exibir == 0): #Menu
            desenhar_texto("Jogo da Velha 3D", (-.6, 2, 0),(0,0,0),56)
            desenhar_texto("Hospedar", (-1, 0.3, 0),(125,255,125),32)
            desenhar_texto("Conectar", (1.5, 0.3, 0),(125,125,255),32)

        elif(exibir == 1): #Conectar
            desenhar_texto("Jogo da Velha 3D", (0, 3, 0), (0,0,0),32)
            desenhar_texto("Digite o ip do host: " + input_text, (-1.5, 1, 0),(0,0,0),32)
            desenhar_texto("Ou clique no botão abaixo para buscar automaticamente na rede", (-2.5, 0, 0),(0,0,0),32)
            desenhar_texto("CONEXÃO AUTOMÁTICA", (-1.5, -1, 0),(125,255,125),56)

        elif exibir == 2:   #Conectado

            if abrir_conexao == 0:
                glRotatef(15, 1, 0, 0)
                HOST = input_text  # IP do host
                print("Conectando ao servidor", HOST, "na porta", PORT)
                
                client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client_socket.connect((HOST, PORT))
                data = client_socket.recv(1024)
                player = int(data.decode())
                cor_player = player
                abrir_conexao = 1

            if checar_zeros() == False:
                exibir = 5 

            message = str(matriz)
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024).decode()
            if (matriz != eval(data)):
                print (player, cor_player, data)
                matriz = eval(data)
            

           
            glDisable(GL_DEPTH_TEST)
            menuInferior()
            glEnable(GL_DEPTH_TEST)
            plano()  

            iluminacao()
            desenhar_esferas(matriz)
            desligaIluminacao()

        elif exibir == 3: # Caso de teste
            glDisable(GL_DEPTH_TEST)
            menuInferior()
            glEnable(GL_DEPTH_TEST)
            plano()  

            iluminacao()
            desenhar_esferas(matriz)
            desligaIluminacao()
            if checar_zeros() == False:
                exibir = 5 
        
        elif exibir == 4: # Hospedar
            HOST = socket.gethostbyname(socket.gethostname())
            texto = "Você está hospedando essa partida no IP " + str(HOST) + " e na porta " + str(PORT)
            desenhar_texto(texto, (-2.5, 1, 0), (0,0,0),32)
            desenhar_texto("Aguardando conexão...", (-.5, -1, 0), (0,0,0),32)

            if abrir_servidor:
                comando = ['python', "server.py"]
                subprocess.Popen(comando)
                abrir_servidor = False
                input_text = HOST
                exibir = 2
            
        elif exibir == 5: # Vitoria
            if checar_vencedor == 1:
                vencedor, count_1, count_2 = checar_vitoria()
                checar_vencedor = 0            
            if (vencedor == player):
                desenhar_texto("Você venceu!", (-1.5, 2, 0), (0,0,0),32)
            elif (vencedor == None):
                desenhar_texto("Deu velha!", (-1.5, 2, 0), (0,0,0),32)
            else:
                desenhar_texto("Você perdeu!", (-1.5, 2, 0), (0,0,0),32)

            if (vencedor != None):
                desenhar_texto("O vencedor é o player " + str(vencedor), (-1.5, 1, 0), (0,0,0),32)
            desenhar_texto("Player 1 fez " + str(count_1)+" arestas", (-1.5, 0, 0), (0,0,0),32)
            desenhar_texto("Player 2 fez " + str(count_2)+ " arestas", (-1.5, -1, 0), (0,0,0),32)
            

            message = str(matriz)
            client_socket.sendall(message.encode())
            data = client_socket.recv(1024).decode()

        glClearColor(*background_color, 1.0) 
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity() 

        pygame.display.flip()
        pygame.time.wait(10)

main()