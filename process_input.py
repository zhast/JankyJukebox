
import spotipy
import openai
import http.server

def run(prompt):

  user_response = prompt
  # process prompt example "inputText=my%20dog%20died" into "my dog died"
  user_response = user_response.replace("inputText=", "")
  user_response = user_response.replace("%20", " ")


  openai.api_key = "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"

  davinci_prompt = str(user_response) + ". Suggest me two funny songs and no other text in the format 1. \"name\" by artist 2. \"name\" by artist \n\n"
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
  song_name_and_artist = response.choices[0].text

  # Split the two songs and remove the " from the song name
  songs = song_name_and_artist.split("2. ")

  song1 = songs[0].split(" by ")
  song2 = songs[1].split(" by ")

  # Remove 1. from song name
  song1[0] = song1[0].replace("1. ", "")

  # Strip anything that's not a letter or a space
  try:
    song1[0] = ''.join(e for e in song1[0] if e.isalnum() or e == ' ')
    song2[0] = ''.join(e for e in song2[0] if e.isalnum() or e == ' ')
  except:
    print("ERROR: Song name or artist name is empty")
  
  try:
    song1[1] = ''.join(e for e in song1[1] if e.isalnum() or e == ' ')
    song2[1] = ''.join(e for e in song2[1] if e.isalnum() or e == ' ')
  except:
    print("ERROR: Song name or artist name is empty")





  # Get the spotify track ID for the song
  spotify = spotipy.Spotify(auth='BQA4Lc-eHINWa9RDp18OMYCGPOWOZQD5rWre2Qg617Pt_XFj9aP_xceTbyzcgPxOb3J8rXcLMEkUacQeWafxvfaqTOGOnMfOia5Md7LPIvDggox4pU8kf1OxPmKQI30IKGaFYRdo6Yi1gDThLH9AZFr3bns2RkqXmYSN_J_jHC1SCnwvAdPZLlEAUkwJW4X2wbY')

  url1 = ""
  url2 = ""

  print(song1)
  print(song2)

  # Song 1
  # Search spotify for the song ID
  results = spotify.search(q='artist:' + song1[1] + ' track:' + song1[0], type='track')
  try:
    trackId1 = results['tracks']['items'][0]['id']
    url1 = "https://open.spotify.com/embed/track/" + trackId1 + "?utm_source=generator"
  except: 
    print("ERROR: No track ID found for song 1")
  #Song 2
  results = spotify.search(q='artist:' + song2[1] + ' track:' + song2[0], type='track')
  try:
    trackId2 = results['tracks']['items'][0]['id']
    url2 = "https://open.spotify.com/embed/track/" + trackId2 + "?utm_source=generator"
  except:
    print("ERROR: No track ID found for song 2")


  print("Here!")
  #Generate the spotify URL for the song
  
  
  return (url1, url2)
  
  # print('<script>')
  # print('document.getElementById("frame1").src = "{}";'.format(url1))
  # print('document.getElementById("frame2").src = "{}";'.format(url2))
  # print('</script>')

