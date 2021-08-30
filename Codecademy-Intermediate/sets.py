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
  
  song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
               'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
               'Stomping Cue': ['country', 'fiddle', 'party'],
               'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
               'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
               'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
               'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
               'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': [
    'pop', 'warm', 'happy', 'electronic', 'synth']}

# Checkpoint 1
tag_diff = set(user_liked_song['Back To Art']) - \
    set(user_disliked_song['Retro Words'])

# Checkpoint 2
recommended_songs = {}
for key, val in song_data.items():
    for tag in val:
        if tag in tag_diff:
            if key not in user_liked_song and key not in user_disliked_song:
                recommended_songs[key] = val

print(recommended_songs)


user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                       'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                       'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                       'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

# Write your code below!
user_tags = set()
for song in user_song_history:
  user_tags.update(set(user_song_history[song]))

friend_tags = set()
for song in friend_song_history:
  friend_tags.update(set(friend_song_history[song]))

unique_tags = user_tags ^ friend_tags


music_tags = {'pop', 'warm', 'happy', 'electronic', 'synth', 'dance', 'upbeat'}

# Write your code below!
my_tags = frozenset(['pop', 'electronic', 'relaxing', 'slow', 'synth'])
frozen_tag_union = my_tags | music_tags
regular_tag_intersect = music_tags & my_tags

frozen_tag_difference = my_tags - music_tags

regular_tag_sd = music_tags ^ my_tags
