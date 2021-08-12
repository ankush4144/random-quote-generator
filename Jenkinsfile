def quote = ''

pipeline {
    agent {
        label 'CENTOS_SLAVE'
    }
    
    stages {
        stage('Fetch Quote') {
            steps {
                echo 'Running Python Script..'
                sh 'python3 --version'
                sh 'python3 forismatic.py'
                script { quote = sh 'cat quote.txt' } 
                script {
                    quote = sh(returnStdout: true, script: 'echo `cat quote.txt`').trim()
                }
            }
        }
        stage('Create Artifact') {
            steps {
                echo 'Creating Artifacts..'
                archiveArtifacts artifacts: 'quote.txt'
            }
        }
        stage('Create Quote Webpage') {
            steps {
                build job: 'Quote_WebPage_Creator', parameters: [ string(name: 'Quote', value:"${quote}") ]
            }
        }
        stage('Pull HTML Artifact') {
            steps {
                copyArtifacts filter: 'quote.html', fingerprintArtifacts: true, projectName: 'Quote_WebPage_Creator', selector: lastSuccessful()
                archiveArtifacts artifacts: 'quote.html'
            }
        }
        stage('Deploy Webpage') {
            steps {
                sh 'sudo mkdir -p /usr/share/tomcat/webapps/quote'
                sh 'sudo cp quote.html /usr/share/tomcat/webapps/quote'
            }
        }
    }
}
