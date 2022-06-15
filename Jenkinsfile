node {
	def app
	def image = 'registry.hub.docker.com/irene19bce2479/web-scrapper'
	def branch = 'main'
		stage('Clone repository') {               
	    	git branch: branch,
	        	credentialsId: 'github',
	        	url: 'https://github.com/irxne19/web-scrapper.git'
	    }
	    stage('Build Image') {
			app = docker.build image
	    }
	    
	    stage('Push') {
	    	docker.withRegistry('https://registry.hub.docker.com', 'irene19bce2479') {            
				app.push("${env.BUILD_NUMBER}")
	        }    
	    }
