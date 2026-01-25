from statistics import mean


def findMaxAverage(nums, k) -> float:

    cum_sum = 0

    for i in range(k):
        cum_sum += nums[i]

    max_avg = cum_sum / k

    for i in range(k, len(nums)):
        cum_sum += nums[i]
        cum_sum -= nums[i-k]
        avg = cum_sum / k

        max_avg = max(max_avg, avg)

    return max_avg


print(findMaxAverage(nums=[1, 12, -5, -6, 50, 3], k=4))
