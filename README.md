# Graph Sets

Hand-curated graph datasets for fast experimentation with graph neural networks. Loaders return PyTorch-ready tensors so you can focus on modeling instead of wrangling benchmark data.

## Installation

- `pip install graphsets`

## Usage

```python
from graphsets import load_cora

# directory containing cora.content and cora.cites from the standard Cora release
data_dir = "/path/to/cora"

features, adj, labels, idx_train, idx_val, idx_test = load_cora(data_dir)
```

## What you get

- Features: float tensor of node attributes (row-normalized).
- Adjacency: symmetric 0/1 tensor built from `cora.cites`.
- Labels: integer class ids matching the original paper labels.
- Splits: simple train/val/test indices (140/300/1000 nodes) for quick baselines.

## Datasets

- `cora` — citation network commonly used for GCN/GAT benchmarks.
