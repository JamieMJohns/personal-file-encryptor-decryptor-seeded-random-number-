# personal-file-encryptor-decryptor-with-seeded-random-number-
test python program i made which encrypts encoding of files in a specified folder (output file types are ".jim" files) after user specifies seed (number) for random number generator ... the ".jim" files can then be decrypted with same program (and converted back to original file type) if user inputs correct random number seed that was used to encrypt files.  
  
When I have time, I will update the repository with more indepth description but for; refer to comments in .py code
for understand how program works.  
  
<repository to be updated soon>  
    
  -> also working on making developing as standalone program as have done with previous python codes  
 Modules required (for running in python);  
 ->numpy  
 ->string  
 ->os  
Current bug in program (to  be fixed soon)!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  
  To be fixed [easily fixed in next release]:     
===>For example files;  
-->file.txt  
-->file_2.png  
-->file.3.exe  
-->file.4.1.pdf [more than one full stop in full name]   
-->file.5.2.6.jpg [more than one full stop in full name]  
-->fileLast.mp3  
===>Encrypted files look like:  
-->file.jim  
-->file_2.jim  
-->file.3.jim  
-->file.4.jim [missing rest of filename after second full stop (of previous name)]  
-->file.5.jim [missing rest of filename after second full stop (of previous name)]  
-->fileLast.jim  
===>Decrypted files look like:  
-->file.txt (works like original file [before encryption])  
-->file_2.png (works like original file [before encryption])  
-->file.3.exe (works like original file [before encryption])  
-->file.4.0 [missing file type and rest of original file name (potentially corrupted)]  
-->file.5.0 [missing file type and rest of original file name (potentially corrupted)]  
-->fileLast.mp3 (works like original file [before encryption])  
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!  

Also to be added in update:  
pseudo-random number generation without numpy or other module (compiling to exe [i.e using pyinstaller])  
results in large file (>120mb) because of dependencies for numpy module;  
I have worked on code (and tested) to generate pseudo-random numbers and will use it  
to replace numpy module in future release to be uploaded soon.  


- jamie johns  
