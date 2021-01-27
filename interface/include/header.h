#include <locale.h>
#include <string>
#include <fstream>
#include <iostream>
#include <vector>
#include <boost/algorithm/string.hpp>


#include <map>


#include <stdlib.h>
#include <ros/ros.h>

#define PL_SAFE_ARG_MACROS
#include <SWI-cpp.h>
#include <SWI-Prolog.h>
#include <stdio.h>
#include <dlfcn.h>
#include <string>
#include <memory>

#include <iostream>


using namespace std;

class Knowledge {
   private:

       static string prologPath;
       vector<string> objType;
       vector<string> object;

   public:

       Knowledge()
       {
           objType.clear();
           object.clear();
       }
       
       bool setKnowledge();

       void prologEnv();
       
 
       inline void setObjecType(vector<string> contRgn){objType = contRgn;}
       inline void setObject(vector<string> obj){object = obj;}
       static void setPath(string path){prologPath = path;}

       static string getPath(){return prologPath;}
       inline vector<string> getObjecType(){return objType;}
       inline vector<string> getObject(){return object;}

       struct OWL{
           string name;
           string type;
           string color;
       };

       
   };