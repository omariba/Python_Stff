import statistics

nums = [12,33,2,4,8,9]
names = ["pup","nun","kun","sus","lul","nun"]

try:
    statistics.median(nums)
    print(statistics.mode(nums))
    ans = statistics.pvariance(nums)
    # print(ans) 
    # print(statistics.mean(nums))
    # print(sum(nums))
except ValueError:
    print('None found')