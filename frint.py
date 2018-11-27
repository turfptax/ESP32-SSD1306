
#-- Main program
#-- Requires SSD1306 from adafruit
import machine, ssd1306, socket

# Thank you Ada Fruit
#Initialize the 128*64 SSD1306 screen pins are 15 & 4 onb
i2c = machine.I2C(scl=machine.Pin(15), sda=machine.Pin(4))
#i2c = machine.I2C(scl=machine.Pin(4), sda=machine.Pin(5))

# Tip to get the oled=ssd1306 to work on ESP32
pin = machine.Pin(16,machine.Pin.OUT)
pin.value(0)
pin.value(1)

#Functions
def screenwipe():
  for x in range(0,128):
    for y in range(0,64):
      oled.pixel(x,y,1)
    oled.show()

  for x in range(0,128):
    for y in range(0,64):
      oled.pixel(x,y,0)
    oled.show()
    
def frint(text):
  global ram
  global cur
 
  lent = 0
  if type(text) != str:
    text = str(text)
  
  oled.fill(0)
  l = len(text)
  c = 0
  x = 0
  buff = ''
  outp = []
  if l > 16:
    for i in text:
      if c < 15:
        buff += i
        c += 1
      else:
        outp.append(buff+i)
        buff = ''
        c = 0
        x += 1
    if buff != '':
      outp.append(buff)
      

  else:
    outp.append(text)
  lent = len(outp)
  
  #cur += 1
  print('what?')
  print('what?')

    
  for z in range(len(outp)):
    ram.append(outp[z])
    #oled.text(outp[z],0,z*10
  for z in range(0,6):
    oled.text(ram[-(6+z)],0,z*10)
  
  oled.show()
  return outp,'Return of frints buff'
      
         

try:
  oled = ssd1306.SSD1306_I2C(128,64,i2c)
  frint("SSD1306 - Good")
  print("ssid1306 - success")
except:
  print("failed to initialize onboard SSD1306")


frint('importing Network')
try:
  import network
  frint('import network  SUCCESS')
  print('import network SUCCESS')
except:
  frint('import network failed')
station = network.WLAN(network.STA_IF)
station.active(True)
station.connect("SSID","Password")
frint(station.isconnected())
frint(station.ifconfig())


try:
  s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
except:
  frint("socket s= s.s failed")
  
#s.bind(('0.0.0.0',8888))
#pext = s.recvfrom(10)
#frint(pext)

frint(machine.freq())



