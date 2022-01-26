import torch 
import numpy as np

print(torch.__version__)
print(torch.cuda.is_available())
print(torch.version.cuda)

#tensor
data = [[1,2], [2,1]]
x_data = torch.tensor(data)
print(x_data)


#from numpy array
np_array = np.array(data)
x_np = torch.from_numpy(np_array)
print(x_np)


dd = [
    [1,2,3],
    [4,5,6],
    [7,8,9] 
    ]

print(dd[0])
print(dd[1])
print(dd[2])


     


