import requests

# MAKE URL 
# MAKE METHOD
# MAKE TYPE
# list types:
	'''activity, captions, channelBanners, channelSections, channel, commentThread, comment, guideCategory, i18nLanguage, i18nRegion, member, membershipsLevel, playlistItem, playlist, subscription, thumbnail, videoAbuseReportReason, videoCategory, video, watermark'''

URL = "https://www.googleapis.com/youtube/v3"
def make_url(base_url = "https://www.googleapis.com/youtube/v3", types=None, token):
	request_url = f"{base_url}/{types}?access_token={token}"
	header = {"Authorization" : "oauth2-token"}

