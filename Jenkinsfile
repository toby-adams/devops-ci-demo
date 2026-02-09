pipeline {
  agent any

  options {
    timestamps()
  }

  environment {
    CI = "true"
    BUILD_REPORT_PATH = "build_report.json"
    VENV_DIR = "${WORKSPACE}/.venv"
  }

  stages {
    stage("Checkout") {
      steps {
        checkout scm
      }
    }

    stage("TypeScript: install + lint + test") {
      steps {
        dir("typescript") {
          sh '''
            npm ci
            npm run lint
            npm test
          '''
        }
      }
    }

    stage("Python: venv + test") {
      steps {
        dir("python") {
          sh '''
            python3 -m venv "$VENV_DIR"
            . "$VENV_DIR/bin/activate"
            pip install --upgrade pip
            pip install -r requirements.txt
            pytest -q
          '''
        }
      }
    }

    stage("Generate build artifact (Python automation)") {
      steps {
        dir("python") {
          sh '''
            . "$VENV_DIR/bin/activate"
            export TS_TESTS_PASSED=2
            export PY_TESTS_PASSED=1
            export BUILD_REPORT_PATH="${WORKSPACE}/${BUILD_REPORT_PATH}"
            python -m src.reportgen
          '''
        }
      }
    }

    stage("Archive artifact") {
      steps {
        archiveArtifacts artifacts: "build_report.json", fingerprint: true
      }
    }
  }
}