pipeline {
    agent any

    stages {

        stage('Run Selenium Tests with pytest') {
            steps {
                echo "Running Selenium Tests using pytest"

                // Install Python dependencies
                bat 'pip install -r requirements.txt'

                // Start Flask application in background
                bat 'start /B python app.py'

                // Wait for Flask application to start
                bat 'ping 127.0.0.1 -n 5 > nul'

                // Run Selenium tests
                bat 'python -m pytest -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "Build Docker Image"

                bat "docker build -t mypythonflaskapp:v1 ."
            }
        }

        stage('Docker Login') {
            steps {
                echo "Logging into Docker Hub"

                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-credentials',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    bat 'docker login -u %DOCKER_USERNAME% -p %DOCKER_PASSWORD%'
                }
            }
        }

        stage('Push Docker Image to Docker Hub') {
            steps {
                echo "Push Docker Image to Docker Hub"

                bat "docker tag mypythonflaskapp:v1 141034durga/mypythonflaskapp:v1"

                bat "docker push 141034durga/mypythonflaskapp:v1"
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo "Deploying application to Kubernetes"

                bat 'kubectl apply -f deployment.yaml --validate=false'

                bat 'kubectl apply -f service.yaml'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed. Please check the logs.'
        }
    }
}