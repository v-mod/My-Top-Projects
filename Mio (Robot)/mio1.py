from bluezero import microbit
from bluezero import async_tools

ubit = microbit.Microbit(device_addr='D6:38:02:51:F5:83',
                         accelerometer_service=False,
                         button_service=False,
                         led_service=False,
                         magnetometer_service=False,
                         pin_service=False,
                         temperature_service=False,
                         uart_service=True)
eloop = async_tools.EventLoop()
ubit.connect()


def ping():
    ubit.uart = 'ping#'
    return True


def goodbye():
    ubit.quit_async()
    ubit.disconnect()
    return False


ubit.subscribe_uart(print)
eloop.add_timer(30000, goodbye)

ubit.run_async()