import time
from threading import Thread, Event

class Timer:
    def __init__(self, name):
        self.name = name
        self.start_time = None
        self.elapsed_time = 0
        self.running = False
        self._stop_event = Event()

    def start(self):
        if not self.running:
            self.start_time = time.time() - self.elapsed_time
            self.running = True
            self._stop_event.clear()
            Thread(target=self._run).start()

    def _run(self):
        while self.running and not self._stop_event.is_set():
            self.elapsed_time = time.time() - self.start_time
            time.sleep(0.1)

    def pause(self):
        if self.running:
            self.running = False
            self.elapsed_time = time.time() - self.start_time

    def stop(self):
        self.running = False
        self.elapsed_time = 0

    def reset(self):
        self.stop()
        self.start()

    def get_time(self):
        return self.elapsed_time

class TimerManager:
    def __init__(self):
        self.timers = {}

    def add_timer(self, name):
        if name not in self.timers:
            self.timers[name] = Timer(name)

    def get_timer(self, name):
        return self.timers.get(name)

    def remove_timer(self, name):
        if name in self.timers:
            del self.timers[name]

# Example usage
if __name__ == "__main__":
    manager = TimerManager()
    manager.add_timer("Timer1")
    timer = manager.get_timer("Timer1")
    timer.start()
    time.sleep(2)
    timer.pause()
    print(f"Elapsed time: {timer.get_time()} seconds")
    timer.reset()
    time.sleep(1)
    timer.stop()
    print(f"Elapsed time after reset: {timer.get_time()} seconds")
