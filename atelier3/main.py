'''
Activité sur la lumière : la LED tricolore 
''' 
import pyb 

RED_PIN = pyb.Pin.board.Y10    # Led rouge
GREEN_PIN = pyb.Pin.board.Y11  # Led verte
BLUE_PIN = pyb.Pin.board.Y12   # Led bleue

# Déclaration des broches
pRed = pyb.Pin( RED_PIN, pyb.Pin.OUT_PP )
pGreen = pyb.Pin( GREEN_PIN, pyb.Pin.OUT_PP )
pBlue = pyb.Pin( BLUE_PIN, pyb.Pin.OUT_PP )

# Eteindre la LED
pRed.high()
pGreen.high()
pBlue.high()

# Allumer la led ROUGE
pRed.low()
pGreen.high()
pBlue.high()

# Attendre 1 secondes
pyb.delay( 1000 )
	
# Allumer la led BLEUE
pRed.high()
pGreen.high()
pBlue.low()

# Attendre 1 secondes
pyb.delay( 1000 )    

# Allumer la led VERTE
pRed.high()
pGreen.low()
pBlue.high()

# Attendre 1 secondes
pyb.delay( 1000 )    

# Allumer en BLANC (toutes les LEDs allumées)
pRed.low()
pGreen.low()
pBlue.low()

# Attendre 1 secondes
pyb.delay( 1000 )    

# Tout en noir (toutes les LEDs éteintes)
pRed.high()
pGreen.high()
pBlue.high()



