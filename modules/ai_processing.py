from openai import OpenAI
import os

def processor(key, path) :
    client = OpenAI(api_key = key)

    file = client.files.create(file = open(path, "rb"), purpose = "user_data") # purpose는 아마 user_data가 맞는듯? 몰루

    response = client.responses.create(
    model="gpt-3.5-turbo",    
    input=[
        {
            "role": "An expert that read subscription file and process it.",
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
    return response.output_text

def sum_save(response_text) :
    with open('summarized', 'w') as f :
        f.write(response_text)

