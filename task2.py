#read color image using imread()
#the cv2.IMREAD_COLOR 

# import cv2
# to read the image
# img=cv2.imread(r"C:\Users\pc\Downloads\WhatsApp Image 2024-06-25 at 13.38.28_5676017e.jpg")
#print it shape
# print('image dimesnion',img.shape)

#the above code output this (200,512,3) the img.shape return tuple returns (height,width,number_of_channels) height of image 400 pixels ,width is 640 and there are three color channel in the image

#opencv2 cv2=read image as greyscale
#we read image as a grey scale image.input can be color image or grey scale image

# import cv2
# img=cv2.imread(r"C:\Users\pc\Downloads\WhatsApp Image 2024-06-25 at 13.38.28_5676017e.jpg",cv2.IMREAD_GRAYSCALE)
# print('image_dimensions',img.shape)

#the above code print the image dimension(200,512) means


#opencv cv2-read image with transparency channel
#we read an image with transparency channel.if there is transparency channel in the image,then we can pass
#cv2.IMREAD_UNCHANGED to read the transparency channel along with the color channels

# import cv2
# img=cv2.imread(r"C:\Users\pc\Downloads\WhatsApp Image 2024-06-25 at 13.38.28_5676017e.jpg",cv2.IMREAD_UNCHANGED)
# print('image dimensions',img.shape)



#opencv-show image-imshow()
#we can display an image to the user during the execution of the python opencv application
#to display an image using opencv cv2 library .we can use cv2.imshow() function

#show image using cv2.imshow()

# import cv2

# Read the image
# img = cv2.imread(r"C:\Users\pc\Downloads\WhatsApp Image 2024-06-25 at 13.38.28_5676017e.jpg")

# Check if the image was successfully loaded
# if img is None:
    # print("Error: Could not load image.")
# else:
    # Show the image in a window
    # cv2.imshow('show image in windows', img)
    
    # Wait for a key press indefinitely or for a specified amount of time
    # cv2.waitKey(0)
    
    # Close all OpenCV windows
    # cv2.destroyAllWindows()



#show numpy.ndarray as image using opencv
#i explain an ndarray as image using imshow().we initialize a numpy array of shape(300,300,3) such that it represents 300x300 image with three color channels.125 intial value

import cv2
import numpy as np

#numpy array
ndarray=np.full((300,300,3),125,dtype=np.uint8)
#show image
cv2.imshow('image showing in',ndarray)
cv2.waitKey(0) #waits until a key is preesed
cv2.destroyAllWindows() #destroy the windows showing image