pipeline {
    agent any

     tools {
        jdk "jdk21"
        sonarscanner "SonarQube Scanner"
     }
     environment {
        DOCKER_HUB_USER = "devopsaditya123"
        IMAGE_NAME = "${DOCKER_HUB_USER}/userapp"
        IMAGE_TAG  =  "${env.GIT_COMMIT.take(8)}"
        SONAR_PROJECT_KEY = "python-app"   
        
        }
    stages {
        stage("1 Checkout"){
            steps {
                echo "Code Checkout from branch : ${env.BRANCH_NAME}"
                checkout scm
            }
        }
        stage("2 SonarQube Analysis"){
            steps {
                withSonarQubeEnv("SonarQube"){
                 sh """
                 sonar-scanner \
                 -Dsonar.projectKey=${SONAR_PROJECT_KEY} \
                 -Dsonar.sources=. \
                 -Dsonar.projectName=python-app 
                 """
                }
                
            }
        }

        stage("3 Quality Gate"){
            steps{
                echo "Waiting for SonarQube Quality Check"
                timeout(time: 5 , unit: "minutes"){
                    waitForQualityGate abortPipeline : true
                }
            }
        }

        stage("4 Docker build"){
            steps{
                echo "Building image: ${IMAGE_NAME}:${IMAGE_TAG}"
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} . "
            }
        }
        stage("5 Docker push image in docker hub"){
            steps {
                withCredentials([usernamePassword(credentialsId: "docker-cred", usernameVariable: "USER", passwordVariable: "PASS")]){
                      sh  "echo $PASS | docker login -u $USER --password-stdin"
                      sh "docker push ${IMAGE_NAME}:${IMAGE_TAG}"
                }
            }
        }
    }
    post {
    success {
        echo " ✅ CI  Pipeline Success......"
    }
    failure {
         echo "❌ CI pipeline Failed......."
    }
    always {
        cleanWs()
    }
}
}

