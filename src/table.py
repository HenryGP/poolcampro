import itertools
import numpy as np
import cv2

class Table():
    '''
    Constructor:
        - Input:
            - corners: matrix with x,y,d 
            - boundaries: matrix with [x,y]
    '''
    def __init__(self, corners=np.zeros(shape=(4,2)), boundaries=np.zeros(shape=(4,2)), calibrated=False):
        self.corners=corners
        self.boundaries=boundaries
        self.calibrated=calibrated
    
    def is_calibrated(self):
        return self.calibrated

    def set_calibration(self,calibration):
        self.calibrated=calibration
        self.save_calibration_details()

    def calibrate_table(self,corners):
        if len(corners[0])<4: #Good luck next time
            return corners
        else: 
            truncated = np.delete(corners,2,2)
            linearized = np.asarray(truncated[0])
            shapes=list(itertools.permutations(linearized, 4))
            for shape in shapes:
                shape = np.array(shape)
                peri = cv2.arcLength(shape, True)
                approx = cv2.approxPolyDP(shape, 0.02 * peri, True)
                if len(approx) == 4:
                    table_boundaries = approx
                    break
            self.boundaries=table_boundaries
            self.corners=corners

    def get_table_details(self):
        return self.corners,self.boundaries

    def save_calibration_details(self):
        np.save('data/table_calibration/corners', self.corners)
        np.save('data/table_calibration/boundaries',self.boundaries)