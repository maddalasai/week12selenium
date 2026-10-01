pipeline { 
    agent any 

    stages { 

        stage('Build Docker Image') { 
            steps { 
                echo "Build Docker Image" 
                bat "docker build -t mypythonflaskapp:v1 ." 
            } 
        } 

        stage('Docker Login') { 
            steps { 
                bat 'docker login -u 141034durga -p Srujana123' 
            } 
        } 

        stage('push Docker Image to Docker Hub') { 
            steps { 
                echo "push Docker Image to Docker Hub" 

                bat "docker tag mypythonflaskapp:v1 141034durga/mypythonflaskapp:v1"                

                bat "docker push 141034durga/mypythonflaskapp:v1" 
            } 
        } 

        stage('Deploy to Kubernetes') {  
            steps {  
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