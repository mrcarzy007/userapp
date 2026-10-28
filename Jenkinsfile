pipeline {
    agent any

    tools {
        jdk "jdk21"
    }

    environment {
        DOCKER_HUB_USER   = "devopsaditya123"
        IMAGE_NAME        = "${DOCKER_HUB_USER}/userapp"
        IMAGE_TAG         = "${env.GIT_COMMIT.take(8)}"
        SONAR_PROJECT_KEY = "python-app"   
    }

    stages {
        stage("1 Checkout") {
            steps {
                echo "Code Checkout from branch : ${env.BRANCH_NAME}"
                checkout scm
            }
        }

        stage("2. SonarQube Analysis") {
            steps {
                script {
                    // Jenkins Tools se scanner ka path le rahe hain
                    def scannerHome = tool 'SonarQube Scanner'
                    
                    withSonarQubeEnv("SonarQube") {
                        sh """
                            ${scannerHome}/bin/sonar-scanner \
                            -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                            -Dsonar.sources=. \
                            -Dsonar.projectName=python-app 
                        """
                    }
                }
            }
        }

        stage("3 Quality Gate") {
            steps {
                echo "Waiting for SonarQube Quality Check"
                timeout(time: 5, unit: 'MINUTES') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }

        stage("4 Docker build") {
            steps {
                echo "Building image: ${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} . "
            }
        }

        stage("5 Docker push image in docker hub") {
            steps {
                withCredentials([usernamePassword(credentialsId: "docker-cred", usernameVariable: "USER", passwordVariable: "PASS")]) {
                    sh 'echo $PASS | docker login -u $USER --password-stdin'
                    sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }

     stage("6 Deploy to DEV") {
            when {
                anyOf {
                    branch 'develop'
                    branch 'feature/*'
                }
            }
            steps {
                echo "Deploying ${IMAGE_TAG} to DEV environment..."
                dir('k8s/overlays/dev') {
                    sh "kustomize edit set image ${IMAGE_NAME}=${IMAGE_NAME}:${IMAGE_TAG}"
                }
                sh "kubectl apply -k k8s/overlays/dev"
            }
        }

        stage("7 Deploy to PROD") {
            when {
                anyOf {
                    branch 'main'
                    branch 'master'
                }
            }
            steps {
                input message: 'Do you want to deploy to PRODUCTION?', ok: 'Deploy to Prod'
                
                echo "Deploying ${IMAGE_TAG} to PROD environment..."
                dir('k8s/overlays/prod') {
                    sh "kustomize edit set image ${IMAGE_NAME}=${IMAGE_NAME}:${IMAGE_TAG}"
                }
                sh "kubectl apply -k k8s/overlays/prod"
            }
        }
  
    }

    post {
        success {
            echo " ✅ Pipeline Success......"
        }
        failure {
            echo "❌ Pipeline Failed......."
        }
        always {
            cleanWs()
        }
    }
}