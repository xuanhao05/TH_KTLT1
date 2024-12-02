print("sv:Nguyen Xuan Hao")
print("mssv:235752021610096")
import numpy as np

student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40.0, 42.0, 45.0, 41.0, 38.0, 40.0, 42.0])

sorted_indices = np.lexsort((student_height, student_id))

sorted_student_id = student_id[sorted_indices]
sorted_student_height = student_height[sorted_indices]

# In kết quả
print("Chỉ số sắp xếp:", sorted_indices)
print("ID sinh viên được sắp xếp:", sorted_student_id)
print("Chiều cao sinh viên được sắp xếp:", sorted_student_height
