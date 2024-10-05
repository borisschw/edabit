import subprocess
GPIO=436

export_gpio = "echo 436 > /sys/class/gpio/export"
directio_gpio = 'echo out > /sys/class/gpio/gpio436/direction'
gpio_val = 1
set_gpio_val = 'echo 1 > /sys/class/gpio/gpio436/value'

subprocess.check_output(export_gpio, shell=True),
subprocess.check_output(directio_gpio, shell=True),
subprocess.check_output(set_gpio_val, shell=True),



