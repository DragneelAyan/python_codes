# https://www.hackerrank.com/challenges/breaking-best-and-worst-records/problem?isFullScreen=true

# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#
def breakingRecords(scores):
    # Write your code here
    record = []
    high = scores[0]
    low = scores[0]
    highcount = 0
    lowcount = 0
    for i in range(1,len(scores)):
        if scores[i] > high:
            highcount += 1
            high = scores[i]
        elif scores[i] < low:
            lowcount +=1
            low = scores[i]
    record.append(highcount)
    record.append(lowcount)
    return(record)

if __name__ == '__main__':
    n = int(input().strip())
    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)
    print(result)
