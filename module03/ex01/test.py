from ImageProcessor import ImageProcessor

if __name__ == '__main__':
    img = ImageProcessor()
    arr = img.load("non_existing_file.png")
    print(arr)
    arr = img.load("../resources/empty_file.png")
    print(arr)
    arr = img.load("../resources/42AI.png")
    print(arr)
    img.display(arr)
