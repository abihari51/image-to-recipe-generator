from transformers import BlipProcessor, BlipForConditionalGeneration, GPT2Tokenizer, GPT2LMHeadModel
from PIL import Image
import gradio as gr
import torch

# Load BLIP model
caption_processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-large")
caption_model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-large")

# Load GPT-2 model
recipe_tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
recipe_model = GPT2LMHeadModel.from_pretrained("gpt2")

def image_to_recipe(image):
    image = image.convert("RGB")
    inputs = caption_processor(images=image, return_tensors="pt")
    caption_ids = caption_model.generate(**inputs, max_length=50)
    caption = caption_processor.decode(caption_ids[0], skip_special_tokens=True)

    prompt = f"Write a detailed recipe for {caption}."
    inputs = recipe_tokenizer(prompt, return_tensors="pt")
    output = recipe_model.generate(
        **inputs,
        max_length=250,
        do_sample=True,
        temperature=0.7,
        top_p=0.9,
    )
    recipe = recipe_tokenizer.decode(output[0], skip_special_tokens=True)
    return f"**Caption**: {caption}\n\n**Recipe**:\n{recipe}"

gr.Interface(
    fn=image_to_recipe,
    inputs=gr.Image(type="pil", label="Upload a food image"),
    outputs=gr.Markdown(),
    title="Image to Recipe Generator",
    description="Upload a food image and get a recipe generated for it!"
).launch()
