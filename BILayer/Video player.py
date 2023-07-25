import sys
from PyQt5.QtCore import Qt, QUrl
from PyQt5.QtGui import QPalette, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QPushButton

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 800, 600)

        self.media_player = QMediaPlayer(self)
        self.video_widget = QVideoWidget(self)
        self.media_player.setVideoOutput(self.video_widget)

        layout = QVBoxLayout()
        layout.addWidget(self.video_widget)

        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_video)
        layout.addWidget(self.play_button)

        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def play_video(self):
        file_path = "path_to_your_video.mp4"  # Replace with the path to your video file
        video_url = QUrl.fromLocalFile(file_path)
        media_content = QMediaContent(video_url)
        self.media_player.setMedia(media_content)
        self.media_player.play()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    player = VideoPlayer()
    player.show()

    sys.exit(app.exec_())
