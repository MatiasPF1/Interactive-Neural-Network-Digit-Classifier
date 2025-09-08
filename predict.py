import torch
from model import DigitRecognizer  

# Global variable to store the loaded model
model = None
def predict_digit(grid, model_path='model.pth'):
    global model
    # Load model First Time
    if model is None:
        print("Loading model for the first time...")
        model = DigitRecognizer()
        model.load_state_dict(torch.load(model_path, map_location='cpu'))
        model.eval()
    # Preprocess the input grid
    img = torch.tensor(grid, dtype=torch.float32).unsqueeze(0).unsqueeze(0)
    img = (img / 255.0 - 0.5) / 0.5  # Normalize to [-1, 1] range

    # Make prediction
    with torch.no_grad():
        output = model(img)  # Raw logits from model
        probabilities = torch.softmax(output, dim=1)  # Convert to probabilities
        predicted_class = torch.argmax(output, dim=1).item()  # Get predicted digit
        confidence = probabilities[0][predicted_class].item()  # Get confidence score
        
        return predicted_class, confidence
