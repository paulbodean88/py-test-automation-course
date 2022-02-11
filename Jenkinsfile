pipeline {
    agent any
    stages {
        stage("build") {
            when {
                expression {
                    BRANCH_NAME == 'main' || CODE_CHANGES == true
                }
            }
            steps {
                sh 'python3 main.py'
            }
        }

        stage('test') {
            when {
                expression {
                    BRANCH_NAME == 'dev'
                }
            }
            steps {
                echo 'building again'
            }
        }

        stage('report') {
            steps {
                echo 'building again'
            }
        }
    }
}