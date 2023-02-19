import cgi
import cgitb
import spotipy
import openai
import http.server

cgitb.enable()

form = cgi.FieldStorage()

inputText = form.getvalue("inputText")

user_response = inputText

# process inputText as needed

openai.api_key = "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"

davinci_prompt = str(user_response) + ". Suggest me two funny songs and no other text. \n\n"
print("INFO: Prompt is: " + davinci_prompt)

response = openai.Completion.create(
  model="text-davinci-003",
  prompt= davinci_prompt,
  temperature=0.7,
  max_tokens=150,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=1
)
print(response.choices[0].text)

# Split the two songs
songs = response.choices[0].text.split("2. ")

# Split the song name and artist
song1 = songs[0].split(" by ")
song2 = songs[1].split(" by ")

# Remove the " from the song name
song1[0] = song1[0].replace('"', '')
song2[0] = song2[0].replace('"', '')

# Remove first three characters from first song name
song1[0] = song1[0][3:]

# Print the songs
# print("Song 1: " + song1[0] + " by " + song1[1])
# print("Song 2: " + song2[0] + " by " + song2[1])

# Get the spotify track ID for the song
spotify = spotipy.Spotify(auth='BQDNah94rSTj7W0yNVNXW2K_Q3ZSKjRR_lfsF3JkQZjL2k0a4J3ixFoPtRh2lrJ4bLgoD6UyAP4oRLCt6E1xUqtPUfHgpwBuk5OCNZYcjZf3-yVG-42Aksx6JF-doXiKg_aQZ91tTREBA7ltMbJIi25TRu7tGIAU96UjGjMWnaNWAUw1fUnCAhiEXCf21l7rG6s')

# Song 1
results = spotify.search(q='artist:' + song1[1] + ' track:' + song1[0], type='track')
trackId1 = results['tracks']['items'][0]['id']

# Song 2
results2 = spotify.search(q='artist:' + song2[1] + ' track:' + song2[0], type='track')
trackId2 = results2['tracks']['items'][0]['id']

# Print the spotify URL for the song
url1 = "https://open.spotify.com/embed/track/" + trackId1 + "?utm_source=generator"
url2 = "https://open.spotify.com/embed/track/" + trackId2 + "?utm_source=generator"

print('<script>')
print('document.getElementById("frame1").src = "{}";'.format(url1))
print('document.getElementById("frame2").src = "{}";'.format(url2))
print('</script>')

