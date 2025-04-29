import os
from moviepy.editor import AudioFileClip


def process_audio_and_summarize(audio_path, save_dir):
    # 저장할 디렉토리가 없으면 생성
    os.makedirs(save_dir, exist_ok=True)

    print(f"[+] Extracting audio from {audio_path}...")
    audio = AudioFileClip(audio_path)
    audio_chunks = []
    chunk_length = 600  # 10분씩 분할

    for i in range(0, int(audio.duration), chunk_length):
        chunk = audio.subclip(i, min(i + chunk_length, audio.duration))
        chunk_filename = os.path.join(save_dir, f"chunk_{i // chunk_length}.wav")
        chunk.write_audiofile(chunk_filename)
        audio_chunks.append(chunk_filename)
        print(f"MoviePy - Writing audio in {chunk_filename}")