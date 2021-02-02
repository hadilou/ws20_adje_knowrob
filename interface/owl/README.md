# Ontology

The ontology is inspired from the core ontologies used in KnowRob: SOMA,DUL,SRDL. Those are added as references in the folder.

The reason is that working on constructing an ontology definition for modelling objects and tasks is time consuming and require full knowledge of the objects, robots,tasks and interactions.

Based on definitions made in _SOMA_, we can describe tasks and objects. For example _hasBodyPart_ is an object property introduced in _SOMA_ and Tiago can use it to define its own parts. That is the approach followed in the development of the ontology. Also, in case we want to work on Knowrob later when it's stable, it will make it easier.

## Ontology for Tiago

Class Diagram:

![Tiago.owl](imgs/class_diagram_Tiago.png)

To see data properties, instances of classes, object properties and more, you can load the file _Tiago.owl_ in Protege. 



## Activity Modelling

Apart from types used in modelling _Tiago_ below elements from SOMA will can used for Grasping task:

- Physical Task::Task   A task in which a PhysicalAgent affects some physical object.

    - Actuating 
        - Delivering
        - Lowering
        - Positioning
    - Assuming Pose
        - Assuming Arm Pose
        - Setting Gripper
    -Manipulation
        - End Effect Positioning
            - Reaching
            - Retracting
        - Grasping
    - Navigating
        - Distancing
        - MovingTo 
    - Perceiving
        - Checking Object Presence
        - Placing (different from positioning where precise location is known)

- Action Execution Plan::Plan idea: steps in workflows assert that they are defined by action execution plans. Links role and parameter fillers to e.g. slots in a data structure.

## Ontology Modelling Environments

[Owlready2](https://owlready2.readthedocs.io/en/latest/index.html) for code-first approach (Python3)

[Protege](../../protege) for ontology-first approach

Using _Owlready2_ , only modifications made on the ontology in Python are saved.

## Spatial Reasoning 

Spatial reasoning provide the robot the ability to know the semantics locations of objects around him.

top: (_Obj1 top Obj2_ ) if object1 is on top of object 2
inside: (_Obj1 in Obj2_) if object1 is inside object 2
leftTo : (_Obj1 left Obj2_)
rightTO : (_Obj1 right Obj2_)

## Reachability  

_(is_reachable(robot,Object) or object.reacheble_by(robot))_

In manipulation task, it is common to estimate the affordance of a task using probabilistic models or ontology with rules.
The reachability concept has been added, given a grasp task _T(robot,object,goal)_ , it evaluates to _True_ if the robot can reach
the goal object. 

## Queries

Queries can be made either using _Owlready2_ or _SparkQL_ and _RDFlib_
In this package, all queries are made with _Owlready2_ 

