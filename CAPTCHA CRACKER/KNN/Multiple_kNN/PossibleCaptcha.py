# PossiblePlate.py

import cv2
import numpy as np

###################################################################################################
class PossibleCaptcha:

    # constructor #################################################################################
    def __init__(self):
        self.imgPlate = None
        self.imgGrayscale = None
        self.imgThresh = None

        self.rrLocationOfPlateInScene = None

        self.strChars = ""
    # end constructor

# end class
