pyuClassify
------------

Python Wrapper for accessing uClassify services.

Currently supports following operation:

1. Creates Classifier
2. Classify
3. Classify Keywords
4. getInformation
5. addClass
6. removeClass
7. Train
8. Untrain
9. removeClassifier 

Installation:
-------------

It is very easy to install pyuClassify.

    	(pip install | easy_install) uclassify

... or in the traditional way:

    	$ git clone git://github.com/psibi/pyuClassify.git
    	$ cd uclassify
    	$ sudo python setup.py install


Usage:
------

An example of how to use the API.

    	from uclassify import uclassify

    	a = uclassify()
    	a.setWriteApiKey(WRITE_API_KEY)
    	a.setReadApiKey(READ_API_KEY)
	
    	a.create("ManorWoman") #Creates Classifier named "ManorWoman"

    	a.addClass(["man","woman"],"ManorWoman") #Adds two class named "man" and "woman" to the classifier "ManorWoman"

    	a.train(["Her hair is so nice!!","I wish I had more cosmetic.","I like those ice creams."],"woman","ManorWoman")
    	#The above function trains three sentences for the class "woman" on the classifier "ManorWoman"
    	
    	d = a.classify(["sample text1","sample text2"],"ManorWoman")
    	#Now the list d will contain the following value [('sample text1', u'0', [(u'man', u'0.5'), (u'woman', u'0.5')]), ('sample text2', u'0', [(u'man', u'0.5'), (u'woman', u'0.5')])]


License:
--------
GNU General Public License v3 (GPLv3)

Bug Report:
-----------
Issue it here: https://github.com/psibi/pyuClassify/issues


