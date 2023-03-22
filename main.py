# python3

def parallel_processing(n, m, data):
    output = []
    n=[0]*n
    i=0
    time=0
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    while (i<len(data)):
        for j in range(len(n)):
            if n[j]<=time:
                n[j]+=data[i]
                output.append(j)
                output.append(time)
                i+=1
        time+=1
    return output

def main():
    # TODO: create input from keyboard
    # input consists of two lines
    # first line - n and m
    # n - thread count 
    # m - job count
    n = 0
    m = 0
    data1 = list(map(int, input().split()))
    n=int(data1[0])
    m=int(data1[1])
    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = []
    data = list(map(int, input().split()))

    assert len(data) == m
    assert n>0
    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for i in range(0,len(result)-1,2):
        print(result[i],result[i+1])


if __name__ == "__main__":
    main()
