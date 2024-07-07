from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
import logging
from pythonjsonlogger import jsonlogger

# Set logging parameters
log = logging.getLogger()
logHandler = logging.StreamHandler()
formatter = jsonlogger.JsonFormatter()
logHandler.setFormatter(formatter)
log.addHandler(logHandler)
log.setLevel(logging.INFO)


# define playlists and sort criteria
EXECLUDED_PLAYLISTS = []
INCLUDE_PLAYLISTS = []
SORT_CRITERIA = 'videoOwnerChannelTitle' ## Change this to the criteria you want to sort by

# Assuming other parts of your code setup are correct
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

flow = InstalledAppFlow.from_client_secrets_file(
	'client_secrets.json', scopes=scopes)

# Use run_local_server instead of run_console
credentials = flow.run_local_server(port=0)

youtube = build('youtube', 'v3', credentials=credentials)

def get_playlist_items(playlist_id, nextPageToken=None):
	request = youtube.playlistItems().list(
		part="snippet,contentDetails",
		playlistId=playlist_id,
		pageToken=nextPageToken,
		maxResults=50
	)
	response = request.execute()
	items=response['items']
	nextPageToken = response.get('nextPageToken')
	if nextPageToken:
		items.extend(get_playlist_items(playlist_id, nextPageToken))
	return items
		

def edit_playlist(playlist):
	# Get the current items in the playlist
	current_items = get_playlist_items(playlist['id'])
	
	# Sort playlists by sort criteria
	current_items.sort(key=lambda x: x['snippet'][SORT_CRITERIA])
	
	# Update the playlist with the new position
	for i in range(len(current_items)):
		try:
			request = youtube.playlistItems().update(
				part="snippet",
				body={
					'id': current_items[i]['id'],
					'snippet': {
						'playlistId': current_items[i]['snippet']['playlistId'],
						'resourceId':current_items[i]['snippet']['resourceId'],
						'position': i
					}
				}
			)
			response = request.execute()
		except Exception as e:
			log.error(f'Error updating playlist {playlist['snippet']['title']}: {e}')
			return None
	
	return playlist['snippet']['title']


# Retrieve a list of the authenticated user's playlists
nextPageToken = True
playlists = []
while nextPageToken:
	nextPageToken = None
	request = youtube.playlists().list(
		part="snippet,contentDetails",
		mine=True,
		maxResults=50,
		pageToken = nextPageToken
	)
	response = request.execute()
	if response:
		playlists.extend(response['items'])
		nextPageToken = response.get('nextPageToken')
	else:
		break

updated_playlist = []

for playlist in playlists:
	print('Sorting the playlist: ', playlist['snippet']['title'])
	if len(INCLUDE_PLAYLISTS) > 0:
		if playlist['snippet']['title'] not in INCLUDE_PLAYLISTS:
			updated_playlist.append(edit_playlist(playlist))
	elif playlist['snippet']['title'] not in EXECLUDED_PLAYLISTS:
		updated_playlist.append(edit_playlist(playlist))

print("\n\n **************************************************************")
print('Updated playlists:')
for playlist in updated_playlist:
	print('  -', playlist)
print("\n\n **************************************************************")

