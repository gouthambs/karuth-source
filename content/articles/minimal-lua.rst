Minimal Lua C++ Example
#######################

:date: 2014-07-17
:tags: lua, programming, C++
:description: Very basic introduction to Lua C++ API
:keywords: lua, programming, c++, embed

If you want to extend and customize the capabilities of a C++ application 
without requiring a full recompilation, then using a embedded scripting language 
is the way to go. Lua is one such embeddable scripting language, and is very popular
among game developers. The main advantage of Lua, in my opinion, is that the core API
is very minimal, has very small memory footprint. The availability of LuaJIT makes
it a very performant alternative as well.


Example Code
------------

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
  	const char lua_script[] = "print('Hello World!')";
  	int load_stat = luaL_loadbuffer(L,lua_script,strlen(lua_script),lua_script);
  	lua_pcall(L, 0, 0, 0);
  
  	// cleanup
  	lua_close(L);	
  	return 0;
  }  
  
Code Explained
--------------

Here the ``lua_open`` and ``luaL_openlibs`` are initialization step in order to prepare 
the ``lua_State * L``. We store the script that we need to execute in the variable ``lua_script``.
The ``luaL_loadbuffer`` is used to load the script. The loaded script can be executed by 
calling ``lua_pcall(L, 0, 0, 0)``. The arguments passed to ``lua_pcall`` are the ``lua_State`` pointer,
number of arguments to the script (which is none here), number of values returned (which is none here). The
last argument to ``lua_pcall`` is the error handler which we will not discuss here.

This needs to be compiled using a C++ compiler and linked to Lua library. When you run the 
executable, you should see ``Hello World!`` printed on the screen.

Conclusion
----------

We looked at a rather simple introductory example of ``lua`` interpreter embeded into ``C++`` code.
