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
    }
}
