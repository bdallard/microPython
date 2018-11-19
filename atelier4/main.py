'''
Activité sur la photo résistance 
'''

import pyb 

#lecture des valeurs 
ldr = pyb.ADC( 'X19' )
while True:
    lecture = ldr.read()
    tension = (lecture * 3.3) / 4095
    print( 'valeur = %s, tension = %s volts' % (lecture, tension) )
    pyb.delay( 300 )


#modulation de la lumière 
# Lecture analogique LDR pour controler la puissance d'une LED PWM.
# ATTENTION: ..chantillonnage 12 Bits (valeur de 0 .. 4096)
from pyb import Timer, delay

# Creer un timer à une fréquence de 100 Hz (le timer 5)
# Créer un canal (channel) PWM avec le Timer.  
tim = pyb.Timer( 5, freq=100)
tchannel = tim.channel(1, Timer.PWM, pin=pyb.Pin.board.X1, pulse_width=0)

# Minimum et Maximum de largeur d'impulsion correspondant au minimum
# et maximum de luminosité
max_width = 150000
min_width = 0100

# Minimum et Maximum de valeur analogique correspondant au variation
# de lumière sur la LDR. Valeur relevée avec le programme précédent
max_ldr = 2750
min_ldr = 680 

# fonction qui permet de passer d'un range de valeur (in_) à une autre
#    (out_) en appliquant une règle de trois. 
def arduino_map(x, in_min, in_max, out_min, out_max):
    return int( (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min )
    
ldr = pyb.ADC( 'X19' )
while True:
	# lecture analogique
    lecture = ldr.read()
    
    # Transformer une valeur analogique (0 .. 4096) en largeur d'impulsion (20000 .. 2000000) 
    pulse_width = arduino_map( lecture, min_ldr, max_ldr, min_width, max_width )
    
    # Modifier le signal PWM
    tchannel.pulse_width( pulse_width )
    
    delay( 100 )


#Couvre la photo-résistance avec ton doigt (sans la toucher). La luminosité de la LED devrait diminuer. Ecarte ton  doigt et la LED devrait s'éclairer plus fort.
