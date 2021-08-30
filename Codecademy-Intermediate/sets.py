allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie', 'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal', 'jazz',
                'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic', 'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb',
                                   'warm', 'due', 'writer', 'happy', 'horrible', 'electric', 'mushroom', 'shed']}

# Write your code below!
tag_set = set(song_data_users['Retro Words'])
bad_tags = []

for tag in tag_set:
  if not tag in allowed_tags:
    bad_tags.append(tag)

for tag in bad_tags:
  tag_set.remove(tag)

song_data_users['Retro Words'] = tag_set


song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'],
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

# Write your code below!
new_song_data = {}

for key, val in song_data.items():
  new_song_data[key] = set(song_data[key]) | set(user_tag_data[key])
