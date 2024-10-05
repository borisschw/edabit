from usb.core import find as finddev
dev = finddev(idVendor=0x1d50, idProduct=0x6089)
dev.reset()
#1d50:6089