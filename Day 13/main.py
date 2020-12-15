# Part 1

def main():
    filename = 'path.txt'
#    filename = 'example'
    with open(filename,'r') as infile:
        timestamp = int(infile.readline().strip())
        bus_IDs = [int(i) for i in infile.readline().strip().split(",") if i != 'x']

    print(f"Timestamp: {timestamp}")
    print(f"Bus IDs: {bus_IDs}")

    from_timestamp = [(i,(i - (timestamp % i))) for i in bus_IDs]
    from_timestamp_sorted = sorted(from_timestamp,key=lambda i:i[1])

    print(f"from_timestamp_sorted : {from_timestamp_sorted}")

    closest_bus = from_timestamp_sorted[0]
    print(f"Closest Bus: {closest_bus}")
    print(closest_bus[0] * closest_bus[1])

if __name__ == "__main__":
    main()



## Part 2

from functools import reduce
import math

def get_inverse(N_i,n_i):
    while N_i > n_i:
        N_i = int(N_i % n_i)
    x_i = 0
    while int((N_i * x_i) % n_i) != 1:
        x_i +=1
    return int(x_i)

def main():
    filename = 'path.txt'
    #filename = 'example2'

    with open(filename,'r') as infile:
        timestamp = int(infile.readline().strip())
        bus_IDs = [(int(i),(int(i) - index)%(int(i)),index)
                for index,i in enumerate(
                    infile.readline().strip().split(",")) if i != 'x']


    N = reduce(lambda x,y: x*y,[bus[0] for bus in bus_IDs])

    x = 0
    for n_i, b_i, i in bus_IDs:
        N_i = N // n_i
        x_i = get_inverse(N_i, n_i)
        x += b_i * x_i * N_i

    print(int(x%N))

if __name__ == "__main__":
    main()
