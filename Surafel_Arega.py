# Selection Sort
arr = [27,54,88,30,19]
n = len(arr)

for i in range(n):
  min_idx = i
  j = i + 1
  
  while j < n:
    if arr[j] < arr[min_idx]:
      min_idx = j
    j += 1

  arr[i], arr[min_idx] = arr[min_idx], arr[i] 
print(f"Selection Sort: {arr}")

# Insertion sort hey 
arr = [40,12,34,56,90,25,73]
n = len(arr)
for i in range(1, n):
  key = arr[i]

  for j in range(i - 1, -1, -1):
    if arr[j] > key:
      arr[j + 1] = arr[j]
      i = j

  arr[i] = key
print(f"Insertion Sort: {arr}")