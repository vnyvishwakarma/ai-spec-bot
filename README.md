# ai-spec-bot

**ai-spec-bot** is a Python-powered utility that scans Java Spring Boot projects in local GitHub repositories and uses **Gemini 1.5 Pro** (Google Generative AI) to generate **natural language test scenarios**. It's ideal for teams looking to automate BDD/test documentation based on annotated controller logic.

---

## ✨ Features

- Powered by **Gemini AI (1.5 Pro)** from Google.
- Scans multiple cloned GitHub repositories inside a single directory.
- Identifies Java classes with `@RestController` or `@Controller` annotations.
- Outputs clear and simple **test scenarios** in English to `test.spec`.
- Easily extendable to support Gherkin, JSON, or Markdown outputs.

---

## ⚙️ Prerequisites

- Python 3.7 or above
- A Google Generative AI API Key (Gemini 1.5 Pro)
- Install the required SDK:

```bash
pip install google-generativeai


