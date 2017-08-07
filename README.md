# Ullman-Foundations-of-CS

I came across Jeff Ullman's page and happened to find this interesting book - Foundations of CS, available in pdf chapterwise.
So, my immediate thought was to write an automated script that downloads and saves the pdfs in the local directory of my system, with filename as the chapter no.

##### Source : http://i.stanford.edu/~ullman/focs.html

# Requirements

* Python 2.7.x
* pip install requests

# Approach

The URL for each pdf had a common structure : http://i.stanford.edu/~ullman/focs/ch[X].pdf.  
Where [X] is the chapter no.

* All the chapters are 2 digits ranging from 01 - 14. 
* [ X ] is to be made sure that it is injected in the URL as 01-09 and not as 1-9 othwerwise it will be a 404 error.
* N no of processes are created to download and save the pdfs on the system. N being the total no. of chapters (14)
* Each process then invokes ```chapterStringManipulate(chapter)``` which expects an integer and checks for the necessary string manipulation of the chapters between 1 - 9 to be converted into string as 01 - 09.  
* ```chapterStringManipulate()``` then calls ```download(chapter)``` which expects a string and then ```requests``` for the URL and writes the downloaded data into path entered in ```savePath```  
  
  
# Run

```
python ullman.py
```
