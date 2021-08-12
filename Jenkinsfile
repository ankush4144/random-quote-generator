def quote = ''

pipeline {
    agent {
        label 'CENTOS_SLAVE'
    }
    
    stages {
        stage('Run') {
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
                script {
                    archiveArtifacts artifacts: 'quote.txt'
                }
            }
        }
        stage('Create Webpage') {
            steps {
                build job: 'Quote_WebPage_Creator', parameters: [ string(name: 'Quote', value:"${quote}") ]
            }
        }
    }
}
