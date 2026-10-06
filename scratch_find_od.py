import json

with open('notebooks/02_system_modeling.ipynb', 'r', encoding='utf-8') as f:
    nb = json.load(f)

for idx, cell in enumerate(nb['cells']):
    src = ''.join(cell.get('source', []))
    keywords = ['cantonal-reference', 'od demand', 'corridor_regions', 'od key', 'od pairs', 'od_pairs', 'origin-destination']
    for kw in keywords:
        if kw in src.lower():
            print(f"Cell {idx} ({cell['cell_type']}) matched '{kw}':")
            lines = src.split('\n')
            for line in lines[:8]:
                print("   ", line)
            print("---")
            break
