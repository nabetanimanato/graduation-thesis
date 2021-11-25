import datetime
class Worker:
    def __init__(self,no,state = 0):
        self.no = no
        self.state = state
class Machine:
    def __init__(self,no,state = 0):
        self.no = no
        self.state = state

worker1 = Worker(1)
worker2 = Worker(2)
machine1 = Machine(1)
now_time = None

worker_list = [worker1,worker2]
machine_list = [machine1]

def process_state(worker,machine,process_time,start):
    global now_time
    if worker.state == 0 & machine.state == 0:
        if start is None:
            start = datetime.datetime(2021,11,15)
        else:
            start = now_time
        finish = start + datetime.timedelta(minutes = process_time)
        while start <= finish:
            worker.state = 1
            machine.state = 1
            start += datetime.timedelta(minutes = 1)
            print(f"作業者番号{worker.no}\t{worker.state}")
            print(f"機械番号  {machine.no}\t{machine.state}")
        else:
            worker.state = 0
            machine.state = 0
            print(f"作業者番号{worker.no}\t{worker.state}")
            print(f"機械番号  {machine.no}\t{machine.state}")
            now_time = finish
            print(now_time)

process_state(worker_list[0],machine_list[0],1,now_time)