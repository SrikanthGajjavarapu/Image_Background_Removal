#import required libraries
from rembg import remove
from PIL import Image

#Creating a function for image background removal purpose
def background_removal(image_path,new_image_path):
    image = Image.open(image_path)     #opening the uploaded image
    new_image = remove(image)          #using rembg to removing the background
    new_image.save(new_image_path)     #after background removal saving new image into new_image_path
    

if __name__ == "__main__":
    image_path = "nameLogo.png"            #original image path
    new_image_path = "new_nameLogo.png"    #new image path

    background_removal(image_path,new_image_path)


