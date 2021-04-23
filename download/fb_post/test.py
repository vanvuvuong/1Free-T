import re
a = '''[<a aria-label="Có thể là hình ảnh về 1 người và đang cười" class="oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso pmk7jnqg i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l i09qtzwb n7fi1qx3 j9ispegn kr520xx4 tm8avpzi" href="/photo/?fbid=2698101270251387&amp;set=pcb.2698101366918044&amp;__cft__[0]=AZVVXTbyepcd6gheVQWFKcD7u63q-u54nVrsF5hPcbjo0hUigIv-TkDfkK1_ChJVD5GitkpFxWPj2N37hMULHSoyHLzz_GP3u-b6gy8cvmvH-MPDXCEoIdGWt7By3M-sftM&amp;__tn__=*bH-R" role="link" tabindex="0"><div class="stjgntxs ni8dbmo4"><div class="do00u71z ni8dbmo4 stjgntxs l9j0dhe7" style="padding-top:200%"><div class="pmk7jnqg kr520xx4" style="height:100%;left:-29.722222222222406%;width:calc(((640/800)/0.5)*100%)"><img alt="" class="i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm" referrerpolicy="origin-when-cross-origin" src="https://scontent.fhph1-1.fna.fbcdn.net/v/t1.6435-9/75412174_2698101273584720_3543431573493776384_n.jpg?_nc_cat=104&amp;_nc_map=control&amp;ccb=1-3&amp;_nc_sid=8bfeb9&amp;_nc_ohc=IKn3-nE2SBUAX9I8TPL&amp;_nc_ht=scontent.fhph1-1.fna&amp;oh=663e9f0c2b3c626da1852a7e9edb3d0a&amp;oe=609E3D5B"/></div></div><div class="hzruof5a opwvks06 linmgsc8 kr520xx4 j9ispegn pmk7jnqg n7fi1qx3 rq0escxv i09qtzwb"></div></div><div class="n00je7tq arfg74bv qs9ysxi8 k77z8yql i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s" data-visualcompletion="ignore"></div></a>, <a aria-label="Không có mô tả ảnh." class="oajrlxb2 gs1a9yip g5ia77u1 mtkw9kbi tlpljxtp qensuy8j ppp5ayq2 goun2846 ccm00jje s44p3ltw mk2mc5f4 rt8b4zig n8ej3o3l agehan2d sk4xxmp2 rq0escxv nhd2j8a9 q9uorilb mg4g778l btwxx1t3 pfnyh3mw p7hjln8o kvgmc6g5 cxmmr5t8 oygrvhab hcukyx3x tgvbjcpo hpfvmrgz jb3vyjys rz4wbd8a qt6c0cv9 a8nywdso pmk7jnqg i1ao9s8h esuyzwwr f1sip0of du4w35lb lzcic4wl abiwlrkh p8dawk7l i09qtzwb n7fi1qx3 j9ispegn kr520xx4 tm8avpzi" href="/photo/?fbid=2698101326918048&amp;set=pcb.2698101366918044&amp;__cft__[0]=AZVVXTbyepcd6gheVQWFKcD7u63q-u54nVrsF5hPcbjo0hUigIv-TkDfkK1_ChJVD5GitkpFxWPj2N37hMULHSoyHLzz_GP3u-b6gy8cvmvH-MPDXCEoIdGWt7By3M-sftM&amp;__tn__=*bH-R" role="link" tabindex="0"><div class="stjgntxs ni8dbmo4"><div class="do00u71z ni8dbmo4 stjgntxs l9j0dhe7" style="padding-top:200%"><div class="pmk7jnqg kr520xx4" style="height:calc((0.5/(462/960))*100%);top:0%;width:100%"><img alt="" class="i09qtzwb n7fi1qx3 datstx6m pmk7jnqg j9ispegn kr520xx4 k4urcfbm" referrerpolicy="origin-when-cross-origin" src="https://scontent.fhph1-1.fna.fbcdn.net/v/t1.6435-9/s960x960/77163546_2698101333584714_6686943520692895744_n.jpg?_nc_cat=102&amp;_nc_map=control&amp;ccb=1-3&amp;_nc_sid=8bfeb9&amp;_nc_ohc=Xu6tuFNEvisAX_OSd8m&amp;_nc_ht=scontent.fhph1-1.fna&amp;tp=7&amp;oh=9dbc1f81cb36f675d0a82888098dbe07&amp;oe=609EBD29"/></div></div><div class="hzruof5a opwvks06 linmgsc8 kr520xx4 j9ispegn pmk7jnqg n7fi1qx3 rq0escxv i09qtzwb"></div></div><div class="n00je7tq arfg74bv qs9ysxi8 k77z8yql i09qtzwb n7fi1qx3 b5wmifdl hzruof5a pmk7jnqg j9ispegn kr520xx4 c5ndavph art1omkt ot9fgl3s" data-visualcompletion="ignore"></div></a>]'''
def get_link(data):
	flag = True
	# new_data = ''
	if '</div></div>' in data:
		data = data.replace('</div></div>', ' ')
	start_cut = re.findall(r'src', data)
	stop_cut = re.findall(r'/>', data)
	list_string = data.split (' ')
	tmp, meta = [], []
	for element in list_string:
		if start_cut[0] in element:
			flag=True
		if stop_cut[-1] in element:
			flag=False
			meta.append(element)
			continue
		if flag:
			tmp.append(element)
	new_data = ' '.join (tmp)
	# meta_data = ' '.join (meta)
	# symbol = '< > = ,'
	# for i in symbol.split(' '):
	# 	if i in new_data:
	# 		new_data = new_data.replace(i, '')
	meta[0] = meta[0].replace('src="','')
	return meta[0].replace('"/>','')

def get_abs_link(string):
	flag = False
	link = ''
	for i in string:
		if '=' == i:
			flag = True
		if '/' == string:
			flag = False
		if flag:
			link += i
	return i
c = get_link(a)
# c = get_abs_link(c)

print (c)