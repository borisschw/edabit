import subprocess

# run lsusb command to get USB device information
lsusb_output = subprocess.check_output(['lsusb']).decode('utf-8').split('\n')

# initialize empty list to store vendor and product IDs
usb_devices = []

# iterate over lsusb output and extract vendor and product IDs
for line in lsusb_output:
    if not line:
        continue
    fields = line.strip().split()
    # vendor_id, product_id = fields[5].split(':')
    print(fields[5])
    usb_devices.append(fields[5])

# print the dictionary of USB devices
print(usb_devices)
count = len([i for i in usb_devices if i=="1d6b:0003"])
print(count)
