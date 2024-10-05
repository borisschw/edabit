import bisect
values = [0.001, 0.05, 0.08, 0.1, 0.4, 0.8, 0.9, 0.95, 0.99]
print(bisect.bisect_left(values, .08))
