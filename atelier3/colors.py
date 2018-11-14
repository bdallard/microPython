'''
plus de couleur 
'''
import pyb 

RED_PIN = pyb.Pin.board.Y10    # Led rouge
GREEN_PIN = pyb.Pin.board.Y11  # Led verte
BLUE_PIN = pyb.Pin.board.Y12   # Led bleue

# Déclaration des broches
pRed = pyb.Pin( RED_PIN, pyb.Pin.OUT_PP )
pGreen = pyb.Pin( GREEN_PIN, pyb.Pin.OUT_PP )
pBlue = pyb.Pin( BLUE_PIN, pyb.Pin.OUT_PP )

# Déclaration des 3 broches la LED RGB 
pRGB = (pRed,pGreen,pBlue)

# Assigne l'etat des broches rouge,vert,bleu à partir d'un tuple de 
# 3 éléments tels que  (True,True,True)
def set_led( p_rgb, state_tuple ):
	for i in range(0,3):
		# Note: Une led est activée si l'on met la broche correspondante
		#       a GND.
	    p_rgb[i].value( not( state_tuple[i] ) ) 

# Faire un mix de deux états RGB pour en composer un troisième.
# Rouge (True,False,False) + Bleu (False,False,True) = Magenta (True,False,True)
def mix_color( color1, color2 ):
    return (color1[0] | color2[0], color1[1] | color2[1], color1[2] | color2[2] ) 

# Désactivation des LEDs
set_led( pRGB, (False, False, False) )

# Sequences d'allumage des LEDs R,G,B
noir  = (False,False,False)
rouge = (True,False,False)
vert  = (False,True,False)
bleu  = (False,False,True)  
jaune = mix_color( rouge, vert )
cyan  = mix_color( vert, bleu )
magenta = mix_color( bleu, rouge )
 
sequences = [ 
    rouge, vert, bleu, noir, # Couleurs de base
    rouge, jaune, vert, cyan, bleu, magenta # Suivre la rouge des couleurs
    ]
    
# Initialiser la LED à toutes les séquences
for seq in sequences:
	set_led( pRGB, seq )
	# Attendre 2 secondes
	pyb.delay( 2000 )
	
set_led( pRGB, noir )


