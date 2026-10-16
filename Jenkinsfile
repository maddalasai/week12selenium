
pipeline {
    agent any

    stages {
        stage('Install Dependencies and Run Tests') {
            steps {
                bat 'pip install -r requirements.txt'
                bat 'start /B python app.py'
                bat 'ping 127.0.0.1 -n 5 > nul'
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t week12selenium:v1 .'
            }
        }

       
stage('Docker Login') {
    steps {
        withCredentials([usernamePassword(
            credentialsId: 'dockerhub-creds',
            usernameVariable: 'DOCKER_USER',
            passwordVariable: 'DOCKER_PASSWORD'
        )]) {
            powershell '''
                $env:DOCKER_PASSWORD | docker login -u $env:DOCKER_USER --password-stdin
                if ($LASTEXITCODE -ne 0) {
                    exit $LASTEXITCODE
                }
            '''
        }
    }
}


        stage('Push Docker Image') {
            steps {
                bat 'docker tag week12selenium:v1 141034durga/week12selenium:v1'
                bat 'docker push 141034durga/week12selenium:v1'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
                bat 'kubectl rollout status deployment/week12selenium-deployment --timeout=120s'
            }
        }
    }

    post {
        success {
            echo 'Week 12 pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed. Check the stage logs.'
        }
    }
}
