
## Docker Files for Knowrob in Kinetic

    cd kinetic-swi

    docker build -t kinetic-swi -f Dockerfile .

    cd ../kinetic-knowrob-daemon

    docker build -t kinetic-knowrob -f Dockerfile .

It is possible to install Kinetic branch of Knowrob with these docker images but not all functionalities will probably be available. 


