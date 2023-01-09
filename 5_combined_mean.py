def mean(arr):
    return sum(arr)/len(arr)
def sd(arr, n):
   sum = 0;
   for i in range(n):
      sum = sum + ((arr[i] - mean(arr)) * (arr[i] - mean(arr)))
   sdd = sum / n
   return sdd
def combinedVariance(A1, A2):
   n = len(A1)
   m = len(A2)
   mean1 = mean(A1)
   mean2 = mean(A2)
   print("mean_1: ", round(mean1, 2), " mean_2: ", round(mean2, 2))
   sd1 = sd(A1, n)
   sd2 = sd(A2, m)
   print("sd_1: ", round(sd1, 2)," sd_2: ", round(sd2, 2))
   combinedMean = (n * mean1 + m * mean2) / (n + m)
   print("Combined Mean: ", round(combinedMean, 2))
   d1_square = ((mean1 - combinedMean) * (mean1 - combinedMean))
   d2_square = ((mean2 - combinedMean) * (mean2 - combinedMean))
   print("d1_square: ", round(d1_square, 2), " d2_square: ", round(d2_square, 2))
   comb_var = (n * (sd1 + d1_square) + m * (sd2 + d2_square)) / (n + m)
   print("Combined Variance: ", round(comb_var, 2))
A1 = [24, 46, 35, 79, 13, 77, 35 ]
A2 = [66, 68, 35, 24, 46 ]
n = len(A1)
m = len(A2)
combinedVariance(A1, A2)