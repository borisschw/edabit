import sys
import threading
from time import sleep

class TimerExit:
    def quit_function(self, fn_name):
        print('{0} took too long'.format(fn_name), file=sys.stderr)
        sys.stderr.flush()
        threading.main_thread().interrupt()  # Raises KeyboardInterrupt

    def exit_after(self, s):
        '''
        Use as decorator to exit process if
        function takes longer than s seconds
        '''
        def outer(fn):
            def inner(*args, **kwargs):
                timer = threading.Timer(s, self.quit_function, args=[fn.__name__])
                timer.start()
                try:
                    result = fn(*args, **kwargs)
                finally:
                    timer.cancel()
                return result
            return inner
        return outer

    @exit_after(10)
    def countdown(self, n):
        print('Countdown started', flush=True)
        for i in range(n, -1, -1):
            print(i, end=', ', flush=True)
            sleep(1)
        print('Countdown finished')

# Example usage
timer_exit = TimerExit()
timer_exit.countdown(5)  # This will timeout after
