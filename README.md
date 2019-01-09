# ESP32-SSD1306
ESP32 SSD1306 micropython screen HITEK library thingie

impetus: https://www.instructables.com/id/MicroPython-on-an-ESP32-Board-With-Integrated-SSD1/
This instructalbe was what made me want to create a CLI interface with the esp32 board. I am not that good with many programming languages so, when I found I could use python on the board it piqued my interest.

Scope:
The scope of this project is to make a psudo library for wraping text onto a screen attached to the esp32 chip using mycropython. The current itteration saves all printed(frinted) things in an array called ram. I am new to using micropython and will be interested in seeing how/if i can optimize code to run more/less smoothly on the esp32.

Requres the adafruit ssd1306 library

The pins for the I2C are different than 5 and 4 see code

Need appropriate firmware for the ESP32

Will be documenting as I go along

