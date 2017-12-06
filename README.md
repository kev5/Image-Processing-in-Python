# Image-Processing-in-Python
Finding duplicate images efficiently in a directory with a large collection of images.

## Description
In the image folders named zero, one, two, three, there is exactly one object in each image, photographed over a perfectly white background image. Any non-white pixel is part of the object.

Also, all the images are RBG with values for each color ranging from 0 to 255 (hence the arrays can be stored using uint8 data types).

The objects are rigid and two-dimensional. The objects are all photographed from the same distance, so the same object appears the same size in all photographs it appears in. However, the object can be rotated by multiples of 90 degrees in the image, and can appear anywhere within the image. All objects are completely contained within the image. One other complication: due to camera inconsistencies, some of the objects appear as their mirror image.

Our program should find all the PNG files in the current directory: these are all files with the extension png. Every PNG file has exactly one number in the filename, and these numbers are guaranteed to be unique among all image files in the directory.

The program should create a file to record the results of the image categorization process, and print out the SHA256 message digest for this file.

The file name is specified on the command line, like this:

```python duplicatefinder.py name_of_file_to_create```

## Output Specification
The resultant file should be formatted such that:
 - Each line contains the filenames of identical objects
 - The filenames in the line are sorted in increasing numerical order (of the number in the filename)
 - The lines in the file are sorted in increasing numerical order based on the first filename in each line.
 - The new line character must be \n and NOT \r\n

For example-
```
rasberry0.png cher2.png grap5.png grape6.png
ban1.png rasber8.png bana9.png
grape3.png
pear4.png rasber7.png```

Note: The SHA256 digest-
Using the facilities of the hashlib module, we print out the SHA256 digest for the file created, so that the resultant text file does not have a long list of filenames.

In Unix-based systems, the SHA256 digest (and others) can be calculated using-

```shasum -a 256 answers.txt```
