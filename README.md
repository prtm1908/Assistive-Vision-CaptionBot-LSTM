# AI-Image-Captioning-Using-LSTM

This repository contains an implementation of an AI image captioning system using Long Short-Term Memory (LSTM) networks. Image captioning is the task of generating textual descriptions for images, allowing computers to understand and describe the contents of images.

## Features

- **LSTM Model:** The core of this project is an LSTM-based neural network that learns to generate captions for input images.
- **Pretrained Models:** Provided pretrained models that you can use to quickly generate captions for your own images.
- **Deployment:** This repository includes scripts and instructions to deploy the trained model for generating captions.

## How It Works

1. **Data Preprocessing:** The images and their corresponding captions are preprocessed and transformed into a suitable format for training.
2. **Model Training:** The LSTM model is trained on the preprocessed data to learn the relationship between images and their associated captions.
3. **Caption Generation:** Given a new image, the trained model generates a relevant caption by predicting one word at a time based on the previous words generated.
4. **Deployment:** The deployment script allows you to use the trained model to generate captions for your own images.

## Usage

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/ai-image-captioning.git
   cd ai-image-captioning
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Download the pretrained model weights from the release page or train your own model.

4. Run the captioning script on your image:
   ```bash
   https://ai-image-captioning-using-lstm.streamlit.app/
   ```

   This will generate a caption for your image using the pretrained model.
