# =============================================================================
# PYTHON + STATISTICS PRACTICE SET (40 QUESTIONS)
# =============================================================================


# =============================================================================
# SECTION A (Q1–Q20)
# =============================================================================

# Q1. Compute mean, median, standard deviation
import statistics as st
data = [12, 15, 20, 22, 25]
print(st.mean(data))
print(st.median(data))
print(st.stdev(data))

# Q2. Compute variance
import statistics as st
data = [5, 10, 15, 20]
print(st.variance(data))

# Q3. Generate Normal data and find mean
import random as r
import statistics as st
r.seed(1)
data = [r.normalvariate(0, 1) for _ in range(10)]
print(st.mean(data))

# Q4. Gamma distribution + sum of squares
import random as r
data = [r.gammavariate(2, 0.2) for _ in range(10)]
sos = sum(x * x for x in data)
print(sos)

# Q5. Mean using function
def mean(x):
    return sum(x) / len(x)
print(mean([2, 4, 6, 8]))

# Q6. Print values greater than mean
import statistics as st
data = [10, 12, 15, 30, 18]
m = st.mean(data)
for x in data:
    if x > m:
        print(x)

# Q7. Frequency count
data = [1, 2, 2, 3, 3, 3]
freq = {}
for x in data:
    freq[x] = freq.get(x, 0) + 1
print(freq)

# Q8. NumPy mean
import numpy as np
arr = np.array([10, 20, 30, 40])
print(np.mean(arr))

# Q9. NumPy standard deviation
import numpy as np
arr = np.array([5, 10, 15, 20])
print(np.std(arr))

# Q10. Reshape array
import numpy as np
arr = np.array([1, 2, 3, 4, 5, 6])
print(np.reshape(arr, (2, 3)))

# Q11. Maximum & minimum
data = [5, 8, 2, 10, 3]
print(max(data), min(data))

# Q12. Range
data = [5, 8, 2, 10, 3]
print(max(data) - min(data))

# Q13. Even-odd classification
data = [2, 5, 8, 11]
for x in data:
    if x % 2 == 0:
        print("Even", x)
    else:
        print("Odd", x)

# Q14. Zero matrix
import numpy as np
print(np.zeros((3, 3)))

# Q15. Pairwise comparison
x = [1, 2, 3]
y = [2, 4, 6]
for i in range(len(x)):
    print(x[i], y[i])

# Q16. Sort data
data = [12, 5, 8, 20]
data.sort()
print(data)

# Q17. NumPy median
import numpy as np
arr = np.array([10, 5, 8, 20])
print(np.median(arr))

# Q18. Random choice
import random as r
print(r.choice([10, 20, 30, 40]))

# Q19. Factorial
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)
print(factorial(5))

# Q20. Coin toss simulation
import random as r
heads = 0
for _ in range(10):
    if r.choice(['H', 'T']) == 'H':
        heads += 1
print(heads)


# =============================================================================
# SECTION B (Q21–Q40)
# =============================================================================

# Q21. Mean (manual) + variance
import statistics as st
data = [2, 4, 6, 8, 10]
mean = sum(data) / len(data)
print(mean)
print(st.variance(data))

# Q22. Count positive normal values
import random as r
count = 0
for _ in range(20):
    if r.normalvariate(0, 1) > 0:
        count += 1
print(count)

# Q23. Median without module
data = [5, 2, 9, 1, 7]
data.sort()
n = len(data)
if n % 2 == 1:
    print(data[n // 2])
else:
    print((data[n // 2] + data[n // 2 - 1]) / 2)

# Q24. Range and midrange
data = [3, 7, 10, 15]
r = max(data) - min(data)
mid = (max(data) + min(data)) / 2
print(r, mid)

# Q25. Check symmetry
import statistics as st
data = [1, 2, 3, 4, 5]
if st.mean(data) == st.median(data):
    print("Symmetric")

# Q26. Count above median
import statistics as st
data = [10, 20, 30, 40, 50]
med = st.median(data)
count = sum(1 for x in data if x > med)
print(count)

# Q27. Random 3x3 matrix
import numpy as np
import random as r
arr = np.array([[r.randint(1, 10) for _ in range(3)] for _ in range(3)])
print(arr)

# Q28. Row sum
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.sum(axis=1))

# Q29. Column mean
import numpy as np
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(np.mean(arr, axis=0))

# Q30. Index of max
data = [5, 12, 7, 20, 9]
print(data.index(max(data)))

# Q31. Dice simulation
import random as r
freq = {}
for _ in range(20):
    x = r.randint(1, 6)
    freq[x] = freq.get(x, 0) + 1
print(freq)

# Q32. Cumulative sum
data = [1, 2, 3, 4]
s = 0
cumsum = []
for x in data:
    s += x
    cumsum.append(s)
print(cumsum)

# Q33. Z-score standardization
import statistics as st
data = [10, 20, 30]
mean = st.mean(data)
sd = st.stdev(data)
z = [(x - mean) / sd for x in data]
print(z)

# Q34. Check increasing data
data = [2, 4, 6, 8]
flag = True
for i in range(len(data) - 1):
    if data[i] > data[i + 1]:
        flag = False
print(flag)

# Q35. Remove outliers
import statistics as st
data = [10, 12, 15, 100]
m = st.mean(data)
clean = [x for x in data if x <= 2 * m]
print(clean)

# Q36. Uniform random values
import random as r
data = [r.random() for _ in range(5)]
print(data)

# Q37. Square list using function
def square_list(lst):
    return [x * x for x in lst]
print(square_list([1, 2, 3, 4]))

# Q38. Dot product
a = [1, 2, 3]
b = [4, 5, 6]
dot = sum(a[i] * b[i] for i in range(len(a)))
print(dot)

# Q39. Convert to NumPy and reshape
import numpy as np
arr = np.array([1, 2, 3, 4])
print(arr.reshape(2, 2))

# Q40. Probability of heads
import random as r
heads = 0
n = 100
for _ in range(n):
    if r.choice(['H', 'T']) == 'H':
        heads += 1
print(heads / n)
