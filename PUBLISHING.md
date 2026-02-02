# How to Publish SPAR on GitHub

## Step 1: Create a GitHub Account

If you don't have one, go to https://github.com and sign up.

---

## Step 2: Create a New Repository

1. Log in to GitHub
2. Click the **+** icon in the top right corner
3. Select **"New repository"**
4. Fill in the details:
   - **Repository name**: `spar-model`
   - **Description**: `Sequential Pattern Averaging Regressor - A non-parametric time series forecasting model`
   - **Visibility**: Select **Public**
   - **DO NOT** check "Add a README file" (we already have one)
   - **DO NOT** check "Add .gitignore" (we already have one)
   - **DO NOT** check "Choose a license" (we already have one)
5. Click **"Create repository"**

---

## Step 3: Upload Files

### Option A: Using GitHub Web Interface (Easiest)

1. On your new empty repository page, you'll see "Quick setup"
2. Click **"uploading an existing file"** link
3. Drag and drop ALL files and folders from the `spar-model` folder:
   ```
   spar-model/
   ├── spar/
   │   └── __init__.py
   ├── examples/
   │   ├── spar_clean_data.py
   │   ├── spar_noisy_data.py
   │   └── spar_financial_data.py
   ├── README.md
   ├── LICENSE
   ├── setup.py
   ├── pyproject.toml
   └── .gitignore
   ```
4. Add commit message: `Initial release v0.1.0`
5. Click **"Commit changes"**

### Option B: Using Git Command Line

Open Terminal/Command Prompt and run:

```bash
# 1. Navigate to the spar-model folder
cd path/to/spar-model

# 2. Initialize git repository
git init

# 3. Add all files
git add .

# 4. Create first commit
git commit -m "Initial release v0.1.0"

# 5. Rename branch to main (if needed)
git branch -M main

# 6. Add your GitHub repository as remote
#    Replace YOUR_USERNAME with your actual GitHub username
git remote add origin https://github.com/YOUR_USERNAME/spar-model.git

# 7. Push to GitHub
git push -u origin main
```

---

## Step 4: Before Uploading - Update Placeholders

Open these files and replace the placeholders:

| Find | Replace with |
|------|--------------|
| `YOUR_USERNAME` | Your GitHub username |
| `YOUR_NAME` | Your name |
| `your.email@example.com` | Your email |

Files to update:
- `README.md` (multiple places)
- `setup.py`
- `pyproject.toml`
- `LICENSE`

---

## Step 5: Create a Release

1. Go to your repository on GitHub
2. Click **"Releases"** in the right sidebar
3. Click **"Create a new release"**
4. Fill in:
   - **Tag version**: `v0.1.0`
   - **Release title**: `v0.1.0 - Initial Release`
   - **Description**:
     ```
     Initial release of SPAR - Sequential Pattern Averaging Regressor
     
     Features:
     - Sklearn-style API (fit/predict)
     - Majority vote signal generation
     - Median path forecasting
     - Optional EMA smoothing
     - Structural or linear forecasts
     - Numba acceleration (optional)
     
     Examples included:
     - Clean synthetic data experiments
     - Noisy synthetic data experiments
     - Real financial data with yfinance
     ```
5. Click **"Publish release"**

---

## Step 6: (Optional) Publish to PyPI

This allows anyone to install with `pip install spar-model`.

### First-time Setup

1. Create account at https://pypi.org
2. Create account at https://test.pypi.org (for testing)
3. Install build tools:
   ```bash
   pip install build twine
   ```

### Build and Upload

```bash
# Navigate to spar-model folder
cd path/to/spar-model

# Build the package
python -m build

# Test upload to TestPyPI first
twine upload --repository testpypi dist/*

# If successful, upload to real PyPI
twine upload dist/*
```

You'll be prompted for your PyPI username and password.

---

## Done!

Your model is now published! Share the link:

```
https://github.com/YOUR_USERNAME/spar-model
```

### Installation Methods

People can now install SPAR via:

```bash
# From GitHub
pip install git+https://github.com/YOUR_USERNAME/spar-model.git

# From PyPI (after Step 6)
pip install spar-model
```

---

## File Structure Summary

```
spar-model/
├── spar/
│   └── __init__.py          # Main SPAR class
├── examples/
│   ├── spar_clean_data.py   # Synthetic data experiments
│   ├── spar_noisy_data.py   # Noisy data experiments
│   └── spar_financial_data.py # Real market data
├── README.md                 # Documentation
├── LICENSE                   # MIT License
├── setup.py                  # pip install support
├── pyproject.toml            # Modern Python packaging
├── .gitignore                # Git ignore rules
└── PUBLISHING.md             # This file (delete before publishing)
```

**Note:** You can delete `PUBLISHING.md` before uploading - it's just for your reference.
