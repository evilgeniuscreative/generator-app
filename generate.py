import openai
import os
import re
from dotenv import load_dotenv

load_dotenv()
client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

OUTPUT_DIR = "static/images"
os.makedirs(OUTPUT_DIR, exist_ok=True)

def slugify(text):
    return re.sub(r'[\W_]+', '_', text).strip('_').lower()

def generate_images(prompts):
    for prompt in prompts:
        try:
            print(f"Generating: {prompt}")
            response = client.images.generate(
                model="dall-e-3",
                prompt=prompt,
                size="1024x1024",
                quality="standard",
                n=1,
            )
            image_url = response.data[0].url
            filename = slugify(prompt[:40]) + ".png"
            path = os.path.join(OUTPUT_DIR, filename)

            # Save image locally
            import requests
            r = requests.get(image_url)
            with open(path, "wb") as f:
                f.write(r.content)
        except Exception as e:
            print(f"Error generating for prompt: {prompt}\n{e}")
