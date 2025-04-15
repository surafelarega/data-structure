# Insertion Sort
arr = [49,52,71,15,21]
n = len(arr)
for i in range(1, n):
  key = arr[i]
  for j in range(i, -1, -1):
    if arr[j -1] > key:
      arr[j] = arr[j-1]
    else:
      break

  arr[j] = key
print(arr) 

# Insertion Sort 
arr = [6,8,9,7,11,19,21,26]
for i in range(1, len(arr)):
  key = arr[i]

  for j in range(i - 1, -1, -1):
    if arr[j] > key:
      arr[j + 1] = arr[j]
      i = j

  arr[i] = key
print(arr)

# Selection Sort using for for loop
arr = [5,1,0,7,9,2,3]

for i in range(len(arr)):
  minimum_index = i

  for j in range(i + 1, len(arr)):
    if arr[j] < arr[minimum_index]:
      minimum_index = j
  arr[i], arr[minimum_index] = arr[minimum_index], arr[i] 
print(arr)

# Selection Sort using for while loop
arr = [2,5,8,3,1]
n = len(arr)
for i in range(n):
  min_idx = i
  j = i + 1
  while j < n:
    if arr[j] < arr[min_idx]:
      min_idx = j
    j += 1

  arr[i], arr[min_idx] = arr[min_idx], arr[i] 
print(arr)

arr = [2,5,8,3,1]
n = len(arr)
for i in range(n):        
  min_idx = n -1
  for j in range(i,-1,-1):
    if arr[j] < arr[min_idx]:
      min_idx = j

  arr[i], arr[min_idx] = arr[min_idx], arr[i] 
print(arr)

