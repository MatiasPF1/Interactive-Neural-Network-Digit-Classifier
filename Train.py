import torch
import torch.nn as nn
import torch.optim as optim
import torch.utils.data
import torchvision
import torchvision.transforms as transforms

from model import DigitRecognizer #Model



# --------------------------
# Data transformations + Loading the Train/Test.
# --------------------------
transform = transforms.Compose([
    transforms.ToTensor(),
    transforms.Normalize((0.5,), (0.5,))
])


train_set = torchvision.datasets.MNIST(
    root='./data',        #Use relative path to current directory
    train=True,           # Load the training set
    download=True,        # Download if it doesn't exist
    transform=transform   # Apply the transformation 
)


train_loader = torch.utils.data.DataLoader(
    train_set,
    batch_size=64,          #Standar procces of 64 images 
    shuffle=True            #Avoiding model to learn order
)


test_set = torchvision.datasets.MNIST(
    root='./data',
    train=False,            # Load the test set (10,000 images)
    download=True,
    transform=transform
)

test_loader = torch.utils.data.DataLoader(
    test_set,
    batch_size=64,
    shuffle=False  # No need to shuffle test data
)





# --------------------------
# Setup Device(CPU-Training-Based) Model, Loss Function and Adam Optimizer
# --------------------------
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
print(f"Using device: {device}")

model = DigitRecognizer().to(device) 
criterion = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)




# --------------------------
# Training loop
# --------------------------
num_epochs = 5
model.train()
for epoch in range(num_epochs):
    running_loss = 0.0
    for i, (images, labels) in enumerate(train_loader):
        images, labels = images.to(device), labels.to(device)

        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()
        if (i + 1) % 200 == 0:
            print(f"Epoch [{epoch+1}/{num_epochs}], Step [{i+1}/{len(train_loader)}], "
                  f"Loss: {running_loss/200:.4f}")
            running_loss = 0.0
print("Finished Training")




# --------------------------
# Save the trained model
# --------------------------
torch.save(model.state_dict(), "model.pth")
print("Model saved as model.pth")




# --------------------------
# Evaluate
# --------------------------
model.eval()
with torch.no_grad():
    correct, total = 0, 0
    for images, labels in test_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        _, predicted = torch.max(outputs.data, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()


    print(f"Accuracy on 10,000 test images: {100 * correct / total:.2f}%")
