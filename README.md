# youtube-music-playlist-sorting-tool
Simple script to sort youtube playlists

# Prepare your project in Google Developers Console 
__1- Go to the Google Developers Console__: Open [Google Developers Console](https://console.cloud.google.com) in your web browser and sign in with your Google account.

__2- Create a New Project__:

Click on the project dropdown next to the Google Cloud Platform logo on the top bar.
Click on "New Project" at the top right of the modal that appears.
Enter a project name and select or create a billing account if prompted. Then, click "Create".

__3- Enable YouTube Data API v3__:

With your new project selected, navigate to the "Library" section from the left sidebar.
Search for "YouTube Data API v3" in the search bar.
Click on the "YouTube Data API v3" result and then click "Enable" to enable the API for your project.

__4- Create Credentials__:

After enabling the API, click on "Create Credentials" in the top bar.
Choose "YouTube Data API v3" from the "Which API are you using?" dropdown.
Choose "Web server (e.g., node.js, Tomcat)" from the "Where will you be calling the API from?" dropdown.
Select "User data" for the type of data you will be accessing.
Click "What credentials do I need?".
If prompted, set up the OAuth consent screen by clicking "Set up consent screen" and fill in the required information. You'll need to provide an Application name, User support email, and Developer contact email at a minimum. Save and continue.
Back in the "Create credentials" flow, you may be asked to provide a name for the OAuth 2.0 client ID and add authorized redirect URIs (for web applications). For desktop or CLI applications, you might not need to specify redirect URIs.
Click "Create OAuth client ID".
Click "Download JSON" on the right side of the client ID you just created. This downloads the client_secrets.json file.

__5- Use the client_secrets.json File__:

Place the downloaded client_secrets.json file in your project directory where your Python script can access it.
Use this file in your code to authenticate using OAuth 2.0.

*Remember to keep your client_secrets.json file secure and do not expose it publicly, as it contains sensitive information about your application.*

__6- Add your user to the test users__
Go to the Google Cloud Console.
Select your project.
Navigate to the "OAuth consent screen" tab under "APIs & Services".
Scroll down to the "Test users" section.
Click on "Add Users" and enter the email addresses of the Google accounts you want to allow as testers.
Save your changes.


__7- Update and run the tool__
You can modify the sorting criteria if you would like.
Insrall the dependencies in requirements.txt and run the tool.

*Some erros may occur because of Youtube API [quotas](https://developers.google.com/youtube/v3/determine_quota_cost)*
