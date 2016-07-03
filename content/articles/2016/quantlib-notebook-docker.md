Title: QuantLib Python Notebooks On Docker
Slug: quantlib-python-notebook-docker
Date: 2016-07-02
Category: QuantLib
Tags: python, finance, programming, quantlib
Description: Running QuantLib python notebooks on Docker


The typical way to get QuantLib python running in your computer
is by compiling QuantLib and the SWIG bindings in your computer.
I have heard from some of my blog readers that they run into issues
with getting QuantLib-Python running in their system. Here I will show
how you can easily get started on QuantLib-Python using Docker.

## Docker

[Docker](https://www.docker.com/what-docker) is a platform for containerization of software. 
In other words, Docker lets one to wrap an application in a complete ecosystem needed to run
the application (aka image), such as system libraries and filesystem. This means that irrespective of
what operating system your computer runs, a Docker image will run reliably on the Docker containers. 
Docker containers are very lightweight, and it starts up in a matter of couple of seconds.

## Docker and QuantLib

Every now and then, I would run into conflicts between the development version of QuantLib and 
the release version.  So in order to not have such conflicts, Docker containers are a perfect 
solution. Every image is isolated and it is easy to load a specific version and not have any 
conflicts. In order to keep my Docker images minimal, I use Alpine Linux as a base instead of Ubuntu.

 


### Getting Up and Running

In order to get started on using Docker, you need to first install Docker. The first step
is to get Docker itself. You can get the Docker client by going to 
[getting started page](https://www.docker.com/products/docker).

Once you have done the installation, you can get quantlib-python by doing the following
on a shell:

	docker pull gbalaraman/quantlib-notebook

This is going to pull the quantlib-notebook image from Docker Hub. This process takes a few 
seconds. Think of this as the same as downloading an installer for a software.


Once you have the image downloaded, you can run quantlib-python notebooks by donig the following:

	docker run -d -p 8888:8888 -v <your notebook folder>:/home/notebooks/ --name ql_notebook gbalaraman/quantlib-notebook 

The above command runs the image "gbalaraman/quantlib-notebook" as a daemon (-d) and
will forward the port 8888 in the container to the port 8888 in localhost (-p 8888:8888).
We are calling the container where this image runs as ql_notebook (--name ql_notebook). 
In "-v <your notebook folder>:/home/notebooks/", you should put the folder in you machine
where you want the notebooks to be stored. This takes care of mapping your local folder
to the volume in the container where the notebook will run from.
You can visit [http://localhost:8888](http://localhost:8888) to access the QuntLib python 
notebook environment to play with. This image also has a few other packages included in it, 
such as numpy, pandas, scipy, matplolib and seaborn. This is most of
all you would need to run the notebooks that I publish as part of my QuantLib python tutorial
series. 

When you are done you can stop the Docker container by using the command:

	docker stop ql_notebook

This is equivalent to shutting down the notebook. If you want to start docker again,
this time around you can start it by saying:
	
	docker start ql_notebook


Give this a try and drop a word about your experience with it. You can also take a look at
[Luigi Ballabio's](http://www.implementingquantlib.com/) presentation on 
[QuantLib using Docker](https://www.youtube.com/watch?v=LZbsxs_VGtQ) for another take on 
this subject.













