# Week 3: Debugging & Logging in Python

## Overview

This week's project is a **simple e-commerce checkout simulation** that demonstrates:

1. **Intentional Bug Introduction** – A deliberate error in the discount calculation to practice debugging.
2. **Using Python's Built-in Debugger (`pdb`)** – Step through code interactively to identify issues.
3. **Logging** – Record cart totals, discounts applied, and errors for traceability.

---

## Files

| File            | Description                                      |
|-----------------|--------------------------------------------------|
| `app.py`        | Main checkout simulation with bug and logging    |
| `checkout.log`  | Log file generated during execution              |

---

## Features

### 1. Product Catalog

A dictionary of items with prices in **Nigerian Naira (₦)**:

```python
items = {
    "Wireless Noise-Cancelling Headphones": 250000.00,
    "Bluetooth Earbuds": 150000.00,
    "Portable Charger": 80000.00,
    # ... more items
}
```

### 2. Discount Codes

| Code         | Type       | Value          |
|--------------|------------|----------------|
| `TENPERCENT` | Percentage | 10% off        |
| `FIVEOFF`    | Fixed      | ₦5,000 off     |

### 3. Intentional Bug 🐛

The percentage discount calculation contains a deliberate bug:

```python
# Bug: multiplying by 100 twice — wrong discount calculation
discount_amount = total_naira * (val * 100)
```

**Expected:** `total_naira * val` (e.g., ₦660,000 × 0.10 = ₦66,000)  
**Actual (buggy):** `total_naira * (val * 100)` (e.g., ₦660,000 × 10 = ₦6,600,000!)

This causes the discount to be **1000% of the subtotal** instead of 10%.

### 4. Logging

Logs are written to both the console and `checkout.log`:

- **DEBUG**: Subtotals, line items, discount calculations
- **INFO**: Cart subtotal, final total, discount applied
- **ERROR**: Unknown items, invalid discount codes

---

## How to Run

```bash
cd "Week 3"
python app.py
```

### Expected Output

```
Summary:
Subtotal: ₦660,000.00
Discount: ₦6,600,000.00   <-- Bug! Should be ₦66,000.00
Total: ₦0.00              <-- Clamped to zero
```

---

## Debugging with pdb

### Interactive Debugging

Add a breakpoint in the code:

```python
import pdb; pdb.set_trace()
```

Or run the script with:

```bash
python -m pdb app.py
```

### Common pdb Commands

| Command | Description                          |
|---------|--------------------------------------|
| `n`     | Next line (step over)                |
| `s`     | Step into function                   |
| `c`     | Continue execution                   |
| `p var` | Print variable value                 |
| `l`     | List source code around current line |
| `q`     | Quit debugger                        |

### Automated pdb Session

The script includes an `automated_pdb_run()` function that runs a non-interactive pdb session with predefined commands to demonstrate stepping through the checkout flow.

---

## Fixing the Bug

To fix the discount calculation, change:

```python
# Buggy
discount_amount = total_naira * (val * 100)
```

To:

```python
# Fixed
discount_amount = total_naira * val
```

---

## Learning Objectives

- [x] Understand how to use `pdb` for debugging Python code
- [x] Learn to add logging statements at key points in a program
- [x] Practice identifying and fixing bugs through debugging
- [x] Understand the difference between DEBUG, INFO, and ERROR log levels

---

## References

- [Python pdb Documentation](https://docs.python.org/3/library/pdb.html)
- [Python logging Documentation](https://docs.python.org/3/library/logging.html)
