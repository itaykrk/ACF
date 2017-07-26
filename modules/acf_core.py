import queue
import threading
from time import sleep
from modules.adb import AndroidDebuggingBridge

DIRECTORY_NOT_FOUND = "No such file or directory"


class Acf(threading.Thread):
    def __init__(self, device_id, threads_num=20):
        threading.Thread.__init__(self)
        self.processes = []
        self._device_id = device_id
        self._command = "shell cat /proc/{pid}/net/icmp /proc/{pid}/net/tcp /proc/{pid}/net/udp /proc/{pid}/net/raw"
        self._adb = AndroidDebuggingBridge(device_id)
        self._processes_queue = queue.Queue()
        self._THREADS_NUM = threads_num
        self._create_threads()

    def run(self):
        while True:
            if self._processes_queue.empty():
                self._populate_processes_queue()
            sleep(0.8)

    def _populate_processes_queue(self):
        for p in self.processes:
            self._processes_queue.put(p)

    def _acm_worker(self):
        while True:
            process = self._processes_queue.get()
            output = AndroidDebuggingBridge.shell(self._command.format(pid=process.pid), self._device_id)
            if DIRECTORY_NOT_FOUND in output:
                self._processes_queue.task_done()
                continue
            conns = output.split("\r\n")
            process.updateConnections(conns)

            self._processes_queue.task_done()

    def _create_threads(self):
        for i in range(self._THREADS_NUM):
            t = threading.Thread(target=self._acm_worker)
            t.daemon = True
            t.start()
