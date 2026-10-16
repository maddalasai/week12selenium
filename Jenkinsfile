
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
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    bat 'echo %DOCKER_PASSWORD%| docker login --username %DOCKER_USERNAME% --password-stdin'
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
