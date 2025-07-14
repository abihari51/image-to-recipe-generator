
# 🥘 Image to Recipe Generator

This project uses BLIP and GPT-2 to generate a recipe from an uploaded food image using a Gradio UI.

## 🔧 How it works
1. BLIP generates a caption for the uploaded image.
2. GPT-2 generates a recipe based on the caption.
3. Gradio provides the interface for interaction.

## 🚀 Run Locally
```bash
git clone https://github.com/yourusername/image-to-recipe-generator.git
cd image-to-recipe-generator
pip install -r requirements.txt
python app.py
