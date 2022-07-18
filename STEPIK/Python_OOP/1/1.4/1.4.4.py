class MediaPlayer:
    def open(self, file):
        self.filename = file
    
    def play(self):
        return f"Воспроизведение {self.file}"

media1 = MediaPlayer()
media2 = MediaPlayer()

media1.open("filemedia1")
media2.open("filemedia2")

print(media1.play())
print(media2.play())

