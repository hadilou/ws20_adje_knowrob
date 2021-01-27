# Protégé Desktop Docker running over X11
###
Desktop version Stanford Ontology IDE
###
    -Protege version 5.5 (from latest GIT)
###
## Components
    -Protege:
        .Protege 5.x
    -Base Components (e.g, Maven,Java.Python,NodeJS, etc.)
    
    -X11 display desktop

## From dockerhub
    docker pull openkbs/protege-docker-x11
## Local image build
    docker build -t protege5_x -f Dockerfile .
## Run (Recommended for easy starting-up)
Once the container is up, this will setup all the neeeded host directory to ensure Protege configurations being persistent for nect run
###
    ./run.sh







