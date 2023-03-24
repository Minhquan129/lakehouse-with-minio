import pandas as pd
import numpy as np
from helpers import load_cfg

CFG_PATH = './utils/cfg.yml'

if __name__ == '__main__':
    start_ts = '25-09-2022'
    end_ts = '25-09-2023'
    features = ['pressure', 'velocity', 'speed']

    ts = pd.date_range(start=start_ts, end=end_ts, freq='H')
    df = pd.DataFrame(ts, columns=['event_timestamp'])
    df = df.set_index('event_timestamp')
    
    for feature in features:
        df[feature] = np.random.random_sample((len(ts),))
    
    cfg = load_cfg(CFG_PATH)
    df.to_parquet(cfg['fake_data_path'])