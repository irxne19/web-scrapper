pipeline {
    agent any
 stages {
  stage('Docker Build and Tag') {
           steps {
              
                sh 'docker build -t web-scrapper:latest .' 
                  sh 'docker tag web-scrapper kristendocker/web-scrapper:latest'               
          }
        }
     
  stage('Publish image to Docker Hub') {
          
            steps {
        withDockerRegistry([ credentialsId: "docker-hub", url: "" ]) {
          sh  'docker push kristendocker/web-scrapper:latest'
        }
                  
          }
        }
  }
}
