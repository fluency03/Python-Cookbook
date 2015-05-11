#!/usr/bin/python

import urllib.request
import urllib.error
import http.cookiejar
import re
import sys

class TUE_OASE():
	def __init__(self):
		# Login URL
		self.top_level_url = 'https://educationsso.tue.nl'
		# Homepage URL
		self.homepage_url = 'https://educationsso.tue.nl/Profiel/Pages/Default.aspx'
		# s-username
		self.username = sys.argv[1]
		# password
		self.password = sys.argv[2]
		# CookieJar subject
		self.cookies = http.cookiejar.CookieJar()
		# require the authentication
		self.authentication()
	def authentication(self):
		# create a password manager
		password_manager = urllib.request.HTTPPasswordMgrWithDefaultRealm()
		password_manager.add_password(None, self.top_level_url, self.username, self.password)
		# because we have put None at the start it will always
		# use this username/password combination for  urls
		# for which `theurl` is a super-url
		# create the AuthHandler
		self.authhandler = urllib.request.HTTPBasicAuthHandler(password_manager)
	def getPage(self):
		# create the opener
		opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(self.cookies), self.authhandler)
		urllib.request.install_opener(opener)
		# All calls to urllib2.urlopen will now use our handler
		# Make sure not to include the protocol in with the URL, or
		# HTTPPasswordMgrWithDefaultRealm will be very confused.
		# You must (of course) use it when fetching the page though.
		# authentication is now handled automatically for us
		page_data = urllib.request.urlopen(self.homepage_url).read()
		# write page data to a login_info.txt file
		login_file = open('login_info.txt', 'wb')
		login_file.write(page_data)
		login_file.close()
		return page_data
	def getTranscripts(self):
		# obtian the page data
		page_data = self.getPage()
		# --------------------------------------------------------------------
		subject_pattern = re.compile(r'<span\sid\=\"ctl00_m_g_88e55087_7c5e_48ee_9376_906d69fe93a6_ctl00_ui_complexList_results_rp_list_ctl\d\d_column\d\d_lb_value\">(.*?)</span>')
		subject_data = subject_pattern.findall(str(page_data))
		num_subject = int(len(subject_data)/5)
		subject_grid = [[] for k in range(num_subject)]
		for i in range(num_subject):
				subject_grid[i] = subject_data[(i*5):((i+1)*5)]
		# --------------------------------------------------------------------
		student_pattern = re.compile(r'<span\sid=\"ctl00_tue_loginHeader_lbl_username\">Welcome\s(.*?)\s-\s</span>')
		student_data = student_pattern.findall(str(page_data))
		# --------------------------------------------------------------------
		self.writeTranscripts(subject_grid, student_data)
	def writeTranscripts(self, subject_grid, student_data):
		transcripts_file = open('transcripts.txt', 'w')
		line = 'This is the transcripts of {:}, which includes the grades of last 10 subjects.\n\n'.format(student_data[0])
		transcripts_file.write(line)
		line = '{0:^17s}\t{1:^60s}\t{2:^17s}\t{3:^5s}\t{4:^3}\n'.format('Evaluation Date', 'Subject', 'Program', 'Grade', 'ECTS')
		transcripts_file.write(line)
		for subject in subject_grid:
			line = '{0:^17s}\t{1:<60s}\t{2:^17s}\t{3:^5s}\t{4:^3}\n'.format(subject[0], subject[1], subject[2], subject[3], subject[4])
			transcripts_file.write(line)
		transcripts_file.close()




oase = TUE_OASE()

oase.getTranscripts()













