# Source - Convert - divide - ensub - merge - AI(GPT) - save - send(e-mail)- delete

#---#
from modules.convert import converter
from modules.divider import process_audio_and_summarize
from modules.ensubtitle import save_srt
from modules.merger import merge_srt_files
from modules.filemanage import delete_saved, delete_source #, transfer
from modules.ai_processing import processor, sum_save

import os, whisper, time, dotenv
#---#

dotenv.load_dotenv()
token = os.environ.get('TEST_API_TOKEN_GPT')

#---#

model = whisper.load_model("small")

video_path = 'source/source_vid.mp4'
audio_path = 'save/saved_aud.wav'
chunks_path = 'save/chunks'
srt_path = 'save/srt'

converter(video_path, audio_path) # Video(mp4) to Audio(wav)
process_audio_and_summarize(audio_path, chunks_path)

num_chunks = len(os.listdir(chunks_path)) # chunks 개수 int
for i in range(num_chunks) :
    chunks = model.transcribe(f"{chunks_path}/chunk_{i}.wav")
    save_srt(chunks, f"{srt_path}/subtitles_{i}.srt")
    print(f"자막이 {i}번째 SRT 파일로 저장되었습니다.")

file_names = [f"save/srt/subtitles_{j}.srt" for j in range(num_chunks)]
merge_srt_files(file_names, "save/srt/merged_subtitles.txt")

#num_srt는 num_chunks + 1 (int)

## AI processing & save summarized

# processor(token, "save/srt/merged_subtitles.txt")

exit()
## delete or transfer

key = int(input('0 : remove all files, 1 : remove saved files'))
if key == 0 :
    delete_saved(srt_path, chunks_path, audio_path, num_chunks)
    delete_source(video_path)
elif key == 1 :
    delete_saved(srt_path, chunks_path, audio_path, num_chunks)
