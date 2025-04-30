import os


def delete_saved(srt_path, chunk_path, saved_aud_path, count) : 
    for i in range(count) :
        os.remove(f'{srt_path}/subtitles_{i}.srt')
    os.remove(f'{srt_path}/merged_subtitles.txt')
    for j in range(count) :
        os.remove(f'{chunk_path}/chunk_{j}.wav')
    os.remove(saved_aud_path)
    print("saved files are removed.")

def delete_source(source_vid_path) :
    os.remove(source_vid_path)
    print("source vidio is removed.")

# def transfer(srt_path, chunk_path, saved_aud_path, source_vid_path, count) :
#     os.replace(srt_path, 'archive')
#     print("srt is replaced to archive.") ## dir 하위 파일 del 구현x

#     os.replace(chunk_path, 'archive')
#     print("chunks are replaced to archive.") ## dir 하위 파일 del 구현x

#     os.replace(saved_aud_path, 'archive')
#     print("saved audio is replaced to archive.")

#     os.replace(source_vid_path, 'archive')
#     print("source video is replaced to archive.")

if __name__ == "__main__" :
    print("done")