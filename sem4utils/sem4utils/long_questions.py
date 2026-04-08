# =============================================================================
# PYTHON + STATISTICS — 10 LONG ANSWER QUESTIONS (5-6 MARKS EACH)
# =============================================================================


# =============================================================================
# Q1. [Modules — math & random]
# Generate 10 random floats, compute sqrt, floor, ceiling — print formatted table
# =============================================================================

import random, math

numbers = [random.uniform(1, 100) for _ in range(10)]
print(f"{'Original':>12} | {'Sqrt':>8} | {'Floor':>6} | {'Ceiling':>8}")
print("-" * 46)
for n in numbers:
    print(f"{n:>12.4f} | {math.sqrt(n):>8.4f} | {math.floor(n):>6} | {math.ceil(n):>8}")


# =============================================================================
# Q2. [Modules — statistics]
# Mean, median, mode, variance, std, Q1/Q2/Q3, IQR, outlier check for 91
# =============================================================================

import statistics

marks = [55, 72, 68, 45, 90, 88, 76, 60, 55, 82, 91, 63]
mean   = statistics.mean(marks)
median = statistics.median(marks)
mode   = statistics.mode(marks)
var    = statistics.variance(marks)
std    = statistics.stdev(marks)
q      = statistics.quantiles(marks, n=4)
Q1, Q2, Q3 = q[0], q[1], q[2]
IQR = Q3 - Q1

print(f"Mean     : {mean}")
print(f"Median   : {median}")
print(f"Mode     : {mode}")
print(f"Variance : {var:.4f}")
print(f"Std Dev  : {std:.4f}")
print(f"Q1={Q1}, Q2={Q2}, Q3={Q3}, IQR={IQR}")

lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR
print(f"Outlier bounds: [{lower}, {upper}]")
print(f"Is 91 an outlier? {91 < lower or 91 > upper}")


# =============================================================================
# Q3. [Modules — random + statistics + lists]
# Roll two dice 500 times, compute stats, print frequency table of sums
# =============================================================================

import random, statistics

sums = [random.randint(1, 6) + random.randint(1, 6) for _ in range(500)]
print(f"Mean   : {statistics.mean(sums):.4f}")
print(f"Median : {statistics.median(sums)}")
print(f"Mode   : {statistics.mode(sums)}")
print(f"Std Dev: {statistics.stdev(sums):.4f}")

print("\nFrequency Table:")
print(f"{'Sum':>5} | {'Frequency':>10} | {'Proportion':>10}")
print("-" * 32)
for s in range(2, 13):
    freq = sums.count(s)
    print(f"{s:>5} | {freq:>10} | {freq/500:>10.4f}")


# =============================================================================
# Q4. [User-Defined Functions + math module]
# Normal PDF function: f(x) = (1 / sigma*sqrt(2pi)) * e^(-(x-mu)^2 / 2*sigma^2)
# =============================================================================

import math

def normal_pdf(x, mu, sigma):
    coefficient = 1 / (sigma * math.sqrt(2 * math.pi))
    exponent = -((x - mu) ** 2) / (2 * sigma ** 2)
    return coefficient * math.exp(exponent)

mu, sigma = 70, 10
print(f"{'x':>5} | {'f(x)':>12}")
print("-" * 22)
for x in [60, 65, 70, 75, 80]:
    print(f"{x:>5} | {normal_pdf(x, mu, sigma):>12.6f}")
# f(70) is the peak (highest value, since x = mean)


# =============================================================================
# Q5. [Functions + Loops + Lists]
# summary_report(name, marks_list) — total, avg, highest, lowest, grade, pass/fail
# =============================================================================

def summary_report(name, marks_list):
    total   = sum(marks_list)
    avg     = total / len(marks_list)
    highest = max(marks_list)
    lowest  = min(marks_list)
    if avg >= 80:   grade = 'A'
    elif avg >= 65: grade = 'B'
    elif avg >= 50: grade = 'C'
    else:           grade = 'F'
    passed = avg >= 50
    print(f"\n--- Report for {name} ---")
    print(f"Marks   : {marks_list}")
    print(f"Total   : {total}")
    print(f"Average : {avg:.2f}")
    print(f"Highest : {highest} | Lowest : {lowest}")
    print(f"Grade   : {grade}")
    print(f"Result  : {'PASS' if passed else 'FAIL'}")

summary_report("Riya",  [78, 85, 90, 72, 88])
summary_report("Arjun", [45, 55, 40, 60, 35])
summary_report("Priya", [90, 95, 88, 92, 97])


# =============================================================================
# Q6. [Modules — random + Conditionals + Loops]
# Biased coin (P(H)=0.6), 200 tosses, proportion per group of 20
# =============================================================================

import random

results = ['H' if random.random() < 0.6 else 'T' for _ in range(200)]
heads = results.count('H')
tails = results.count('T')
print(f"Total Heads: {heads}, Total Tails: {tails}")
print(f"Overall Head Proportion: {heads/200:.4f}\n")

