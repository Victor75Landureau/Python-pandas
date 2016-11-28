README:
csv file link = http://data.dft.gov.uk/road-accidents-safety-data/Stats19-Data1979-2004.zip

Conclusion
So, what did we accomplish? Well, we took a very large file that Excel could not open and utilized Pandas to-

Open the file.
Perform SQL-like queries against the data.
Create a new XLSX file with a subset of the original data.
Keep in mind that even though this file is nearly 800MB, in the age of big data, it’s still quite small. What if you wanted to open a 4GB file? Even if you have 8GB or more of RAM, that might still not be possible since much of your RAM is reserved for the OS and other system processes. In fact, my laptop froze a few times when first reading in the 800MB file. If I opened a 4GB file, it would have a heart attack.

So how do we proceed?

The trick is not to open the whole file in one go. That’s what we’ll look at in the next blog post. Until then, analyze your own data. Leave questions/comments below. Grab the code from the repo.
