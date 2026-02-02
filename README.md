# SPAR - Sequential Pattern Averaging Regressor

A non-parametric time series forecasting model that identifies discrete directional patterns and predicts future movements based on historical outcomes.

![Python](https://img.shields.io/badge/python-3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

## Installation

```bash
pip install spar-model
```

Or install from source:

```bash
git clone https://github.com/sofienkaabar/spar-model.git
cd spar-model
pip install -e .
```

**Optional:** Install `numba` for 5-10x faster performance:

```bash
pip install numba
```

## Quick Start

```python
from spar import SPAR
import numpy as np

# Your price data
prices = np.array([100, 101, 99, 102, 103, 101, 104, 105, 103, 106, ...])

# Create and fit model
model = SPAR(field=5, min_instances=3)
model.fit(prices[:-50])  # Train on historical data

# Predict
recent_prices = prices[-6:]  # Need field+1 values
result = model.predict(recent_prices)

print(result['signal'])           # 'bullish', 'bearish', or 'flat'
print(result['predicted_values']) # Forecasted prices
print(result['hit_ratio'])        # Majority ratio
print(result['instances'])        # Number of pattern matches
```

## How It Works

SPAR encodes price movements into discrete patterns and uses majority voting:

### 1. Pattern Encoding
Each period is classified as Up (U), Down (D), or Flat (F) based on percentage change:

```
Price:    100 → 102 → 101 → 103 → 105
Pattern:      U     D     U     U
Key:      "UDUU|P" (P = overall positive)
```

### 2. Majority Vote
When a pattern is matched, SPAR counts historical outcomes:
- If 60% of outcomes were bullish → Signal = **bullish**
- If 60% of outcomes were bearish → Signal = **bearish**
- If 50/50 → Signal = **flat** (no prediction)

### 3. Median Path Forecast
Instead of averaging all outcomes (which can cancel out), SPAR:
1. Filters to only outcomes matching the majority direction
2. Takes the **median path** of those filtered outcomes
3. Produces a cleaner, more representative forecast

## Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `field` | int | required | Pattern length and forecast horizon (recommended: 3-10) |
| `min_instances` | int | 5 | Minimum matches in majority direction for prediction |
| `flat_threshold` | float | 0.0001 | Changes below this are "flat" |
| `smoothing` | bool | False | Apply EMA smoothing to reduce noise |
| `smoothing_period` | int | 2 | EMA period (2-5) |
| `structural` | bool | True | Preserve forecast shape (vs linear) |

## API Reference

### `SPAR.fit(X)`

Fit the model on training data.

- **X**: 1D array of prices
- **Returns**: self

### `SPAR.predict(X)`

Make prediction based on recent prices.

- **X**: 1D array of recent prices (at least `field+1` values)
- **Returns**: dict with keys:
  - `pattern_key`: Encoded pattern string
  - `found`: Whether pattern exists in training data
  - `signal`: 'bullish', 'bearish', or 'flat'
  - `hit_ratio`: Majority ratio (e.g., 0.6 = 60% majority)
  - `median_return`: Median return of majority direction
  - `instances`: Total number of historical matches
  - `n_bullish`: Count of bullish outcomes
  - `n_bearish`: Count of bearish outcomes
  - `predicted_values`: List of predicted future values

### `SPAR.get_params()` / `SPAR.set_params(**params)`

Sklearn-compatible parameter getters/setters.

## Examples

### With Yahoo Finance Data

```python
import yfinance as yf
from spar import SPAR

# Download data
data = yf.download('AAPL', period='5y')
prices = data['Close'].values

# Train/test split
train_size = int(len(prices) * 0.7)
train = prices[:train_size]
test = prices[train_size:]

# Fit model
model = SPAR(field=5, min_instances=5)
model.fit(train)

# Evaluate on test set
correct = 0
total = 0

for i in range(5, len(test) - 5):
    recent = prices[train_size + i - 5:train_size + i + 1]
    pred = model.predict(recent)
    
    if pred['signal'] != 'flat':
        total += 1
        future_price = prices[train_size + i + 5]
        start_price = prices[train_size + i]
        
        if pred['signal'] == 'bullish' and future_price > start_price:
            correct += 1
        elif pred['signal'] == 'bearish' and future_price < start_price:
            correct += 1

print(f"Accuracy: {correct/total:.1%}")
```

### Running the Examples

The `examples/` folder contains ready-to-run scripts:

```bash
# Clean synthetic data experiments
python examples/spar_clean_data.py

# Noisy synthetic data experiments  
python examples/spar_noisy_data.py

# Real financial data (requires yfinance)
python examples/spar_financial_data.py
```

## Pattern Space

The number of possible patterns grows exponentially:

| Field | Max Patterns | Notes |
|-------|--------------|-------|
| 3 | 54 | Good for small datasets |
| 5 | 486 | Recommended for most cases |
| 10 | 118,098 | Needs 10,000+ data points |
| 15 | 28M+ | Needs 1M+ data points |

**Rule of thumb:** Use `field` where you have at least 10× more data points than possible patterns.

## Performance on Synthetic Data

| Data Type | Clean | 25% Noise | 75% Noise |
|-----------|-------|-----------|-----------|
| Deterministic | 100% | 85-92% | 65-75% |
| Sine Wave | 94-96% | 70-80% | 50-60% |
| Composite Wave | 68-79% | 55-65% | 45-55% |

## When to Use SPAR

**Good for:**
- Assets with momentum characteristics
- Daily or longer timeframes
- Combining with other signals
- Transparent, interpretable predictions

**Not ideal for:**
- High-frequency/tick data (too noisy)
- Highly efficient markets (EUR/USD)
- When magnitude matters more than direction

## License

MIT License - see [LICENSE](LICENSE) file.

## Contributing

Contributions welcome! Please open an issue or PR on GitHub.

## Citation

If you use SPAR in your research, please cite:

```bibtex
@software{spar2025,
  title = {SPAR: Sequential Pattern Averaging Regressor},
  author = {Sofien Kaabar, CFA},
  year = {2025},
  url = {https://github.com/sofienkaabar/spar-model}
}
```
