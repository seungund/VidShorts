from openai import OpenAI
import os

def processor(key, path) :
    client = OpenAI(api_key = key)

    file = client.files.create(file = open(path, "rb"), purpose = "user_data") # purpose는 아마 user_data가 맞는듯? 몰루

    response = client.responses.create(
    model="gpt-4.1",    
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_file",
                    "file_id": file.id,
                },
                {
                    "type": "input_text",
                    "text": "Please summarize text file in Korean.",
                    },
                ]
            }
        ]
    )

    print(response.output_text)

def sum_save() :
    return 0;

