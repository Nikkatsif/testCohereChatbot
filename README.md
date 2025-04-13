# testCohereChatbot
An automated test suit for the Cohere chat bot, using Pytest and Playwright.
It tests a simple response, as well as the identification of the topic of an uploaded .pdf file.

# How to use
1. Install the dependencies from the requirements.txt
2. Add your Cohere credentials to the config.json file
3. Run the tests

# Add more chatbot pages
In order to run the same tests on different chatbots, do the following:
1. Add the name of the chatbot to the PAGES_LIST of the config.py
2. Using the same name, add the corresponding credentials to PAGE_CREDENTIALS dictionary of the config.py
3. Using the same name, create a new sub-folder in the pages folder
4. Within this subfolder, implement the DashboardInterface and LandingPageInterface classes, that are in the dashboard_iterface.py and landing_page_interface.py files, respectively

If implemented correctly running the tests will now include the new chatbot page.
