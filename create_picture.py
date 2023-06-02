from collections import Counter
import numpy as np
import matplotlib.pyplot as plt

LANG = "Rust"

with open(f"./{LANG}.csv") as f:
    lines = f.read().splitlines()

ranked = [ (k,v) for k,v in Counter(lines).items() if v >= 2 and k != '""']
ranked = sorted(ranked, key=lambda x: x[1])
labels, values = zip(*ranked)

indexes = np.arange(len(labels))

plt.figure(figsize=(10,len(labels)//5))
plt.subplots_adjust(left=0.2)
plt.barh(indexes, values, 0.8)
plt.yticks(indexes, labels)
plt.title(LANG)
plt.savefig(f'{LANG}.png')