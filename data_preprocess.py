# Shala Chen
import pandas as pd
import numpy as np
import csv
import sys
from datetime import datetime
import json
import simplejson
csv.field_size_limit(sys.maxsize)

# load dta from csv file and open new files to write them
count = 0
newData = open('newData.csv', 'wb')
writeNewData = csv.writer(newData) 
writeNewData.writerow(["created_days","compound","neg","neu","pos",
						"postLength","favorite_count","coordinates",
						"user_descrip_length","followers_count","url",
						"verified","friends_count","location",
						"hashtags","place","Check_URL"])

classes = open('classes.csv', 'wb')
writeClass = csv.writer(classes)
writeClass.writerow(["classes"])

with open('twitter_csv.csv', '"rU"') as oldDataFile:
	oldData = csv.reader(oldDataFile)
	next(oldData, None)
	for row in oldData:

		# exclude those don't have brand or rts_likes
		if len(row[1]) == 6 and row[7] != "" :
			newFeature = []

			# add Created_at data into features as days
			createDate = row[3].replace("/", " ")
			createDate = datetime.strptime(createDate, '%m %d %y %H:%M')
			dateDifference = datetime.now() - createDate
			days = dateDifference.days
			newFeature.append(days)

			# add sentiment data into features 
			if row[5] == '':
				sentiment = [0,0,0,0]
			else:
				data = json.loads(row[5])
				sentiment = [data["compound"],data["neg"],data["neu"],data["pos"]]
			newFeature.extend(sentiment)

			# add post length into features
			postLength = len(row[6])
			newFeature.append(postLength)

			# add classes information into classes
			writeClass.writerow([row[7]])

			# add extra data from Json_data to features
			if row[8] =='':
				# if there's no json_data information, put 0s instead
				newFeature.extend([0,0,0,0,0,0,0,0,0,0,0,0])
			else:
				extraData = row[8].replace('"',"'").replace('\\', '').replace("'}",'"}').replace("'withheld_in_countries':",'"withheld_in_countries":').replace("'visit_site'",'"visit_site"').replace("'call_to_actions'",'"call_to_actions"').replace("'embeddable'",'"embeddable"').replace("'title'",'"title"').replace("'source_user'",'"source_user"').replace("'monetizable'",'"monetizable"').replace("'additional_media_info'",'"additional_media_info"').replace("'profile_text_color'",'"profile_text_color"').replace("'profile_sidebar_fill_color'",'"profile_sidebar_fill_color"').replace("'in_reply_to_status_id_str'",'"in_reply_to_status_id_str"').replace("'result_type'",'"result_type"').replace("'iso_language_code'",'"iso_language_code"').replace("'metadata'",'"metadata"').replace("'quoted_status'",'"quoted_status"').replace("'time_zone'",'"time_zone"').replace("'profile_background_color'",'"profile_background_color"').replace("'profile_sidebar_border_color'",'"profile_sidebar_border_color"').replace("'default_profile_image'",'"default_profile_image"').replace("'following'",'"following"').replace("'profile_background_image_url_https'",'"profile_background_image_url_https"').replace("'profile_link_color'",'"profile_link_color"').replace("'is_translation_enabled'",'"is_translation_enabled"').replace("'notifications'",'"notifications"').replace("'contributors'",'"contributors"').replace("'in_reply_to_user_id_str'",'"in_reply_to_user_id_str"').replace("'retweeted'",'"retweeted"').replace("'in_reply_to_screen_name'",'"in_reply_to_screen_name"').replace("'truncated'",'"truncated"').replace("'in_reply_to_user_id'",'"in_reply_to_user_id"').replace("'symbols'",'"symbols"').replace("'user_mentions'",'"user_mentions"').replace("'in_reply_to_status_id'",'"in_reply_to_status_id"').replace("'profile_background_image_url'",'"profile_background_image_url"').replace("'is_translator'",'"is_translator"').replace("'protected'",'"protected"').replace("'follow_request_sent'",'"follow_request_sent"').replace("'utc_offset'",'"utc_offset"').replace("'profile_use_background_image'",'"profile_use_background_image"').replace("'profile_image_url_https'",'"profile_image_url_https"').replace("'profile_background_tile'",'"profile_background_tile"').replace("'lang'",'"lang"').replace("'statuses_count'",'"statuses_count"').replace("'geo_enabled'",'"geo_enabled"').replace("'profile_banner_url'",'"profile_banner_url"').replace("'listed_count'",'"listed_count"').replace("'favourites_count'",'"favourites_count"').replace("'contributors_enabled'",'"contributors_enabled"').replace("'default_profile'",'"default_profile"').replace("'large':",'"large":').replace("'small'",'"small"').replace("'thumb'",'"thumb"').replace("'resize'",'"resize"').replace("'h'",'"h"').replace("'w'",'"w"').replace("'medium'",'"medium"').replace("'sizes'",'"sizes"').replace("'extended_entities'",'"extended_entities"').replace("'favorited'",'"favorited"').replace("'bitrate'",'"bitrate"').replace("'content_type'",'"content_type"').replace("'variants'",'"variants"').replace("'aspect_ratio'",'"aspect_ratio"').replace("'duration_millis'",'"duration_millis"').replace("'video_info'",'"video_info"').replace("'contained_within'",'"contained_within"').replace("'followers'",'"followers"').replace("'scopes'",'"scopes"').replace("'is_quote_status'",'"is_quote_status"').replace("'has_extended_profile'",'"has_extended_profile"').replace("'translator_type'",'"translator_type"').replace("'has_extended_profile'",'"has_extended_profile"').replace("'possibly_sensitive'",'"possibly_sensitive"').replace("'possibly_sensitive_appealable'",'"possibly_sensitive_appealable"').replace("'source_user_id'",'"source_user_id"').replace("'source_status_id'",'"source_status_id"').replace("'source_status_id_str'",'"source_status_id_str"').replace("'source_user_id_str'",'"source_user_id_str"').replace("'country_code'",'"country_code"').replace("'country'",'"country"').replace("'bounding_box'",'"bounding_box"').replace("'full_name'",'"full_name"').replace("'attributes'",'"attributes"').replace("'place_type'",'"place_type"').replace("'quoted_status_id_str'",'"quoted_status_id_str"').replace("'quoted_status_id'",'"quoted_status_id"').replace("'media'",'"media"').replace("'media_url'",'"media_url"').replace("'type'",'"type"').replace("'media_url_https'",'"media_url_https"').replace("'source':",'"source":').replace("'id':",'"id":').replace("'favorite_count'",'"favorite_count"').replace("'coordinates'",'"coordinates"').replace("'id_str'",'"id_str"').replace("'user'",'"user"').replace("'name'",'"name"').replace("'description'",'"description"').replace("'followers_count'",'"followers_count"').replace("'url'",'"url"').replace("'verified'",'"verified"').replace("'screen_name'",'"screen_name"').replace("'friends_count'",'"friends_count"').replace("'location'",'"location"').replace("'profile_image_url'",'"profile_image_url"').replace("'entities'",'"entities"').replace("'hashtags'",'"hashtags"').replace("'urls'",'"urls"').replace("'indices'",'"indices"').replace("'expanded_url'",'"expanded_url"').replace("'display_url'",'"display_url"').replace("'created_at'",'"created_at"').replace("'retweet_count'",'"retweet_count"').replace("'geo'",'"geo"').replace("'text'",'"text"').replace("'place'",'"place"').replace("\": None",'": "None"').replace("\": False",'": "False"').replace("\": True",'": "True"').replace("\": '",'": "').replace("', \"",'", "').replace('"}",',"'}\",").replace(": ['",": \"['").replace("'], ","']\", " )
				# extraData = row[8].replace('"',"'").replace('\\', '').replace("{'",'{"').replace("'}",'"}').replace(", '",', "').replace("': ",'": ').replace(": '",': "').replace("',",'",').replace(": None",': "None"').replace(": False",': "False"').replace(": True",': "True"')
				extraDataJson = json.loads(extraData.decode('latin-1'))

				# add favorite_count into features
				newFeature.append(extraDataJson["favorite_count"])

				# add whether there were coordinates into features
				if extraDataJson["coordinates"] == "None":
					newFeature.append(0)
				else:
					newFeature.append(1)

				# add user description length and users' followers count into features
				newFeature.extend([len(extraDataJson["user"]["description"]), extraDataJson["user"]["followers_count"]])

				# add whether there were user url into features
				if extraDataJson["user"]["url"] == "None":
					newFeature.append(0)
				else:
					newFeature.append(1)

				# add whether user is verified into features
				if extraDataJson["user"]["verified"] == "False":
					newFeature.append(0)
				else:
					newFeature.append(1)

				# add user friends count into features
				newFeature.append(extraDataJson["user"]["friends_count"])

				# add whether user had a location into feathers
				if extraDataJson["user"]["location"] == "None":
					newFeature.append(0)
				else:
					newFeature.append(1)

				# add number of hashtags
				newFeature.append(len(extraDataJson["entities"]["hashtags"])) 

				if extraDataJson["place"] == "None":
					newFeature.append(0)
				else:
					newFeature.append(1)

			newFeature.append(row[9])
			writeNewData.writerow(newFeature)
			count +=1
print count

