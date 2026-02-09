# DevOps CI Demo (Jenkins + TypeScript + Python)

This repository demonstrates a simple multi-language CI/CD pipeline using Jenkins.

## Features
- TypeScript module with Jest tests
- Python automation script with pytest tests
- Jenkins pipeline that:
  - installs dependencies
  - runs linting and tests
  - generates a build report artifact (`build_report.json`)
  - archives artifacts for traceability

## Pipeline Stages
1. Checkout
2. TypeScript: install, lint, test
3. Python: virtualenv, install, test
4. Generate build artifact
5. Archive artifact