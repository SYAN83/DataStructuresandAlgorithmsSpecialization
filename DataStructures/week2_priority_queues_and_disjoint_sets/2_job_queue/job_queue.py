# python3

from collections import namedtuple
import heapq

AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    result = list()
    queue = [(0, w) for w in range(n_workers)]
    while jobs:
        job = jobs.pop(0)
        t, w = heapq.heappop(queue)
        result.append(AssignedJob(w, t))
        heapq.heappush(queue, (t + job, w))
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
