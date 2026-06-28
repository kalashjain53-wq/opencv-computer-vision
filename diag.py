import numpy as np
p = list(np.load('people.npy', allow_pickle=True))
print("Index -> Name mapping:")
for i, name in enumerate(p):
    print(f"  {i} -> {name}")