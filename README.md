# TrelloE2E
End-to-end tests for Trello

# Requirements

* Python 3.10.X
* pip and setuptools
* [venv](<https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/>) (recommended)

# Instalation

1. Download or clone the repository 
2. Open a terminal
3. Go to the project root directory.
4. Create a virtual environment: `py -m venv venv`
5. Activate the virtual environment executing the following script: `.\venv\bin\activate`
6. Execute the following command to download the necessary libraries:  `pip install -r requirements.txt`

# Test Execution

1. Open a terminal
2. From the project root directory run: `python -m pytest --html=report.html`

# Results

To check the report, open the 'report.html' file once the execution has finished.

# Improvement ideas:

Because project was time sensitive I didnt have time to include this for now.

* Replace time.sleep with appropriate web driver method 
* Replace pytest-bdd @scenario with @scenarious 
* Move pytest fixtures into conftest.py 
* Clean up requirenments.txt 
* Describe all elements using Page object model
