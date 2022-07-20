class ImageFileAcceptor:
    def __init__(self, extension):
        self.extension = extension

    def __call__(self, file):
        return file.split('.')[1] in self.extension


filenames = ["boat.jpg", "web.png", "text.txt", "python.doc", "ava.jpg", "forest.jpeg", "eq_1.png", "eq_2.png"]
acceptor = ImageFileAcceptor(('jpg', 'bmp', 'jpeg'))
image_filenames = filter(acceptor, filenames)
print(list(image_filenames))  # ["boat.jpg", "ava.jpg", "forest.jpeg"]