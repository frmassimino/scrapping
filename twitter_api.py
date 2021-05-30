import twitter

consumer_key = ""
consumer_key_secret = ""
access_token = ""
access_token_secret = ""

api = twitter.Api(consumer_key=consumer_key, consumer_secret=consumer_key_secret, access_token_key=access_token, access_token_secret=access_token_secret)

print(api.VerifyCredentials())

followers = api.GetFollowers()
friends = api.GetFriends()
#print(followers)
#print(friends)

status_var = "Nuevo mensaje"
post_update = api.PostUpdates(status=status_var)

#length_status = twitter.twitter_utils.calc_expected_status_length(status=status_var)

#new_message= api.PostDirectMessage(screen_name='', text='Prueba api post')
#print(new_message)

#api.PostDirectMessage(user, text)
#api.GetUser(user)
#api.GetReplies()
#api.GetUserTimeline(user)
#api.GetHomeTimeline()
#api.GetStatus(status_id)
#api.GetStatuses(status_ids)
#api.DestroyStatus(status_id)
#api.GetFriends(user)
#api.GetFollowers()
#api.GetFeatured()
#api.GetDirectMessages()
#api.GetSentDirectMessages()
#api.PostDirectMessage(user, text)
#api.DestroyDirectMessage(message_id)
#api.DestroyFriendship(user)
#api.CreateFriendship(user)
#api.LookupFriendship(user)
#api.VerifyCredentials()