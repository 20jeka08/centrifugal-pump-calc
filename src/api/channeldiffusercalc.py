import numpy as np
from typing import Optional
from dataclasses import dataclass
from src.api.impellercalc import ImpellerCalc


@dataclass
class ChannelDiffuserCalc(ImpellerCalc):
    ns: Optional[float] = None
    nq: Optional[float] = None
    Hi: Optional[int] = None

    def D3_D2(self):
        '''Recomended value of D3 to D2 ratio by Gulich'''
        nq = self.nq
        if self.Hi < 100:
            D3toD2 = 1.015
        else:
            if nq < 40:
                D3toD2 = 1.015+0.08*((self.ro*self.Hi)/(1000*1000)-0.1)**0.8
            else:
                D3toD2 = 1.04+0.001*(nq-40)

        return D3toD2

    def D3(self, D2, D3toD2):
        '''Calculation of radial position of Leading edge of stator vanes - D3 [mm]'''
        D3 = D2*D3toD2
        return D3

    




