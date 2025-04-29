from moviepy.editor import VideoFileClip

def converter (vid_path, aud_path) :
    video = VideoFileClip(vid_path)
    video.audio.write_audiofile(aud_path)
    return 0
#완