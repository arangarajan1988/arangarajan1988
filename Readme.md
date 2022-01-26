markdown file
torch - whole library 
torch.nn - NN library 
torch.autocad 
torch.functional
torch.optim
torch.utils
torch.vision 

torch uses dynamically compute graphs 

 nd array 
 nd tensor

scalar - 0 dimenetional tensor
vector - 1d dimentional tensor
matrix - 2dimentional tensor
nd array - nd dimetional tensor



rank , axes , shape 

Rank of tensor  - Number of dimentions present in the tensor 
Rank of tensor - 2 is for matrix - its helps to define indexes required to access 

Axes  - 
Length of the first axes = 3

t[0]
t[1]
t[2]


Length of the second axes = 4 

t[0][0]
t[1][0]
t[2][0]

t[0][1]
t[1][1]
t[2][1]

t[0][2]
t[1][2]
t[2][2]

t[0][3]
t[1][3]
t[2][3]

Tensor for images 

[B, c , H ,W]
B - Batch size 
C - Color chennals 
H - Height of the image
W - Width of the Images 

Note :

Tensors contain same type of uniform datatype(dtype)
Tensors computations between tensors depends on dtype and device 


array1 = np.array([[1,2],[2,3]])
print(torch.Tensor(array1).dtype) -> Constructor 
print(torch.tensor(array1).dtype) -> Factory pattern 
print(torch.as_tensor(array1).dtype) -> Factory pattern 
print(torch.from_numpy(array1).dtype) -> Factory pattern 

Modification after converting from numpy 

No changes  after the modfification ( copy mememory)
print(torch.Tensor(array1).dtype) -> Constructor 
print(torch.tensor(array1).dtype) -> Factory pattern 

Changes made after the modification ( shared memeory)
print(torch.as_tensor(array1).dtype) -> Factory pattern 
print(torch.from_numpy(array1).dtype) -> Factory pattern 

Primary operation 
1. reshape operation 
2. Element wise operation  
3. Reduction operation 
4. Access operation 


1. reshape operation :
 
