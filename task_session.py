import numpy as np

#1
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(arr)

#******************************************************
#2
arr = np.array([[0, 1], [2, 3], [4, 5], [6, 7], [8, 9], [10, 11], [12, 13], [14, 15], [16, 17], [18, 19]])
print(arr)

#******************************************************
#3
python_list = [1, 2, 3, 4, 5]
numpy_array = np.array(python_list)

print(f"Original Python list: {python_list}")
print(f"NumPy array: {numpy_array}")
print(f"Type: {type(numpy_array)}")
#******************************************************
#4
scalar_array = np.array(42)                    
vector_array = np.array([1, 2, 3, 4, 5])       
matrix_array = np.array([[1, 2, 3], [4, 5, 6]])  
tensor_array = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])  

def print_array_properties(arr, name):
    """Print dimensions, shape and data type of a NumPy array"""
    print(f"=== {name} ===")
    print(f"Array contents:\n{arr}")
    print(f"Number of dimensions (ndim): {arr.ndim}")
    print(f"Shape: {arr.shape}")
    print(f"Data type (dtype): {arr.dtype}")
    print("-" * 50)

print_array_properties(scalar_array, "Scalar (0D Array)")
print_array_properties(vector_array, "Vector (1D Array)")
print_array_properties(matrix_array, "Matrix (2D Array)")
print_array_properties(tensor_array, "Tensor (3D Array)")

#******************************************************
#5
