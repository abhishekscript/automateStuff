import subprocess
import json,time,urllib2

# Change confuguration below

cfg = {  
			"wait" 			: 0,
			"sites" 		: ["hr.mantralabsglobal.com", "https://google.com" , "https://gmail.com"],
			"browsername" 	: "chromium-browser",
			"terminal" 		: "gnome-terminal",
			"commands"		: []	
     }

# end of configuration

def startPrograms():
	print "Admin waiting time ..."
	time.sleep(cfg['wait'])
	while True:
		try:
			response=urllib2.urlopen('https://google.co.in',timeout=1)
			print "Internet Available... Launching startPrograms"
			launchApps()
			break
		except urllib2.URLError as err:
			print err
			print "Internet Not Available.. trying again"
			pass
def launchApps():
	sites = cfg['sites']
	sites.insert(0,cfg["browsername"])
	#print sites
	#print browserTask
	subprocess.call(sites)
startPrograms()