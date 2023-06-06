# UTM_Tracker_Django_Implementation
Introduction:
The UTM Tracker is a Django-based web application that enables tracking and storing UTM parameters (UTM source and UTM medium) when users click on advertisement cards. The UTM parameters are included in the URL of the advertisement page, and upon reaching the advertisement page, the UTM parameters are retrieved and stored in the Django administration database.

Features:

  Clicking on advertisement cards redirects users to the advertisement page with UTM parameters in the URL.

  UTM parameters (UTM source and UTM medium) are automatically extracted from the URL on the advertisement page.

  Extracted UTM parameters are stored in the Django administration database for further analysis and tracking purposes.

Installation:

  1. Clone the UTM Tracker project repository from GitHub.
  2. Create a virtual environment and activate it.
  3. Install the required dependencies using pip install -r requirements.txt.
  4. Configure the Django settings, including database settings, static files, and other necessary configurations.
  5. Run the database migrations using python manage.py migrate.
  6. Start the Django development server with python manage.py runserver.

Usage:

  1. Open the web application in a web browser.
  2. Click on the advertisement cards displayed on the homepage.
  3. You will be redirected to the advertisement page with UTM parameters included in the URL.
  4. Upon reaching the advertisement page, the UTM parameters (UTM source and UTM medium) are automatically retrieved and stored in the Django administration database.
  5. To view and analyze the stored UTM parameters, log in to the Django administration panel and navigate to the UTM Data section.

Configuration:

  1. The UTM Tracker project provides a Django app named "tracker" that handles the tracking functionality.
  2. The necessary URL routes and views are defined in the Django app's "urls.py" and "views.py" files.
  3. The UTM parameters are extracted from the URL using the request.GET.get('utm_source') and request.GET.get('utm_medium') methods in the Django views.
  4. The extracted UTM parameters are stored in the UTMData model in the Django administration database.

Dependencies:

Django: the web framework used for developing the UTM Tracker application.
Other dependencies as specified in the project's requirements.txt file.

Result: 

![Screenshot 2023-06-06 212247](https://github.com/EMMUUU28/UTM_Tracker_Django_Implementation/assets/97393911/65dbdf0f-7294-4f41-9ae4-c88cd3760e25)

Database content

![Screenshot 2023-06-06 212308](https://github.com/EMMUUU28/UTM_Tracker_Django_Implementation/assets/97393911/eb3f9e59-2411-4718-944b-f961897ebb20)

Conclusion:

The UTM Tracker project provides a seamless solution for tracking and storing UTM parameters when users click on advertisement cards. By integrating UTM tracking functionality into the Django-based web application, it allows businesses to gain insights into the effectiveness of their advertising campaigns. The stored UTM parameters can be further analyzed and used for reporting and optimizing marketing strategies.

