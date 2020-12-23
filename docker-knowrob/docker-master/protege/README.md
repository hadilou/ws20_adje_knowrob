# Protégé Desktop Docker running over X11
###
Desktop version Stanford Ontology IDE
###
    -Protege version 5.5 (from latest GIT)
###
## Components
    -Protege:
        .Protege .x
    -Base Components (e.g, Maven,Java.Python,NodeJS, etc.)
        
        . See [openkbs/jdk-mvn-py3](https://github.com/DrSnowbird/jdk-mvn-py3/blob/master/README.md#Components)
    -X11 display desktop

## From dockerhub
    docker pull openkbs/protege-docker-x11
## Local image build
    docker build -t protege5_x -f Dockerfile .
## Run (Recommended for easy starting-up)
This will setup all the neeeded host directory to ensure Protege configurations being persistent for nect run
###
    ./run.sh







