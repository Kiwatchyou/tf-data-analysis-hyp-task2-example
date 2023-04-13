import pandas as pd
import numpy as np
from scipy.stats import anderson_ksamp


chat_id = 390760498 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array, y: np.array) -> bool:
    alpha = 0.1
    pvalue = anderson_ksamp([x, y])[2]
    return pvalue < alpha


