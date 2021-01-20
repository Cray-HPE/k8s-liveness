// Jenkinsfile for k8s-liveness Python package
// Copyright 2020-2021 Hewlett Packard Enterprise Development LP
 
@Library('dst-shared@master') _

pipeline {
    agent {
        kubernetes {
            label "cray-k8s-liveness"
            containerTemplate {
                name "cms-k8s-livenesss-cont"
                image "dtr.dev.cray.com/dst/cray-alpine3_build_environment:latest"
                ttyEnabled true
                command "cat"
            }
        }
    }

    // Configuration options applicable to the entire job
    options {
        // This build should not take long, fail the build if it appears stuck
        timeout(time: 10, unit: 'MINUTES')

        // Don't fill up the build server with unnecessary cruft
        buildDiscarder(logRotator(numToKeepStr: '5'))

        // Add timestamps and color to console output, cuz pretty
        timestamps()
    }

    environment {
        // Set environment variables here
        GIT_TAG = sh(returnStdout: true, script: "git rev-parse --short HEAD").trim()
    }

    stages {
        stage('Push to github') {
            when { allOf {
                expression { BRANCH_NAME ==~ /(bugfix\/.*|feature\/.*|hotfix\/.*|master|release\/.*)/ }
            }}
            steps {
                container('cms-k8s-livenesss-cont') {
                    sh """
                        apk add --no-cache bash curl jq git openssl
                    """
                    script {
                        pushToGithub(
                            githubRepo: "Cray-HPE/k8s-liveness",
                            pemSecretId: "githubapp-stash-sync",
                            githubAppId: "91129",
                            githubAppInstallationId: "13313749"
                        )
                    }
                }
            }
        }

        stage('Build Package') {
            steps {
                container('cms-k8s-livenesss-cont') {
                    sh """
                        apk add --no-cache --virtual .build-deps g++ python3-dev libffi-dev openssl-dev py3-pip bash curl
                        apk add --no-cache --update python3 && \
                        pip3 install --upgrade pip setuptools
                        pip3 install wheel
                        python3 setup.py sdist bdist_wheel
                    """             
                }
            }
        }

        stage('Unit Tests') {
            steps {
                container('cms-k8s-livenesss-cont') {
                    sh """
                       pip3 install -r requirements.txt
                       pip3 install -r requirements-test.txt
                       python3 setup.py install
                       python3 tests/test_liveness.py
                       pycodestyle --config=.pycodestyle ./src/liveness || true
                       pylint ./src/liveness || true
                    """
                }
            }
        }

        stage('PUBLISH') {
            when { branch 'master'}
            steps {
                container('cms-k8s-livenesss-cont') {
                    // Need to install ssh and rsync commands and get private key in place for transferPkgs
                    // sshpass is for the transferPkgs function
                    sh """
                        apk add --no-cache openssh-client rsync sshpass
                    """
                    transferPkgs(directory: "liveness", artifactName: "dist/*.tar.gz")
                    transferPkgs(directory: "liveness", artifactName: "dist/*.whl")
                }
            }
        }
    }

    post('Post-build steps') {
        failure {
            emailext (
                subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
                <p>Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
                recipientProviders: [[$class: 'CulpritsRecipientProvider'], [$class: 'RequesterRecipientProvider']]
            )
        }

        success {
            archiveArtifacts artifacts: 'dist/*', fingerprint: true
        }
    }
}
