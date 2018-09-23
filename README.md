# Google-Search-knowledge-carousal-parser
A simple script that extracts the list of items in the carousal returned by Google search's knowledge graph.

For many search terms that can return a list of answers, for instance "the cast of suits", Google's knowledge graph provides a carousal showing a list of top results.

This script extracts these results as a list of strings. 

### parameters

The first parameter should be the number of results required.

The second parameter onwards should be the keywords for the search query. Any amount of keywords can be used.

### instructions

1. install the selenium web driver for chrome

```python
pip install selenium chromedriver_installer
```

2. download the chrome web driver from https://sites.google.com/a/chromium.org/chromedriver/downloads

3. clone the repo, and change the path_to_chromedriver variable in script.py to the directory you extracted the chrome web driver to, and the save_path variable to the same directory as the repo.

4. run the script.
```python
python script.py 20 cast of suits
```

### Purpose behind the code

Eventhough the Google Knowledge Graph API can provide a list of results similar to the information displayed in the carousal, unfortunately it returns many unrelated items as well. This can be solved by specifying the "type" argument, this requires the caller to know in advance the type of result it expects. For instance to get a list of presidents of the USA, the type should be specified as "person". In addition only a small variety of types are available, which means that categories such as "dog breeds" are not covered. This script was designed to address this issue.

The reason the Selenium web driver is used instead of a library such as urllib is because frustatingly, the web page returned to a simple html library such as urllib by Google does not include the carousal.


