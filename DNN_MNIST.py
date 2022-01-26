import torch
import torchvision
import torchvision.transforms as transformers

#ETL

train_set = torchvision.datasets.FashionMNIST(
    root= './data/FashionMNIST',            # Extract
    train = True,
    download= True,
    transform=transformers.Compose([transformers.ToTensor])   # transforms
)

train_loader = torch.utils.data.DataLoader(train_set, batch_size = 10)   # Load 
