# Automated Testing — DemoQA Form

![QA](https://img.shields.io/badge/Testing-Automation-blue)
![Tool](https://img.shields.io/badge/Selenium-Python-green)
![Test Type](https://img.shields.io/badge/Testing-Functional-lightgrey)
![Python application](https://github.com/celiapaivab/qa-formulario-selenium-demoqa/actions/workflows/python-app.yml/badge.svg?branch=main)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Profile-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/celia-bruno)


---

## 📌 Project Overview

This project was developed as part of my **QA learning journey**, focusing on **automated testing** for the registration form on [DemoQA](https://demoqa.com/automation-practice-form).

The purpose of this project is to practice the implementation of automation tools and good testing practices. Since DemoQA is a demo site for training purposes, no real bugs were found or reported — the focus was on simulating realistic scenarios and validating both positive and negative flows.

---

## 🎯 Project Goals

- Automate the form filling and submission process.
- Validate required fields and data formats (email, phone).
- Capture screenshots for result analysis.
- Run tests automatically with GitHub Actions (CI/CD).

---

## 🔧 Technologies and Tools

- **Python**
- **Pytest**
- **Selenium WebDriver**
- **GitHub Actions** (CI/CD)

---

## ▶️ How to Run

1. Clone this repository:
  ```bash
  git clone https://github.com/celiapaivab/qa-formulario-selenium-demoqa
  cd qa-formulario-selenium-demoqa
  ```
  
2. Create and activate a virtual environment:
  ```bash  
  python -m venv venv  
  source venv/bin/activate  (Linux/macOS)  
  venv\Scripts\activate  (Windows)
  ```
  
3. Install the dependencies:
  ```bash
  pip install -r requirements.txt
  ```
  
4. Run the tests with Pytest:
  ```bash
  pytest -s tests/
  ```
- Screenshots will be saved automatically in the screenshots/ folder.

---

## 🧾 Results

- Testes automatizados de fluxo positivo e negativo implementados e executados com sucesso.  
- Validação correta da exibição do modal de confirmação apenas em envios válidos.  
- Captura de evidências visuais por meio de screenshots em casos de sucesso e falha.  
- Pipeline de integração contínua configurado no GitHub Actions para execução automática.

---

## 📚 What I Learned

- Applied the **Page Object Model (POM)** pattern to organize the test code.
- Developed functional automated tests using Selenium and Pytest.
- Implemented screenshot capture and storage for evidence.
- Configured continuous integration with GitHub Actions for automated test execution.

---

## 💡 Future Improvements

- Add tests to validate additional form fields.
- Include detailed HTML reports after test execution.
- Expand the test suite to cover other forms and functionalities on the DemoQA site.
- Automate execution on different browsers and screen resolutions for cross-browser testing.

---

## 📂 Project Files

- `tests/` — Automated test scripts in Python  
- `pages/` — Page Object Model implementation for the form page  
- `screenshots/` — Screenshots generated during test execution  
- `requirements.txt` — Python dependencies list  
- `.github/workflows/python-app.yml` — GitHub Actions pipeline configuration

---
