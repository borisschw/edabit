import time
import logging
from queue import Queue

# Example class with necessary attributes
class ExampleClass:
    def __init__(self):
        self.commands_q = Queue()
        self.THREAD_INTERVEL_SEC = 1  # Example interval time
        self.COMMAND_VALID_TIMEOUT_SEC = 10  # Example timeout
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(level=logging.DEBUG)

    def blocking(func):
        def wrapper(self, *args, **kwargs):
            result = func(self, *args, **kwargs)

            # Get the command_q length
            queue_length = self.commands_q.qsize()

            # The time the command will be executed depends on the queue length
            # Added 2 extra iterations to make sure the command is executed
            time_to_wait_sec = (queue_length + 3) * self.THREAD_INTERVEL_SEC
            self.logger.debug("Waiting for function {}, {} seconds".format(func.__name__, time_to_wait_sec))

            time.sleep(min(time_to_wait_sec, self.COMMAND_VALID_TIMEOUT_SEC))
            return result
        return wrapper

    @blocking
    def example_function(self):
        # Example function body
        print("Function executed.")

# Example usage
example = ExampleClass()
example.example_function()
