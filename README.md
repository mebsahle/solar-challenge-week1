# Solar Data Discovery

A reproducible data‐analysis pipeline and interactive dashboard for the Solar Data Discovery challenge at MoonLight Energy Solutions. We process and explore solar farm measurements from Benin, Sierra Leone, and Togo.

---

## 🚀 Features

- **Data ingestion & cleaning** pipelines in `src/`  
- **Exploratory Data Analysis** notebooks in `notebooks/`  
- **Interactive Streamlit dashboard** in `app/`  
- **Automated testing** with `pytest`  
- **CI/CD** via GitHub Actions

---

## 📋 Prerequisites

- Python 3.10+  
- Git  
- (Optional) Docker & Docker Compose—for containerized development

---

## ⚙️ Setup

1. **Clone repository**  
   ```bash
   git clone https://github.com/your-org/solar-data-discovery.git
   cd solar-data-discovery
   ```

2. **Create & activate virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate    # macOS/Linux
   .\.venv\Scripts\activate     # Windows PowerShell
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Create data folder**

   ```bash
   mkdir data/raw data/clean
   # Place your raw CSVs in data/raw/
   ```

---

## 🛠️ Usage

### 1. Run Data‐Cleaning Scripts

```bash
python src/clean_benin.py
python src/clean_sierra_leone.py
python src/clean_togo.py
# Outputs go to data/clean/<country>_clean.csv
```

### 2. Launch EDA Notebooks

```bash
jupyter lab notebooks/
```

### 3. Start Streamlit Dashboard

```bash
streamlit run app/main.py
```

---

## 📂 Project Structure

```
.
├── .github/
│   └── workflows/ci.yml       # CI pipeline
├── app/                       # Streamlit dashboard
│   └── main.py
├── data/
│   ├── raw/                   # Raw CSVs (git-ignored)
│   └── clean/                 # Cleaned CSVs (git-ignored)
├── notebooks/                 # EDA notebooks
├── src/                       # Data‐processing scripts
│   ├── clean_benin.py
│   ├── clean_sierra_leone.py
│   └── clean_togo.py
├── tests/                     # pytest test suite
├── .gitignore
├── requirements.txt
└── README.md
```

---

## ✅ Testing

Run the full test suite with:

```bash
pytest --maxfail=1 --disable-warnings -q
```

---

## 🤝 Contributing

1. Fork the repo
2. Create a feature branch (`git checkout -b feature/foo`)
3. Commit your changes (`git commit -m "feat: add X"`)
4. Push to your branch (`git push origin feature/foo`)
5. Open a Pull Request against `main`

---

## 🛡️ License
MIT License
----------------
This project is licensed under the MIT License. See [LICENSE](./LICENSE) for details.

