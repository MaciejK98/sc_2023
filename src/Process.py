class Process:
    class Agenda:
        def init(self, comparator):
            self.processes = []
            self.comparator = comparator
            
        def push(self, process):
            self.processes.append(process)
            self.processes.sort(key=lambda x: self.comparator(x))

        def pop(self):
            return self.processes.pop(0)

        def top(self):
            return self.processes[0]

        def empty(self):
            return len(self.processes) == 0

        def size(self):
            return len(self.processes)

    def __init__(self, time, wireless_network, agenda):
        # self.state = self.State.GENERATE_PACKET
        self.time = time
        self.terminated = False
        self.wireless_network = wireless_network
        self.agenda = agenda

    def execute(self):
        pass

    def activate(self, time, relative=True):
        if relative:
            self.time += time
        else:
            self.time = time
        self.agenda.push(self)

    def is_terminated(self):
        return self.terminated

    def set_terminated(self):
        self.terminated = True
