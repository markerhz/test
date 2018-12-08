import spidev
import time
analog_ch = 1
spi = spidev.SpiDev(0,0)
spi.max_speed_hz=1200000
spi.open(0, 0)
def readADC(adcnum):
	if adcnum > 7 or adcnum < 0:
		return -1;
	r = spi.xfer2([4 | 2 | (adcnum >> 2), (adcnum & 3) <<6, 0])
	adcout = ((r[1] & 15) << 8) + r[2]
	return adcout
while True:
	value = readADC(analog_ch)
	print(value)
 	time.sleep(0.3)
