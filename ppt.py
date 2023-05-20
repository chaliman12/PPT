import aspose.slides as slides

# load presentation
with slides.Presentation("Chapter 6 Staffing function.pptx") as presentation:
    # select slide
    slide = presentation.slides[0]

    # load video file
    with open("DURAANUU GELANA GAROMSA New Oromo music 2023 Galaanaa Gaaromsaa (1).mp4", "rb") as in_file:
        # add video to presentation
        vid = presentation.videos.add_video(in_file)

        # add video frame
        vf = slide.shapes.add_video_frame(50, 150, 300, 350, vid)

        # set video to video frame
        vf.embedded_video = vid

        # set play mode and volume of the video
        vf.play_mode = slides.VideoPlayModePreset.AUTO
        vf.volume = slides.AudioVolumeMode.LOUD

    # save presentation
    presentation.save("add-video-frame.pptx", slides.export.SaveFormat.PPTX)