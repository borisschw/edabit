import usb.core
import usb.util

class UsbDevice():
    def __init__(self):
        self.dev = None

    def connect(self):
            # Check if the device is connected
            try:
                self.dev.get_active_configuration()
                self.logger.info("Already connected to device.")
                return
            except:
                self.logger.info("No active configuration found for device.")
                pass

            self.logger.info("Connect to Device...")
            # Find the USB device
            self.dev = usb.core.find(idVendor=self.vid, idProduct=self.pid)
            if self.dev is None:
                raise Exception("USB device not found.")

            if self.dev.is_kernel_driver_active(0):
                self.logger.debug("detaching kernel driver")
                self.dev.detach_kernel_driver(0)

            self.cfg = self.dev.get_active_configuration()
            self.intf = self.cfg[(0,0)]

            self.ep_out = usb.util.find_descriptor(
                self.intf,
                # match the first OUT endpoint
                custom_match = \
                lambda e: \
                    usb.util.endpoint_direction(e.bEndpointAddress) == \
                    usb.util.ENDPOINT_OUT)
            if self.ep_out is None:
                self.logger.error("OUT endpoint not found")
                raise Exception("OUT endpoint not found")

            self.ep_in = usb.util.find_descriptor(
                self.intf,
                # match the first IN endpoint
                custom_match = \
                lambda e: \
                    usb.util.endpoint_direction(e.bEndpointAddress) == \
                    usb.util.ENDPOINT_IN)
            if self.ep_in is None:
                self.logger.error("IN endpoint not found")
                raise Exception("IN endpoint not found")