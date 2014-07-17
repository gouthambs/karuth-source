Minimal Lua C++ Example
#######################

:date: 2014-07-17
:tags: lua, programming, C++
:description: Very basic introduction to Lua C++ API


If you want to extend and customize the capabilities of a C++ application 
without requiring a full recompilation, then using a embedded scripting language 
is the way to go. Lua is one such embeddable scripting language, and is very popular
among game developers. The main advantage of Lua, in my opinion, is that the core API
is very minimal, has very small memory footprint. The availability of LuaJIT makes
it a very performant alternative as well.


Minimal Example
---------------

Here is a minimal Lua(V5.1) - C++  example to get one started.

.. code :: c++


  // luaexample.cpp
  extern "C" {
    #include "lua.h"
    #include "lualib.h"
    #include "lauxlib.h"
  }
  #include <string.h>
  
  int main(int argc, char* argv[])
  {
  	// initialization
  	lua_State * L = lua_open();
  	luaL_openlibs(L);
  
  	// execute script
  	lua_settop(L,0);
  	const char lua_script[] = "print('Hello World!')";
  	int load_stat = luaL_loadbuffer(L,lua_script,strlen(lua_script),lua_script);
  	lua_pcall(L, 0, 0, 0);
  
  	// cleanup
  	lua_close(L);	
  	return 0;
  }  
  


This needs to be compiled using a C++ compiler and linked to Lua library. When you run the 
executable, you should see `Hello World!` printed on the screen.
