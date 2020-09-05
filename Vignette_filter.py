import numpy as np 
import cv2


input = cv2.imread('input/strawberry.jpg') 
    
height, width = input_image.shape[:2] 
   
x_gauss = cv2.getGaussianKernel(width,250) 
y_gauss = cv2.getGaussianKernel(height,200) 
    
kernel = x_gauss * y_gauss.T


mask = kernel * 255 / np.linalg.norm(kernel)  
    
output[:,:,0] = input[:,:,0] * mask 
output[:,:,1] = input[:,:,1] * mask 
output[:,:,2] = input[:,:,2] * mask 



cv2.imshow('vignette', output) 
cv2.waitKey(0) 
cv2.destroyAllWindows()