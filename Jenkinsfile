pipeline {
    agent any

    stages {
        agent any

        environment {
            VENV_DIR = 'venv'
        }

        stage("Cloning from Github..."){
            steps{
                script {
                    echo 'Cloning from Github...'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/GaoWeiChang/anime_recommender']])
                }
            }
        }

        stage("Creating virtual environment..."){
            steps{
                script {
                    echo 'Creating virtual environment...'
                    sh '''
                    python -m venv ${VENV_DIR}
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }

        stage("DVC pull"){
            steps{
                withCredentials([file(credentialsId:'gcp-key', variable: 'GOOGLE_APPLICATION_CREDENTIALS')]){
                    script{
                        echo 'DVC Pull....'
                        sh '''
                        . ${VENV_DIR}/bin/activate
                        dvc pull
                        '''
                    }
                }
            }
        }

    }
}