import pandas
import numpy

import frac1
import frac2
import footing
import end

workout = pandas.date_range("2023/01/01", "2023/12/31", freq='w-mon')

min_len = min(len(frac1.frac1.T), len(frac2.frac2.T), len(footing.footing.T),
              len(end.end.T)) - 1

DATE = []
for d in range(min_len):
    DATE.append(pandas.to_datetime(workout).strftime('%d.%m.%Y'))

df = pandas.DataFrame({
    # 'date': workout[:3],
    'date':
    DATE[0][:min_len],
    'des_frac1': [frac1.frac1[[str(i + 1)]].values[0] for i in range(min_len)],
    'frac1': [[
        float(frac1.frac1[[str(i + 1)]].values[1]),
        float(frac1.frac1[[str(i + 1)]].values[2]),
        float(frac1.frac1[[str(i + 1)]].values[3])
    ] for i in range(min_len)],
    'des_frac2': [frac2.frac2[[str(i + 1)]].values[0] for i in range(min_len)],
    'frac2': [[
        float(frac2.frac2[[str(i + 1)]].values[1]),
        float(frac2.frac2[[str(i + 1)]].values[2]),
        float(frac2.frac2[[str(i + 1)]].values[3])
    ] for i in range(min_len)],
    'des_footing':
    [footing.footing[[str(i + 1)]].values[0] for i in range(min_len)],
    'footing': [[
        float(footing.footing[[str(i + 1)]].values[1]),
        float(footing.footing[[str(i + 1)]].values[2]),
        float(footing.footing[[str(i + 1)]].values[3])
    ] for i in range(min_len)],
    'des end': [end.end[[str(i + 1)]].values[0] for i in range(min_len)],
    'end': [[
        float(end.end[[str(i + 1)]].values[1]),
        float(end.end[[str(i + 1)]].values[2]),
        float(end.end[[str(i + 1)]].values[3])
    ] for i in range(min_len)],
})

print(df)
