#!groovy
node('master') {
  wrap([$class: 'AnsiColorBuildWrapper', colorMapName: 'xterm']) {
    stage("Checkout") {
      checkout scm
    }

    stage("testing google.com with selenium chrome") {
      sh '''#!/bin/bash -e
        pytest test_google_assert.py
        
      '''
    }

  }
}
