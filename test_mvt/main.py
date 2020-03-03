from DRV8833_V2 import *

DRV8833_Sleep_pin = 'P20' # Pin SLEEP
DRV8833_AIN1 = 'P22' # Entree PWM moteur droit : AIN1
DRV8833_AIN2 = 'P21' # Entree PWM moteur droit : AIN2
DRV8833_BIN1 = 'P12' # Entree PWM moteur droit : AIN1
DRV8833_BIN2 = 'P19' # Entree PWM moteur droit : AIN2

Moteur_Droit = DRV8833_V2 (DRV8833_AIN1, DRV8833_AIN2,DRV8833_Sleep_pin, 1, 500, 2, 3, MOTEUR_DROIT_Flag)
Moteur_Gauche = DRV8833_V2 (DRV8833_BIN1, DRV8833_BIN2,DRV8833_Sleep_pin, 1, 500, 0, 1, MOTEUR_GAUCHE_Flag)

def Avancer (consigne_rotation_roue) :
    while (True):
        # Commande du moteur droit
        Moteur_Droit.Cmde_moteur(SENS_HORAIRE,consigne_rotation_roue)
        # Commande du moteur gauche
        Moteur_Gauche.Cmde_moteur(SENS_HORAIRE,consigne_rotation_roue)

def Reculer (consigne_rotation_roue) :
    while (True):
        # Commande du moteur droit
        Moteur_Droit.Cmde_moteur(SENS_ANTI_HORAIRE,consigne_rotation_roue)
        # Commande du moteur gauche
        Moteur_Gauche.Cmde_moteur(SENS_ANTI_HORAIRE,consigne_rotation_roue)

def Pivoter_droite (consigne_rotation_roue) :
    while (True):
        # Commande du moteur droit
        Moteur_Droit.Cmde_moteur(SENS_HORAIRE,consigne_rotation_roue/2)
        # Commande du moteur gauche
        Moteur_Gauche.Cmde_moteur(SENS_HORAIRE,consigne_rotation_roue)


def Pivoter_gauche (consigne_rotation_roue) :
    while (True):
        # Commande du moteur droit
        Moteur_Droit.Cmde_moteur(SENS_HORAIRE,consigne_rotation_roue)
        # Commande du moteur gauche
        Moteur_Gauche.Cmde_moteur(SENS_HORAIRE,consigne_rotation_roue/2)

consigne_rotation_roue = 0.5
Avancer(consigne_rotation_roue)
time.sleep (1)
Reculer(consigne_rotation_roue)
time.sleep (1)
Pivoter_gauche (consigne_rotation_roue)
time.sleep (1)
Pivoter_droite (consigne_rotation_roue)
