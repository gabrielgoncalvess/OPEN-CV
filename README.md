# Reconhecimento Facial

<p align="center">
  <img src="/face_exemple.png" />
</p>

Este projeto teve o intuito de treinar um modelo de reconhecimento facial para identificar três atores: Christian Bale, Margot Robbie, Tom Welling. O primeiro foi escolhido pela sua extrema mudança de aparência ao longo dos papéis, os outros dois foram escolhidos justamente pelo oposto. Para a detecção de rostos, foi utilizado o Haar Cascade, que pode ser encontrado na biblioteca OpenCV (principal biblioteca de código aberto para a visão computacional) e é um algoritmo de aprendizado baseado em AdaBoost. Este modelo já é previamente treinado. A partir de aproximadamente 30 fotos de cada ator, separadas em pastas diferentes, foi possível treinar o modelo pelo arquivo "faces_train.py".
