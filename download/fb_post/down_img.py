import requests
url = 'https://scontent.fhph1-1.fna.fbcdn.net/v/t1.6435-9/75412174_2698101273584720_3543431573493776384_n.jpg?_nc_cat=104&_nc_map=control&ccb=1-3&_nc_sid=8bfeb9&_nc_ohc=IKn3-nE2SBUAX9I8TPL&_nc_ht=scontent.fhph1-1.fna&oh=663e9f0c2b3c626da1852a7e9edb3d0a&oe=609E3D5B'

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
download_file(url, 'picxx')