import numpy as np
from numpy.core.records import array

# arr = np.array([1,5,2,9,10], dtype=np.int8)
# print(arr)

# print()
# nd_arr = np.array([
#                [12, 45, 78],
#                [34, 56, 13],
#                [12, 98, 76]
#                ])
# print(nd_arr)
# print(nd_arr.dtype)

# print()
# arr, step = np.linspace(-6, 21, 60, endpoint=False,  retstep=True)
# print(round(step, 2))

# arr = np.linspace(1,2,6)
# print(arr)
# print()

# nd_array = np.linspace(0, 6, 12, endpoint=False).reshape(3,4)
# print(nd_array)
# print(nd_array[1,2])
# print(nd_array[:2])

# data = np.array([4, 9, -4, 3])
# roots = np.sqrt(data)
# roots[np.isnan(roots)] = 0
# print(roots)
# print(sum(roots))

# shape = (2, 3)
# a = np.random.sample(shape) 
# print(a)
# print()
# # b = np.random.randint(-30, 50, size=(3,4))
# # print(b)

# np.random.seed(100)
# print(np.random.randint(10, size=3))
# print(np.random.randint(10, size=3))
# print(np.random.randint(10, size=3))

# even = [i for i in range(2, 17) if i % 2 == 0]
# print(even)



# def get_chess(a):
#     nd_zeros = np.zeros((a, a), dtype=np.float32)
#     nd_zeros[1::2, ::2] = 1
#     nd_zeros[::2, 1::2] = 1
    
#     return nd_zeros
    
# print(get_chess(5))

# b = np.uint32(124)
# print(np.iinfo(b))
# print()


# playlist = [1, 55, 2, 47, 54, 89, 304, 27, 65, 66, 98, 80, 100, 105, 4, 76]
# a = np.random.randint(2**32, dtype=np.uint32)
# print(a)
# np.random.seed(a)
# new_arr = np.random.permutation(playlist)
# print(new_arr)



print(np.random.choice(np.arange(1,101), size=5*5, replace=False))


simplelist = [19, 242, 14, 152, 142, 1000]

avg = sum(simplelist) / len(simplelist)
print(avg)