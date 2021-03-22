# WS20_ADJE_KNOWROB

Knowlegde processing for robots using ontologies.

Contains:

    - Ontology for modeling Tiago, the used-case scene and the pick up and place task

    - Showcase of how to use the ontology with sample queries

## Getting started
    
    docker-compose -f docker/docker-compose.yaml up

## External dependencies
- [Tiago Tutorials](http://wiki.ros.org/Robots/TIAGo/Tutorials) used for pick-up and place scenario

- [Protege](protege/) for visualising the inferred ontology

## Build dependencies
- [Dockerfile](docker/Dockerfile)

## Run dependencies

- [Tiago pick up demo](http://wiki.ros.org/Robots/TIAGo/Tutorials/MoveIt/Pick_place) from Tiago Tutorials, use [this world](interface/worlds/sim_world.xml) as world file in gazebo

- [Joint states listener service](joint_states_listener/nodes/joint_states_listener.py)

## Authors
- Kayode @Ahadilou

## License
What license is applied to this repository in case of open sourcing.



## Report 

[Project presentation](IKI-Final-Presentation.pdf)
