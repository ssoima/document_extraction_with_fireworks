import json
from typing import Type

import openai
from pydantic import BaseModel, ValidationError

from utils import FIREWORKS_API_KEY


def process_image(prompt: str, image_base64: str, model: str, response_model: Type[BaseModel], retry = 0):
    client = openai.OpenAI(
        base_url="https://api.fireworks.ai/inference/v1",
        api_key=FIREWORKS_API_KEY,
    )

    # There is a type mismatch in ResponseFormatJSONSchema. It expects json_schema
    response = client.chat.completions.create(
        model=model,
        response_format={"type": "json_object", "schema": response_model.model_json_schema()},
        temperature=0.0,
        messages=[{
            "role": "user",
            "content": [{
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{image_base64}"
                },
            }, {
                "type": "text",
                "text": prompt,
            }, ],
        }],
    )

    response_content = response.choices[0].message.content
    print(response_content)

    try:
        response_dict = json.loads(response_content)

        license_data = response_model.parse_obj(response_dict) # Validate output against the schema
        return license_data
        print("Valid Data:", license_data.model_dump_json())
    except ValidationError as e:
        if retry:
            print("Validation Error:", e.json())
            print("Retrying request...")
            return process_image(prompt, image_base64, model, response_model, retry - 1)
        print("Validation Error:", e.json())
