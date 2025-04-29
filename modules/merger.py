def merge_srt_files(file_names, output_file):
    # 출력 파일을 UTF-8 인코딩으로 열기
    with open(output_file, "w", encoding="utf-8") as outfile:
        subtitle_index = 1  # 자막 번호는 1부터 시작

        for file_name in file_names:
            with open(file_name, "r", encoding="utf-8") as infile:
                # 파일의 내용 읽기
                lines = infile.readlines()

                # 자막 번호 수정
                for line in lines:
                    # 자막 번호가 포함된 라인만 수정
                    if line.strip().isdigit():
                        outfile.write(f"{subtitle_index}\n")
                        subtitle_index += 1
                    else:
                        outfile.write(line)

    print(f"모든 자막이 {output_file}로 합쳐졌습니다.")

