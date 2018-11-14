'''
Le potentiomètre
'''

import pyb

# Lecture analogique pour controler la puissance d'une LED PWM.
# ATTENTION: échantillonnage 12 Bits (valeur de 0 à 4096)
from pyb import Timer, delay

adc = pyb.ADC(pyb.Pin.board.X19)    # Créer ADC sur la broche  X19

# Creer un timer à une fréquence de 100 Hz (le timer 5)
# Créer un canal (channel) PWM avec le Timer.  
tim = pyb.Timer( 5, freq=100)
tchannel = tim.channel(1, Timer.PWM, pin=pyb.Pin.board.X1, pulse_width=0)

# Minimum et Maximum de largeur d'impulsion correspondant au minimum
# et maximum de luminosité
max_width = 150000
min_width = 8000

# fonction qui permet de passer d'un range de valeur (in_) à une autre
#    (out_) en appliquant une règle de trois. 
def arduino_map(x, in_min, in_max, out_min, out_max):
    return int( (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min ) 

while True:
	# Lectures analogiques
    ivalue = adc.read()
    
    # Transformer une valeur analogique (0 à 4096) en largeur d'impulsion (20000 à 2000000) 
    pulse_width = arduino_map( ivalue, 0, 4096, min_width, max_width )
    
    # Modifier le signal PWM
    tchannel.pulse_width( pulse_width )
    
    delay( 100 )

