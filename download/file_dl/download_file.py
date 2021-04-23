import requests


def download_file(url, name):
	# NOTE the stream=True parameter below
	with requests.get(url, stream=True, allow_redirects=True) as r:
		r.raise_for_status()
		with open(name, 'wb') as f:
			for chunk in r.iter_content(chunk_size=8192):
				# If you have chunk encoded response uncomment if
				# and set chunk_size parameter to None.
				#if chunk:
				f.write(chunk)
	return name

attach_data = {'2': 'WTDistributorsPVCspecs+Warranty.doc', '6': 'ShadetexTechnicalinformation.pdf',
               '7': 'N27-160.pdf', '8': 'H35-130.pdf', '9': 'H35-200.pdf', '10': 'N31-190.pdf',
               '11': 'EvaDureEVA-ProductRangeDatasheet.pdf', '12': 'DurafoamPE30.pdf', '13': 'N20-100.pdf',
               '14': 'U29-400.pdf', '15': 'H42-500.pdf', '16': 'WB6350-WB3348.pdf',
               '17': 'WI3848testresult.pdf', '18': 'WI4025.pdf', '19': 'Spectratestresults.pdf',
               '23': 'HeliosPDatasheet2014-04_tcm35-17885.pdf', '24': 'T84BONDSTRENGTH.pdf',
               '25': 'Eyelets-HEF-18ESM.pdf', '26': 'Eyelets-HP-36.pdf', '27': 'Eyelets-HP-40.pdf',
               '28': 'Eyelets-KP-36KickPress.pdf', '29': 'Eyelets-M5HandPress.pdf',
               '30': 'Model3P5EyeletsSupply.pdf', '31': 'Model3P5-XEyeletsSupply.pdf',
               '32': 'Model4KEWEyeletSupply.pdf', '33': "CoatedBacklitBannerSpec's.doc",
               '34': "CoatedBlockoutBannerSpec's.doc", '35': "CoatedMeshBannerSpec's.doc",
               '36': "FrontlitBannerSpec's.doc", '37': 'Weldablewebtestresult.pdf', '38': 'seatbeltweb.pdf',
               '45': 'EMAILORDERFORM(WITHCOURIER).xls-CompatibilityMode.pdf'}

for key, value in attach_data.items():
        url = 'https://www.webbing.co.nz/attachment.php?id_attachment={}'.format(key)
        download_file (url, value)
        
# [
#     {
#         "title": "Download",
#         "id": "download",
#         "content": "<p><a href=\"http://syn142.syd4.hostyourservices.net/~webbingc/wp-content/uploads/filedownload/EMAILORDERFORM(WITHCOURIER).xls-CompatibilityMode.pdf\">FILE NAME</a></p>"
#     }
# ]
# http://43.250.140.47/~webbingc/wp-content/uploads/filedownload/