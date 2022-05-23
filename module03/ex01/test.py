from ImageProcessor import ImageProcessor
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook

img = ImageProcessor()
arr = img.load("non_existing_file.png")
print(arr)
arr = img.load("../resources/empty_file.png")
print(arr)
arr = img.load("../resources/42AI.png")
print(arr)
img.display(arr)
