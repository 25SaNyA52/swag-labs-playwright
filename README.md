# Swag Labs — Playwright Automation Project

End-to-end test suite for [saucedemo.com](https://www.saucedemo.com) using the Page Object Model pattern.

## Tech Stack

- **Python** 3.10+
- **Playwright** (sync API)
- **pytest** + pytest-playwright
- **pytest-html** for HTML reports
- **python-dotenv** for environment config

## Folder Structure

```
swag-labs-playwright/
│
├── pages/
│   ├── __init__.py
│   ├── base_page.py
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── product_detail_page.py
│   ├── cart_page.py
│   ├── checkout_info_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
│
├── tests/
│   ├── __init__.py
│   ├── conftest.py
│   ├── test_login.py
│   ├── test_inventory.py
│   ├── test_product_detail.py
│   ├── test_cart.py
│   └── test_checkout.py
│
├── utils/
│   ├── __init__.py
│   ├── config.py
│   └── helpers.py
│
├── test_data/
│   └── users.py
│
├── .env                ← NOT committed (create from .env.example)
├── .env.example        ← committed as a template
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/<your-username>/swag-labs-playwright.git
cd swag-labs-playwright
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv

# Mac/Linux
source venv/bin/activate

# Windows
venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
playwright install chromium
```

### 4. Configure environment variables
```bash
cp .env.example .env
# Edit .env if needed (defaults work for saucedemo.com)
```

## Running Tests

### Run all 20 tests
```bash
pytest
```

### Run a single test file with verbose output
```bash
pytest tests/test_login.py -v
```

### Run with a visible browser (headed mode)
Set `HEADLESS=false` in your `.env`, then:
```bash
pytest
```

### Run a specific test by name
```bash
pytest -k "test_successful_login"
```

## HTML Report

After running, open `reports/report.html` in your browser to view the full test report.

## Test Coverage

| Module | Test IDs | Count |
|---|---|---|
| Login / Auth | TC_LOGIN_01 – TC_LOGIN_06 | 6 |
| Inventory | TC_INV_01 – TC_INV_05 | 5 |
| Product Detail | TC_PDP_01 | 1 |
| Cart | TC_CART_01 – TC_CART_02 | 2 |
| Checkout | TC_CHK_01 – TC_CHK_05, TC_E2E_01 | 6 |
| **Total** | | **20** |