print(f"{'Group':>7} | {'Heads':>6} | {'Proportion':>12} | {'vs 0.6':>10}")
print("-" * 44)
for g in range(10):
    group   = results[g*20 : (g+1)*20]
    h_count = group.count('H')
    prop    = h_count / 20
    status  = "Above" if prop > 0.6 else ("Below" if prop < 0.6 else "Equal")
    print(f"{g+1:>7} | {h_count:>6} | {prop:>12.4f} | {status:>10}")


# =============================================================================
# Q7. [NumPy + statistics]
# 4x5 random int array — shape/ndim/size, row means, col sums,
# best row, z-score standardisation (no loops)
# =============================================================================

import numpy as np

np.random.seed(7)
A = np.random.randint(10, 101, size=(4, 5))
print("Matrix:\n", A)
print("\nShape:", A.shape, " | Ndim:", A.ndim, " | Size:", A.size)

row_means = np.mean(A, axis=1)
col_sums  = np.sum(A, axis=0)
print("Row means :", row_means)
print("Col sums  :", col_sums)

best_row = np.argmax(row_means)
print(f"Row with highest mean: Row {best_row+1} (mean={row_means[best_row]:.2f})")

# Z-score standardisation (element-wise, no loops)
mean = np.mean(A)
std  = np.std(A)
Z = (A - mean) / std
print("\nZ-score matrix (rounded):\n", np.round(Z, 2))


# =============================================================================
# Q8. [Strings + Lists + Functions]
# parse_records() and top_students() — parse CSV-style strings into dicts
# =============================================================================

def parse_records(records):
    result = []
    for r in records:
        parts = r.split(',')
        result.append({
            'name' : parts[0].strip(),
            'score': int(parts[1].strip()),
            'grade': parts[2].strip()
        })
    return result

def top_students(records, n):
    parsed = parse_records(records)
    sorted_records = sorted(parsed, key=lambda x: x['score'], reverse=True)
    return sorted_records[:n]

data = [
    "Riya, 88, A",
    "Arjun, 74, B",
    "Priya, 95, A",
    "Sam, 61, C",
    "Meera, 82, A",
    "Rohan, 55, D"
]

top3 = top_students(data, 3)
print("Top 3 Students:")
for i, s in enumerate(top3):
    print(f"  {i+1}. {s['name']:>8} — Score: {s['score']}, Grade: {s['grade']}")


# =============================================================================
# Q9. [math + statistics + Functions — Full Statistics Pipeline]
# analyse(data): mean, median, mode, variance, std, Pearson's skewness, shape
# =============================================================================

import statistics, math

def analyse(data):
    n        = len(data)
    mean     = statistics.mean(data)
    median   = statistics.median(data)
    mode     = statistics.mode(data)
    var      = statistics.variance(data)
    std      = statistics.stdev(data)
    skewness = 3 * (mean - median) / std    # Pearson's skewness formula

    if skewness > 0.1:    shape = "Positively Skewed (Right)"
    elif skewness < -0.1: shape = "Negatively Skewed (Left)"
    else:                 shape = "Approximately Symmetric"

    print(f"n        : {n}")
    print(f"Mean     : {mean:.4f}")
    print(f"Median   : {median:.4f}")
    print(f"Mode     : {mode}")
    print(f"Variance : {var:.4f}")
    print(f"Std Dev  : {std:.4f}")
    print(f"Skewness : {skewness:.4f}")
    print(f"Shape    : {shape}")

analyse([4, 7, 13, 2, 1, 9, 6, 4, 4, 12])


# =============================================================================
# Q10. [random + statistics + Loops — Central Limit Theorem Simulation]
# 1000 samples of size 30 from Uniform(0,100) — show sample means ≈ Normal
# =============================================================================

import random, statistics

random.seed(42)
sample_means = []
for _ in range(1000):
    sample = [random.uniform(0, 100) for _ in range(30)]
    sample_means.append(statistics.mean(sample))

overall_mean = statistics.mean(sample_means)
overall_std  = statistics.stdev(sample_means)

print(f"Number of samples      : 1000")
print(f"Each sample size       : 30")
print(f"Mean of sample means   : {overall_mean:.4f}  (expected ≈ 50)")
print(f"Std of sample means    : {overall_std:.4f}  (expected ≈ 100/√30 ≈ 5.27)")

# % of sample means within 1 std of 50
within_1std = sum(1 for m in sample_means if abs(m - 50) < overall_std)
print(f"Within 1 std of 50     : {within_1std/10:.1f}%  (expected ≈ 68%)")

q = statistics.quantiles(sample_means, n=4)
print(f"Q1={q[0]:.2f}, Median={q[1]:.2f}, Q3={q[2]:.2f}")
print(f"Min={min(sample_means):.2f}, Max={max(sample_means):.2f}")
