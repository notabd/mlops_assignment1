pipeline {
    agent any

    environment {
        DOCKER_IMAGE = 'flask-app'  // Name of your Docker image
        DOCKERHUB_REPO = 'saimalam843/mlops-flask-app'  // Replace with your Docker Hub repository
        EMAIL_RECIPIENT = 'i211183@nu.edu.pk'  // Replace with the admin's email address
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm  // Checkout the code from your GitHub repository
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    // Build the Docker image from the Dockerfile in your repository
                    sh 'docker build -t $DOCKERHUB_REPO:$BUILD_NUMBER .'
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    // Log in to Docker Hub and push the image
                    docker.withRegistry('https://index.docker.io/v1/', 'dockerhub-creds') {
                        sh 'docker push $DOCKERHUB_REPO:$BUILD_NUMBER'
                    }
                }
            }
        }

        stage('Send Email Notification') {
            steps {
                script {
                    // Send an email notification after successful deployment
                    emailext(
                        subject: "Deployment Successful",
                        body: "The Docker image for your Flask app has been successfully pushed to Docker Hub.",
                        to: "$EMAIL_RECIPIENT"
                    )
                }
            }
        }
    }

    post {
        success {
            echo "Deployment completed successfully!"
        }
        failure {
            echo "Deployment failed!"
        }
    }
}
