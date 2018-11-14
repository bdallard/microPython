'''
Premier script : controle de LED 
''' 
#import de la librairie 
import pyb 

#définition des led avec tableau 
leds = [pyb.LED(i) for i in range(1,5)]
for l in leds:
    l.off()

#affichage de la led 
n = 0
try:
   while True:
      n = (n + 1) % 4
      leds[n].toggle()
      pyb.delay(50)
finally:
    for l in leds:
        l.off()


