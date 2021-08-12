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
                archiveArtifacts artifacts: 'quote.txt'
            }
        }
        stage('Create Webpage') {
            steps {
                build job: 'Quote_WebPage_Creator', parameters: [ string(name: 'Quote', value:"${quote}") ]
            }
        }
        stage('Pull Artifact') {
            steps {
                copyArtifacts filter: 'quote.html', fingerprintArtifacts: true, projectName: 'Quote_WebPage_Creator', lastSuccessful: true
                archiveArtifacts artifacts: 'quote.html'
            }
        }
    }
}
