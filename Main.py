import cv2
import mediapipe as mp                                                          ##construído pelo google

##vincular webcam ao python
webcam = cv2.VideoCapture(0)

##iniclializando o midiapipe
reconhecimento_maos = mp.solutions.hands
desenho_mp = mp.solutions.drawing_utils
maos = reconhecimento_maos.Hands()

if webcam.isOpened():                                                           #verificando se conseguiu se conectar
    ##lendo webcan
    validacao, frame = webcam.read()

    ##pegando vários frames
    while validacao:                                                            #enquanto for verdadeiro, posso colocar while validacao == True:
        validacao, frame = webcam.read()
        frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)                       ##Convertendo cores em BGR do open cv para RGB do mp
        lista_maos = maos.process(frameRGB)
        if lista_maos.multi_hand_landmarks:
            for mao in lista_maos.multi_hand_landmarks:
                desenho_mp.draw_landmarks(frame, mao, reconhecimento_maos.HAND_CONNECTIONS)

        # mostrar o frame da webcam que o python está vendo
        cv2.imshow("Video da Webcam", frame)

        #mandar o código esperar um pouco - de forma inteligente
        tecla = cv2.waitKey(2)                                                  ##tempo de espera em milesegundos e além disso, armazena a tecla pressionada

        #sair do código se eu clicar no ESC
        if tecla == 27:                                                         ##tecla 27 = esq no opencv
            break

    #reconhecer as maos usando mediapipe

webcam.release()   ##desfazer conexão com webcan
cv2.destroyAllWindows()   #fecha a tela