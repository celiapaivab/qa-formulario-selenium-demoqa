# Automação de Testes – Formulário DemoQA

![QA](https://img.shields.io/badge/Testes-Automação-blue)
![Ferramenta](https://img.shields.io/badge/Selenium-Python-green)
![Tipo de Teste](https://img.shields.io/badge/Testes-Funcional-lightgrey)
![Python application](https://github.com/celiapaivab/qa-formulario-selenium-demoqa/actions/workflows/python-app.yml/badge.svg?branch=main)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-blue?style=flat&logo=linkedin)](https://www.linkedin.com/in/celia-bruno)


---

## 📌 Sobre o Projeto
Este projeto foi desenvolvido como parte do meu aprendizado em QA, focando na automação de testes para o formulário de cadastro do site [DemoQA](https://demoqa.com/automation-practice-form).

---

## 🎯 Objetivo do Projeto

- Automatizar o preenchimento e submissão do formulário  
- Validar campos obrigatórios e formatos de dados (e-mail, telefone)  
- Implementar captura de screenshots para análise dos resultados

---

## 🔧 Tecnologias e Ferramentas

- Python
- Pytest
- Selenium WebDriver
- GitHub Actions (para CI/CD)

---

## ▶️ Como Executar

1. Clone este repositório:
  ```bash
  git clone https://github.com/celiapaivab/qa-formulario-selenium-demoqa
  cd qa-formulario-selenium-demoqa
  ```
  
2. Crie e ative o ambiente virtual (opcional, mas recomendado):
  ```bash  
  python -m venv venv  
  source venv/bin/activate  (Linux/macOS)  
  venv\Scripts\activate  (Windows)
  ```
  
3. Instale as dependências:
  ```bash
  pip install -r requirements.txt
  ```
  
4. Execute os testes com pytest:
  ```bash
  pytest -s tests/
  ```
- As screenshots serão salvas na pasta `screenshots/` (criada automaticamente).

---

## 🧾 Resultado

- Testes automatizados de fluxo positivo e negativo implementados e executados com sucesso.  
- Validação correta da exibição do modal de confirmação apenas em envios válidos.  
- Captura de evidências visuais por meio de screenshots em casos de sucesso e falha.  
- Pipeline de integração contínua configurado no GitHub Actions para execução automática.

---

## 📚 Aprendizados

- Aplicação do padrão **Page Object Model (POM)** para organização do código.  
- Desenvolvimento de testes funcionais automatizados utilizando Selenium e Pytest.  
- Implementação de captura e armazenamento de screenshots para evidências.  
- Configuração de integração contínua via GitHub Actions para testes automatizados.

---

## 💡 Melhorias Futuras

- Adicionar testes para validação de campos adicionais do formulário.  
- Incluir relatórios HTML detalhados após execução dos testes.  
- Expandir a suíte para testes de outros formulários e funcionalidades do site DemoQA.  
- Automatizar o tratamento de diferentes navegadores e resoluções para testes cross-browser.

---

## 📂 Arquivos do Projeto

- `tests/` – Scripts de teste automatizados em Python  
- `pages/` – Implementação do Page Object Model para a página do formulário  
- `screenshots/` – Capturas de tela geradas durante a execução dos testes  
- `requirements.txt` – Lista de dependências Python  
- `.github/workflows/python-app.yml` – Configuração da pipeline de GitHub Actions

---

## 🇺🇸 Project Summary

This project was developed as part of my QA learning journey, focusing on test automation for the registration form on the DemoQA website.  

The main goal is to ensure the correct functionality of the form, including mandatory field validations and submission flows. Automated tests cover both positive and negative scenarios, capturing screenshots as evidence.  

The project also includes a CI pipeline configured with GitHub Actions to run tests automatically on push events.
