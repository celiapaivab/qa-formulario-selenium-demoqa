# Automação de Testes – Formulário DemoQA

![QA](https://img.shields.io/badge/Testes-Automação-blue)
![Ferramenta](https://img.shields.io/badge/Selenium-Python-green)
![Tipo de Teste](https://img.shields.io/badge/Testes-Funcional-lightgrey)
![Python application](https://github.com/celiapaivab/qa-formulario-selenium-demoqa/actions/workflows/python-app.yml/badge.svg?branch=main)


Este projeto foi desenvolvido como parte do meu aprendizado em QA, focando na automação de testes para o formulário de cadastro do site [DemoQA](https://demoqa.com/automation-practice-form).

---

## 📌 Objetivos do Projeto

- Automatizar o preenchimento e submissão do formulário  
- Validar campos obrigatórios e formatos de dados (e-mail, telefone)  
- Implementar captura de screenshots para análise dos resultados

---

## 🔧 Tecnologias utilizadas

- Python
- Pytest
- Selenium WebDriver
- GitHub Actions

---

## 📋 Atividades Realizadas

- Implementação do padrão Page Object Model (POM) para organizar o código  
- Desenvolvimento de testes positivos e negativos para os campos do formulário  
- Integração de captura de screenshots em casos de sucesso e falha
- Verificação de exibição do modal de sucesso apenas em envios válidos  
- Automação integrada ao GitHub Actions

---

## ✅ Testes Automatizados

Este projeto cobre testes de:

- ✅ **Preenchimento completo e válido do formulário** (positivo)
- ❌ **Tentativas de envio com dados inválidos ou ausentes** (negativo), como:
  - E-mails inválidos ou vazios
  - Nome ausente
  - Número de celular inválido

Todos os testes validam se o modal de confirmação **só é exibido em envios válidos**.

---

## 🚀 Como usar

1. Clone este repositório:
  ```bash
  `git clone https://github.com/seu-usuario/seu-repositorio.git`  
  `cd seu-repositorio`
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
