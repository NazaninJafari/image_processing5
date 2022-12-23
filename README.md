# image_processing5

## Part_1 :

on met un filtre flou sur les visages qui vont être détectés...

![Screen shot](part_1/images/20221213_231445.jpg)

## Part_2 :

cela augmente le contraste de cadre du webcam et puis détermine la couleur qui est plus marqué entre ces trois(noir, blanc et gris)


## Part_3 :

j'ai utilisé d'autre façon au lieu de (cv2.equalizeHist) 
pour augmenter le contrast. et vous pouvez voir la difference :

image d'origin


![Screen Shot](part_3/low-contrast-2.jpg)


(cv2.equalizeHist)


![Screen Shot](part_3/highCont_image.jpg)


(cv2.convertScaleAbs(image, alpha=alpha, beta=beta))


![Screen Shot](part_3/highCont_image2.jpg)

---
## Part_4 :

il faut séparer les nombres dans la photo du Sudoku

### image d'entrée après avoir augmenté le contraste:

![Screen Shot](part_4/equ_img.jpg)

### la sortie:

Ce sont des petits photos qui comportent les nombres :

![Screen Shot](part_4/output_img/pic1.jpg) ![Screen Shot](part_4/output_img/pic2.jpg) ![Screen Shot](part_4/output_img/pic3.jpg)   ....
