
#include <iostream>
#include <header.h>
#include <ros/ros.h>

#include <SWI-Prolog.h>
#include <SWI-cpp.h>

string Knowledge::prologPath="";

void Knowledge::prologEnv()
{
    string loadFile;
    loadFile = "consult('";
    loadFile += prologPath;
    loadFile += "')";

    const char * argv [] = {" -q "};

    // Opening the Prolog environment.
    cout<<"Prolog file has been loaded from the directory: "<<prologPath<<endl;
    PlEngine e(1, (char **) argv);

    // Loading the Prolog file.
    PlCall(loadFile.c_str());
}

int main()
{
    Knowledge owlKnowledge;
    owlKnowledge.setPath("../prolog/knowledge.pl");
    std::cout << owlKnowledge.getPath();
    owlKnowledge.prologEnv();
}
