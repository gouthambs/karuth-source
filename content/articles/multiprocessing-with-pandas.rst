Multi-Processing With Pandas
############################

:date: 2014-11-19
:tags: python, programming, pandas
:description: Motivation for using multi-processing with pandas
:slug: distributed-processing-pandas

If you have used ``pandas``, you must be familiar with the awesome functionality and tools that 
it brings to data processing. I have used ``pandas`` as a tool to read data files and transform
them into various summaries of interest. My usual process pipeline would start with 
a text file with data in a CSV format. I would read data into a ``pandas`` ``DataFrame`` 
and run various transformations of interest. 

Recently I stumbled into a problem with this approach. My file was big, in the 100's of MBs. I was 
running a 32-bit version of python, and I started getting ``MemoryError``. This happens because
``pandas`` and ``numpy`` would need to allocate contiguous memory blocks, and 32-bit system
would have a cap at 2GB. Additionally processing a huge file took some time (more than my impatience
could tolerate). The approach I took to solve this problem is:

- Read the large input file in smaller chunks so it wouldn't run into ``MemoryError``
- Use multi-processing to process the input file in parallel to speed up processing

Sample Code
-----------

``Pandas`` ``read_table`` method can take ``chunksize`` as an argument and return an ``iterator`` 
while reading a file. This means that you can process individual ``DataFrames`` consisting of 
``chunksize`` rows at a time. You can then put the individual results together.

.. code:: python

	import pandas as pd
	
	LARGE_FILE = "D:\\my_large_file.txt"
	CHUNKSIZE = 100000 # processing 100,000 rows at a time
	
	def process_frame(df):
		# process data frame
		return len(df)
	
	if __name__ == '__main__':
		reader = pd.read_table(LARGE_FILE, chunksize=CHUNKSIZE)
		
		result = 0
		for df in reader:
			# process each data frame
			result += process_frame(df)
		
		print "There are %d rows of data"%(result)
		
The code chunk above shows you how to read file in smaller chunks and process
each chunk at a time. You can also add a ``multiprocessing`` twist to it
to get performance boost. Here is a ``multiprocessing`` version of the same 
snippet from above.

.. code:: python
	
	import pandas as pd
	import multiprocessing as mp
	
	LARGE_FILE = "D:\\my_large_file.txt"
	CHUNKSIZE = 100000 # processing 100,000 rows at a time
	
	def process_frame(df):
		# process data frame
		return len(df)
	
	if __name__ == '__main__':
		reader = pd.read_table(LARGE_FILE, chunksize=CHUNKSIZE)
		pool = mp.Pool(4) # use 4 processes
		
		funclist = []
		for df in reader:
			# process each data frame
			f = pool.apply_async(process_frame,[df])
		
		result = 0
		for f in funclist:
			result += f.get(timeout=10) # timeout in 10 seconds
			
		print "There are %d rows of data"%(result)

		
The code snippet above should be fairly self explanatory. The idea here is to 
*asynchronously* process chunk of data by pushing it into a multiprocessing pool queue. 
Each process in pool will work on the task, and return the result.
