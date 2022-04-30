import numpy as np
from dataclasses import dataclass
from typing import Optional

@dataclass
class Parameters:
    # Input initial parameters of centrifugal pump
    Q: Optional[float] = None
    H: Optional[float] = None
    n: Optional[float] = None
    i: Optional[int] = None

    @property
    def H_st(self) -> float:
        H_st = self.H/self.i
        return H_st

