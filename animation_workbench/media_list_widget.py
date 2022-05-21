# coding=utf-8
"""Widget for managing a list of media in the AnimationWorkbench."""

__copyright__ = "Copyright 2022, Tim Sutton"
__license__ = "GPL version 3"
__email__ = "tim@kartoza.com"
__revision__ = "$Format:%H$"

from qgis.PyQt.QtWidgets import QWidget, QSizePolicy
from qgis.PyQt.QtCore import pyqtSignal
from qgis.PyQt.QtCore import Qt
from typing import Optional

from PyQt5.QtMultimedia import QMediaContent, QMediaPlayer
from PyQt5.QtMultimediaWidgets import QVideoWidget
from qgis.PyQt.QtCore import pyqtSlot, QUrl
from qgis.PyQt.QtGui import QIcon, QPixmap, QImage
from qgis.PyQt.QtWidgets import QFileDialog, QListWidgetItem
from .utilities import get_ui_class

FORM_CLASS = get_ui_class("media_list_widget_base.ui")


class MediaListWidget(QWidget, FORM_CLASS):
    """
    A widget for managing a list of media.
    """

    def __init__(self, media_type="images", parent=None):
        """Constructor for media_list_widget.

        :media_type: Types of media that can be managed. Valid options are
            "images", "images and movies", "movies", "sound".
        :type media_type: str

        :param parent: Parent widget of this widget.
        :type parent: QWidget
        """
        QWidget.__init__(self, parent)
        self.setupUi(self)
        self.media_type = None
        self.media_filter = None
        self.set_media_type(media_type)
        self.media_list.currentRowChanged.connect(self.media_item_selected)
        self.add_media.clicked.connect(self.choose_media_file)
        self.preview.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)

    def set_media_type(self, media_type):
        """Setter for media_type property.

        :media_type: Types of media that can be managed. Valid options are
            "images", "images and movies", "movies", "sound".
        :type media_type: str

        :param parent: Parent widget of this widget.
        :type parent: QWidget
        """
        self.media_type = media_type
        self.images = "JPEG (*.jpg);;PNG (*.png)"
        self.movies = "MOV (*.mov);;MP4 (*.mp4)"
        self.movies_and_images = "JPEG (*.jpg);;PNG (*.png);;MOV (*.mov);;MP4 (*.mp4)"
        self.sounds = "MP3 (*.mp3);;WAV (*.wav)"
        if self.media_type == "movies":
            self.media_filter = self.movies
        if self.media_type == "images":
            self.media_filter = self.images
        if self.media_type == "images and movies":
            self.media_filter == self.movies_and_images
        if self.media_type == "sounds":
            self.media_type == self.sounds

    def media_item_selected(self, current_index):
        value = self.media_list.currentItem().text()
        self.details_label.setText(str(value))

    def choose_media_file(self):
        """
        Asks the user for the a media file path
        """
        # Popup a dialog to request the filename for music backing track
        dialog_title = "Media (jpg, png, mov, mp4) for video"

        # noinspection PyCallByClass,PyTypeChecker
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            dialog_title,
            self.media_filter,
            self.movies_and_images,
        )
        if file_path is None or file_path == "":
            return
        item = QListWidgetItem(file_path)
        item.setData(Qt.UserRole, file_path)
        self.media_list.insertItem(0, item)
        image = QImage(file_path)
        if not image.isNull():
            pixmap = QPixmap.fromImage(image)
            self.preview.setPixmap(
                pixmap.scaled(
                    self.preview.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation
                )
            )
