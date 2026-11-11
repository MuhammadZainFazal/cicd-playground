// Same pipeline as ci.yml, expressed in Jenkins "declarative pipeline" syntax.
pipeline {
    agent { docker { image 'python:3.12-slim' } }

    options {
        timeout(time: 15, unit: 'MINUTES')
        disableConcurrentBuilds()
    }

    environment {
        HOME = "${WORKSPACE}"   // pip needs a writable home inside the container
    }

    stages {
        stage('Install') {
            steps { sh 'pip install --user -r requirements-dev.txt' }
        }
        stage('Lint') {
            steps { sh '~/.local/bin/ruff check .' }
        }
        stage('Test') {
            steps { sh '~/.local/bin/pytest --cov=app --junitxml=report.xml' }
            post { always { junit 'report.xml' } }
        }
        stage('Deploy') {
            when { branch 'main' }
            steps { echo 'Deploy step goes here' }
        }
    }

    post {
        failure { echo 'Build failed - notify the team here (email/Slack)' }
    }
}
