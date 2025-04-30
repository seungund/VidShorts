import whisper
import time

# model = whisper.load_model("small")

# 자막을 SRT 형식으로 저장하는 함수 (반복문 외부로 이동)
def save_srt(result, filename):
    with open(filename, "w", encoding="utf-8") as f:  # UTF-8 인코딩 지정
        for idx, segment in enumerate(result["segments"]):
            start = time.strftime("%H:%M:%S", time.gmtime(segment["start"]))
            end = time.strftime("%H:%M:%S", time.gmtime(segment["end"]))
            text = segment["text"]
            f.write(f"{idx+1}\n")
            f.write(f"{start} --> {end}\n")
            f.write(f"{text}\n\n")
