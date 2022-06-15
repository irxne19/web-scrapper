pipeline {
    agent any
 stages {
  stage('Docker Build and Tag') {
           steps {
              
                sh 'docker build -t web-scrapper:latest .' 
                  sh 'docker tag web-scrapper irene19bce2479/web_scrapper_main:latest'               
          }
        }
     
  stage('Publish image to Docker Hub') {
          
            steps {
        withDockerRegistry([ credentialsId: "irene19bce2479", url: "" ]) {
          sh  'docker push irene19bce2479/web_scrapper_main:latest'
        }
                  
          }
        }
  }
}
