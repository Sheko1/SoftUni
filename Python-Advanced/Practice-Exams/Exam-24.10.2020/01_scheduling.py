def find_min_num(jobs_list):
    return min([int(num) for num in jobs_list if num.isdigit()])


jobs = input().split(", ")
index = int(input())
clock_cycles = 0

while True:
    job_to_remove = find_min_num(jobs)
    clock_cycles += job_to_remove

    curr_index = jobs.index(str(job_to_remove))
    jobs[curr_index] = ""

    if curr_index == index:
        print(clock_cycles)
        break
