from owlready2 import *

#to load ref ontologies
onto_path.append("../owl")
#load tiago onto
tiago_onto = get_ontology("../owl/SOMA.owl")
tiago_onto =tiago_onto.load()


print(tiago_onto.imported_ontologies)