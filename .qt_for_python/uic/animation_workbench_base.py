# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/timlinux/dev/python/QGISAnimationWorkbench/ui/animation_workbench_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_animation_workbench_base(object):
    def setupUi(self, animation_workbench_base):
        animation_workbench_base.setObjectName("animation_workbench_base")
        animation_workbench_base.resize(980, 830)
        self.gridLayout_9 = QtWidgets.QGridLayout(animation_workbench_base)
        self.gridLayout_9.setObjectName("gridLayout_9")
        self.frame = QtWidgets.QFrame(animation_workbench_base)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.frame)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.render_mode_group = QtWidgets.QGroupBox(self.frame)
        self.render_mode_group.setObjectName("render_mode_group")
        self.gridLayout = QtWidgets.QGridLayout(self.render_mode_group)
        self.gridLayout.setObjectName("gridLayout")
        self.radio_planar = QtWidgets.QRadioButton(self.render_mode_group)
        self.radio_planar.setChecked(True)
        self.radio_planar.setObjectName("radio_planar")
        self.gridLayout.addWidget(self.radio_planar, 0, 1, 1, 1)
        self.radio_sphere = QtWidgets.QRadioButton(self.render_mode_group)
        self.radio_sphere.setObjectName("radio_sphere")
        self.gridLayout.addWidget(self.radio_sphere, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.render_mode_group, 2, 0, 1, 1)
        self.output_destination_group = QtWidgets.QGroupBox(self.frame)
        self.output_destination_group.setObjectName("output_destination_group")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.output_destination_group)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.folder_label = QtWidgets.QLabel(self.output_destination_group)
        self.folder_label.setObjectName("folder_label")
        self.gridLayout_6.addWidget(self.folder_label, 0, 0, 1, 1)
        self.folder_edit = QtWidgets.QLineEdit(self.output_destination_group)
        self.folder_edit.setObjectName("folder_edit")
        self.gridLayout_6.addWidget(self.folder_edit, 0, 1, 1, 1)
        self.folder_button = QtWidgets.QToolButton(self.output_destination_group)
        self.folder_button.setObjectName("folder_button")
        self.gridLayout_6.addWidget(self.folder_button, 0, 2, 1, 1)
        self.gridLayout_7.addWidget(self.output_destination_group, 7, 0, 1, 1)
        self.animation_reference_group = QtWidgets.QGroupBox(self.frame)
        self.animation_reference_group.setObjectName("animation_reference_group")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.animation_reference_group)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.layer_combo = gui.QgsMapLayerComboBox(self.animation_reference_group)
        self.layer_combo.setObjectName("layer_combo")
        self.gridLayout_4.addWidget(self.layer_combo, 1, 1, 1, 1)
        self.point_layer_label = QtWidgets.QLabel(self.animation_reference_group)
        self.point_layer_label.setObjectName("point_layer_label")
        self.gridLayout_4.addWidget(self.point_layer_label, 1, 0, 1, 1)
        self.gridLayout_7.addWidget(self.animation_reference_group, 0, 0, 1, 1)
        self.output_options_group = QtWidgets.QGroupBox(self.frame)
        self.output_options_group.setObjectName("output_options_group")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.output_options_group)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.reuse_cache = QtWidgets.QCheckBox(self.output_options_group)
        self.reuse_cache.setObjectName("reuse_cache")
        self.gridLayout_5.addWidget(self.reuse_cache, 0, 0, 1, 2)
        self.radio_gif = QtWidgets.QRadioButton(self.output_options_group)
        self.radio_gif.setObjectName("radio_gif")
        self.gridLayout_5.addWidget(self.radio_gif, 1, 0, 1, 1)
        self.rad_movie = QtWidgets.QRadioButton(self.output_options_group)
        self.rad_movie.setChecked(True)
        self.rad_movie.setObjectName("rad_movie")
        self.gridLayout_5.addWidget(self.rad_movie, 1, 1, 1, 1)
        self.gridLayout_7.addWidget(self.output_options_group, 6, 0, 1, 1)
        self.animation_frames_group = QtWidgets.QGroupBox(self.frame)
        self.animation_frames_group.setObjectName("animation_frames_group")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.animation_frames_group)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.hover_frames_label = QtWidgets.QLabel(self.animation_frames_group)
        self.hover_frames_label.setObjectName("hover_frames_label")
        self.gridLayout_8.addWidget(self.hover_frames_label, 1, 0, 1, 1)
        self.hover_frames_spin = QtWidgets.QSpinBox(self.animation_frames_group)
        self.hover_frames_spin.setMaximum(999)
        self.hover_frames_spin.setProperty("value", 15)
        self.hover_frames_spin.setObjectName("hover_frames_spin")
        self.gridLayout_8.addWidget(self.hover_frames_spin, 1, 1, 1, 1)
        self.point_frames_label = QtWidgets.QLabel(self.animation_frames_group)
        self.point_frames_label.setObjectName("point_frames_label")
        self.gridLayout_8.addWidget(self.point_frames_label, 0, 0, 1, 1)
        self.point_frames_spin = QtWidgets.QSpinBox(self.animation_frames_group)
        self.point_frames_spin.setMaximum(999)
        self.point_frames_spin.setProperty("value", 15)
        self.point_frames_spin.setObjectName("point_frames_spin")
        self.gridLayout_8.addWidget(self.point_frames_spin, 0, 1, 1, 1)
        self.gridLayout_7.addWidget(self.animation_frames_group, 5, 0, 1, 1)
        self.easings_group = QtWidgets.QGroupBox(self.frame)
        self.easings_group.setObjectName("easings_group")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.easings_group)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.zoom_easing_combo = QtWidgets.QComboBox(self.easings_group)
        self.zoom_easing_combo.setEnabled(False)
        self.zoom_easing_combo.setObjectName("zoom_easing_combo")
        self.gridLayout_2.addWidget(self.zoom_easing_combo, 1, 2, 1, 1)
        self.pan_preview_legend = QtWidgets.QWidget(self.easings_group)
        self.pan_preview_legend.setMinimumSize(QtCore.QSize(25, 25))
        self.pan_preview_legend.setMaximumSize(QtCore.QSize(25, 25))
        self.pan_preview_legend.setAutoFillBackground(False)
        self.pan_preview_legend.setStyleSheet("background: yellow; border-radius: 3px;")
        self.pan_preview_legend.setObjectName("pan_preview_legend")
        self.gridLayout_2.addWidget(self.pan_preview_legend, 0, 1, 1, 1)
        self.pan_easing_combo = QtWidgets.QComboBox(self.easings_group)
        self.pan_easing_combo.setEnabled(False)
        self.pan_easing_combo.setObjectName("pan_easing_combo")
        self.gridLayout_2.addWidget(self.pan_easing_combo, 0, 2, 1, 1)
        self.enable_zoom_easing = QtWidgets.QCheckBox(self.easings_group)
        self.enable_zoom_easing.setObjectName("enable_zoom_easing")
        self.gridLayout_2.addWidget(self.enable_zoom_easing, 1, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.easings_group)
        self.widget_2.setMinimumSize(QtCore.QSize(25, 25))
        self.widget_2.setMaximumSize(QtCore.QSize(25, 25))
        self.widget_2.setStyleSheet("background: cyan; border-radius: 3px;")
        self.widget_2.setObjectName("widget_2")
        self.gridLayout_2.addWidget(self.widget_2, 1, 1, 1, 1)
        self.enable_pan_easing = QtWidgets.QCheckBox(self.easings_group)
        self.enable_pan_easing.setObjectName("enable_pan_easing")
        self.gridLayout_2.addWidget(self.enable_pan_easing, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.easings_group, 3, 0, 1, 1)
        self.zoom_range_group = QtWidgets.QGroupBox(self.frame)
        self.zoom_range_group.setEnabled(False)
        self.zoom_range_group.setObjectName("zoom_range_group")
        self.gridLayout_10 = QtWidgets.QGridLayout(self.zoom_range_group)
        self.gridLayout_10.setObjectName("gridLayout_10")
        self.scale_range = gui.QgsScaleRangeWidget(self.zoom_range_group)
        self.scale_range.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.scale_range.setObjectName("scale_range")
        self.gridLayout_10.addWidget(self.scale_range, 0, 0, 1, 1)
        self.gridLayout_7.addWidget(self.zoom_range_group, 4, 0, 1, 1)
        self.gridLayout_9.addWidget(self.frame, 0, 0, 1, 1)
        self.preview_frame = QtWidgets.QFrame(animation_workbench_base)
        self.preview_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.preview_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.preview_frame.setLineWidth(0)
        self.preview_frame.setObjectName("preview_frame")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.preview_frame)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.output_log_label = QtWidgets.QLabel(self.preview_frame)
        self.output_log_label.setObjectName("output_log_label")
        self.gridLayout_3.addWidget(self.output_log_label, 2, 0, 1, 1)
        self.preview_stack = QtWidgets.QStackedWidget(self.preview_frame)
        self.preview_stack.setObjectName("preview_stack")
        self.preview_page = QtWidgets.QWidget()
        self.preview_page.setObjectName("preview_page")
        self.gridLayout_11 = QtWidgets.QGridLayout(self.preview_page)
        self.gridLayout_11.setObjectName("gridLayout_11")
        self.current_frame_preview_label = QtWidgets.QLabel(self.preview_page)
        self.current_frame_preview_label.setObjectName("current_frame_preview_label")
        self.gridLayout_11.addWidget(self.current_frame_preview_label, 0, 0, 1, 1)
        self.current_frame_preview = QtWidgets.QLabel(self.preview_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.current_frame_preview.sizePolicy().hasHeightForWidth())
        self.current_frame_preview.setSizePolicy(sizePolicy)
        self.current_frame_preview.setMinimumSize(QtCore.QSize(250, 150))
        self.current_frame_preview.setMaximumSize(QtCore.QSize(9999999, 999999))
        self.current_frame_preview.setText("")
        self.current_frame_preview.setScaledContents(True)
        self.current_frame_preview.setAlignment(QtCore.Qt.AlignCenter)
        self.current_frame_preview.setObjectName("current_frame_preview")
        self.gridLayout_11.addWidget(self.current_frame_preview, 1, 0, 1, 1)
        self.preview_stack.addWidget(self.preview_page)
        self.video_page = QtWidgets.QWidget()
        self.video_page.setObjectName("video_page")
        self.gridLayout_12 = QtWidgets.QGridLayout(self.video_page)
        self.gridLayout_12.setObjectName("gridLayout_12")
        self.video_preview_label = QtWidgets.QLabel(self.video_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_preview_label.sizePolicy().hasHeightForWidth())
        self.video_preview_label.setSizePolicy(sizePolicy)
        self.video_preview_label.setObjectName("video_preview_label")
        self.gridLayout_12.addWidget(self.video_preview_label, 0, 0, 1, 3)
        self.play_button = QtWidgets.QToolButton(self.video_page)
        self.play_button.setObjectName("play_button")
        self.gridLayout_12.addWidget(self.play_button, 2, 0, 1, 1)
        self.video_preview_widget = QtWidgets.QWidget(self.video_page)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.video_preview_widget.sizePolicy().hasHeightForWidth())
        self.video_preview_widget.setSizePolicy(sizePolicy)
        self.video_preview_widget.setObjectName("video_preview_widget")
        self.gridLayout_12.addWidget(self.video_preview_widget, 1, 0, 1, 3)
        self.video_slider = QtWidgets.QSlider(self.video_page)
        self.video_slider.setOrientation(QtCore.Qt.Horizontal)
        self.video_slider.setObjectName("video_slider")
        self.gridLayout_12.addWidget(self.video_slider, 2, 1, 1, 1)
        self.preview_stack.addWidget(self.video_page)
        self.gridLayout_3.addWidget(self.preview_stack, 1, 0, 1, 2)
        self.status_stack = QtWidgets.QStackedWidget(self.preview_frame)
        self.status_stack.setObjectName("status_stack")
        self.easing_status_page = QtWidgets.QWidget()
        self.easing_status_page.setObjectName("easing_status_page")
        self.gridLayout_13 = QtWidgets.QGridLayout(self.easing_status_page)
        self.gridLayout_13.setObjectName("gridLayout_13")
        self.pan_easing_preview_label = QtWidgets.QLabel(self.easing_status_page)
        self.pan_easing_preview_label.setObjectName("pan_easing_preview_label")
        self.gridLayout_13.addWidget(self.pan_easing_preview_label, 0, 0, 1, 1)
        self.zoom_easing_preview_label = QtWidgets.QLabel(self.easing_status_page)
        self.zoom_easing_preview_label.setObjectName("zoom_easing_preview_label")
        self.gridLayout_13.addWidget(self.zoom_easing_preview_label, 0, 1, 1, 1)
        self.pan_easing_preview = QtWidgets.QWidget(self.easing_status_page)
        self.pan_easing_preview.setMinimumSize(QtCore.QSize(250, 150))
        self.pan_easing_preview.setObjectName("pan_easing_preview")
        self.gridLayout_13.addWidget(self.pan_easing_preview, 1, 0, 1, 1)
        self.zoom_easing_preview = QtWidgets.QWidget(self.easing_status_page)
        self.zoom_easing_preview.setMinimumSize(QtCore.QSize(250, 150))
        self.zoom_easing_preview.setObjectName("zoom_easing_preview")
        self.gridLayout_13.addWidget(self.zoom_easing_preview, 1, 1, 1, 1)
        self.status_stack.addWidget(self.easing_status_page)
        self.job_progress_page = QtWidgets.QWidget()
        self.job_progress_page.setObjectName("job_progress_page")
        self.gridLayout_14 = QtWidgets.QGridLayout(self.job_progress_page)
        self.gridLayout_14.setObjectName("gridLayout_14")
        self.queue_lcd = QtWidgets.QLCDNumber(self.job_progress_page)
        self.queue_lcd.setObjectName("queue_lcd")
        self.gridLayout_14.addWidget(self.queue_lcd, 0, 0, 1, 1)
        self.active_lcd = QtWidgets.QLCDNumber(self.job_progress_page)
        self.active_lcd.setObjectName("active_lcd")
        self.gridLayout_14.addWidget(self.active_lcd, 0, 1, 1, 1)
        self.completed_lcd = QtWidgets.QLCDNumber(self.job_progress_page)
        self.completed_lcd.setObjectName("completed_lcd")
        self.gridLayout_14.addWidget(self.completed_lcd, 0, 2, 1, 1)
        self.queue_label = QtWidgets.QLabel(self.job_progress_page)
        self.queue_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.queue_label.setObjectName("queue_label")
        self.gridLayout_14.addWidget(self.queue_label, 1, 0, 1, 1)
        self.active_label = QtWidgets.QLabel(self.job_progress_page)
        self.active_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.active_label.setObjectName("active_label")
        self.gridLayout_14.addWidget(self.active_label, 1, 1, 1, 1)
        self.completed_label = QtWidgets.QLabel(self.job_progress_page)
        self.completed_label.setAlignment(QtCore.Qt.AlignHCenter|QtCore.Qt.AlignTop)
        self.completed_label.setObjectName("completed_label")
        self.gridLayout_14.addWidget(self.completed_label, 1, 2, 1, 1)
        self.status_stack.addWidget(self.job_progress_page)
        self.gridLayout_3.addWidget(self.status_stack, 0, 0, 1, 2)
        self.output_log_text_edit = QtWidgets.QTextEdit(self.preview_frame)
        self.output_log_text_edit.setObjectName("output_log_text_edit")
        self.gridLayout_3.addWidget(self.output_log_text_edit, 3, 0, 1, 2)
        self.gridLayout_9.addWidget(self.preview_frame, 0, 1, 1, 1)
        self.progress_bar = QtWidgets.QProgressBar(animation_workbench_base)
        self.progress_bar.setProperty("value", 24)
        self.progress_bar.setObjectName("progress_bar")
        self.gridLayout_9.addWidget(self.progress_bar, 1, 0, 1, 2)
        self.button_box = QtWidgets.QDialogButtonBox(animation_workbench_base)
        self.button_box.setOrientation(QtCore.Qt.Horizontal)
        self.button_box.setStandardButtons(QtWidgets.QDialogButtonBox.Close|QtWidgets.QDialogButtonBox.Help|QtWidgets.QDialogButtonBox.Ok)
        self.button_box.setObjectName("button_box")
        self.gridLayout_9.addWidget(self.button_box, 2, 0, 1, 2)
        self.point_layer_label.setBuddy(self.layer_combo)
        self.hover_frames_label.setBuddy(self.hover_frames_spin)
        self.point_frames_label.setBuddy(self.point_frames_spin)

        self.retranslateUi(animation_workbench_base)
        self.preview_stack.setCurrentIndex(1)
        self.status_stack.setCurrentIndex(1)
        self.button_box.accepted.connect(animation_workbench_base.accept) # type: ignore
        self.button_box.rejected.connect(animation_workbench_base.reject) # type: ignore
        self.enable_pan_easing.toggled['bool'].connect(self.pan_easing_combo.setEnabled) # type: ignore
        self.enable_zoom_easing.toggled['bool'].connect(self.zoom_easing_combo.setEnabled) # type: ignore
        self.enable_zoom_easing.toggled['bool'].connect(self.zoom_range_group.setEnabled) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(animation_workbench_base)
        animation_workbench_base.setTabOrder(self.layer_combo, self.scale_range)
        animation_workbench_base.setTabOrder(self.scale_range, self.radio_sphere)
        animation_workbench_base.setTabOrder(self.radio_sphere, self.radio_planar)
        animation_workbench_base.setTabOrder(self.radio_planar, self.enable_pan_easing)
        animation_workbench_base.setTabOrder(self.enable_pan_easing, self.pan_easing_combo)
        animation_workbench_base.setTabOrder(self.pan_easing_combo, self.enable_zoom_easing)
        animation_workbench_base.setTabOrder(self.enable_zoom_easing, self.zoom_easing_combo)
        animation_workbench_base.setTabOrder(self.zoom_easing_combo, self.point_frames_spin)
        animation_workbench_base.setTabOrder(self.point_frames_spin, self.hover_frames_spin)
        animation_workbench_base.setTabOrder(self.hover_frames_spin, self.reuse_cache)
        animation_workbench_base.setTabOrder(self.reuse_cache, self.radio_gif)
        animation_workbench_base.setTabOrder(self.radio_gif, self.rad_movie)
        animation_workbench_base.setTabOrder(self.rad_movie, self.folder_edit)
        animation_workbench_base.setTabOrder(self.folder_edit, self.folder_button)
        animation_workbench_base.setTabOrder(self.folder_button, self.output_log_text_edit)

    def retranslateUi(self, animation_workbench_base):
        _translate = QtCore.QCoreApplication.translate
        animation_workbench_base.setWindowTitle(_translate("animation_workbench_base", "Dialog"))
        self.render_mode_group.setToolTip(_translate("animation_workbench_base", "The render mode determines the behaviour and type of the animation. \n"
"For \'Sphere\' the coordinate reference system (CRS) will \n"
"be manipulated to create a spinning globe effect. \n"
"For \'Plane\', the CRS will not be altered, but will pan and \n"
"zoom to each point."))
        self.render_mode_group.setTitle(_translate("animation_workbench_base", "Render Mode"))
        self.radio_planar.setText(_translate("animation_workbench_base", "Planar"))
        self.radio_sphere.setText(_translate("animation_workbench_base", "Sphere"))
        self.output_destination_group.setTitle(_translate("animation_workbench_base", "Output Destination"))
        self.folder_label.setText(_translate("animation_workbench_base", "Folder"))
        self.folder_edit.setToolTip(_translate("animation_workbench_base", "The output folder will be populated with \n"
"all of the frames of the animation, and \n"
"the GIF or MP4 as selected above."))
        self.folder_button.setText(_translate("animation_workbench_base", "..."))
        self.animation_reference_group.setTitle(_translate("animation_workbench_base", "Animation Reference"))
        self.point_layer_label.setText(_translate("animation_workbench_base", "Point layer"))
        self.output_options_group.setToolTip(_translate("animation_workbench_base", "Select which output format you would like. \n"
"Regardless of which you choose, a folder \n"
"of images will be created, one image per frame. \n"
"For the GIF export to work, you will \n"
"need to have the ImageMagick \'convert\'  application \n"
"available on your system. For the MP4 option to work, \n"
"you need to have the \'ffmpeg\' application on \n"
"your system."))
        self.output_options_group.setTitle(_translate("animation_workbench_base", "Output Options"))
        self.reuse_cache.setToolTip(_translate("animation_workbench_base", "Will not erase cached images on disk \n"
"and will resume processing from last cached image."))
        self.reuse_cache.setText(_translate("animation_workbench_base", "Re-use cached images where possible"))
        self.radio_gif.setText(_translate("animation_workbench_base", "Animated GIF"))
        self.rad_movie.setText(_translate("animation_workbench_base", "Movie (MP4)"))
        self.animation_frames_group.setTitle(_translate("animation_workbench_base", "Animation Frames"))
        self.hover_frames_label.setText(_translate("animation_workbench_base", "Hover frames at each point"))
        self.hover_frames_spin.setToolTip(_translate("animation_workbench_base", "This is the number of frames that will \n"
"be used during animation of the motion from \n"
"one point to the next. Video generation \n"
"is done at 30 frames per second, so a value \n"
"of 30 here would result in a 1 second flight time \n"
"between two consecutive points. \n"
"Set to zero to disable."))
        self.point_frames_label.setText(_translate("animation_workbench_base", "Frames between points"))
        self.point_frames_spin.setToolTip(_translate("animation_workbench_base", "This is the number of frames that will be used during\n"
" animation of the dwell period at each point. \n"
"Video generation is done at 30 frames per \n"
"second, so a value of 30 here would result in a 1 second \n"
"dwell time. \n"
"Set to zero to disable."))
        self.easings_group.setTitle(_translate("animation_workbench_base", "Easings"))
        self.zoom_easing_combo.setToolTip(_translate("animation_workbench_base", "The zoom easing will affect the behaviour \n"
"of the camera during zoom transitions."))
        self.pan_easing_combo.setToolTip(_translate("animation_workbench_base", "The pan easing will determine the motion \n"
"characteristics of the camera on the Y axis \n"
"as it flies across the scene."))
        self.enable_zoom_easing.setText(_translate("animation_workbench_base", "Enable Zoom Easing"))
        self.enable_pan_easing.setText(_translate("animation_workbench_base", "Enable Pan Easing"))
        self.zoom_range_group.setToolTip(_translate("animation_workbench_base", "The scale range that the animation should \n"
"move through. The smallest scale will be \n"
"the zenith of the animation when it zooms \n"
"out while travelling between points, and the \n"
"largest scale will be the scale used when \n"
"we arrive at each point."))
        self.zoom_range_group.setTitle(_translate("animation_workbench_base", "Zoom Range"))
        self.output_log_label.setText(_translate("animation_workbench_base", "Output Logs"))
        self.current_frame_preview_label.setText(_translate("animation_workbench_base", "Current Frame Preview"))
        self.video_preview_label.setText(_translate("animation_workbench_base", "Video Preview"))
        self.play_button.setText(_translate("animation_workbench_base", ">"))
        self.pan_easing_preview_label.setText(_translate("animation_workbench_base", "Pan Easing Preview"))
        self.zoom_easing_preview_label.setText(_translate("animation_workbench_base", "Zoom Easing Preview"))
        self.queue_label.setText(_translate("animation_workbench_base", "Queued Tasks"))
        self.active_label.setText(_translate("animation_workbench_base", "Active Tasks"))
        self.completed_label.setText(_translate("animation_workbench_base", "Completed  Tasks"))
        self.output_log_text_edit.setHtml(_translate("animation_workbench_base", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
from qgis import gui
