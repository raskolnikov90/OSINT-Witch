from googlesearch import search
from bs4 import BeautifulSoup
from bs4.element import Tag
import requests
from dateutil import parser


def get_html(url):
	if(url.count('.pdf')==1):
		return url
	else:
		try:
			#open with GET method
			resp = requests.get(url, timeout=3)
		    	#http_respone 200 means OK status
			if resp.status_code==200:
				soup = BeautifulSoup(resp.text,'html.parser')
				return soup.get_text()
			else:
				return "Error"
		except:
			return 'Failed connection'
			
print(""".......................::::::::::..:!YGP5PGPY5GY^.:^~!?JJ^~!7????JJ???77!^:..:^~
................................:!YGGGPPGB###GPGBPPPPPP5P5^~7???????777~:....:^~
..............................~YPGGGGGGBB#&&&&#BBGGGB###GGG^!?????777!~:....:^^~
:::::......................^JPPPPPGGBB####&PPB#&##BGJ~!J5GBB!!77777!!~:. ..:^^~~
^^^:::...................!5P5555PPGB######? ..^!JY7^^~~~^~!77~~~~~~~^..  .::^^~~
~~^^::.................!P55Y555PPGGB####&#B~.::::::^~~~~!!7!:: ..::~!   ..:^^^~~
~~^::.................YGYY5555PPPGGB######&#^..::^^^~~~~~!!!^^   :^~!~ ..:^~~~~!
~^^::.......        .GGJYY55PPPGGGGBB###&&#&#: .::^^~~~~~!!!^^. ...:^?:.:^~~~~~~
^^:::.......       :BBYY55PPGGGGGGGBBB###&&&&B..::^^~~~~~~~~~^^:::::^~?.:^~~~~~~
:::::......       :BBG5PPPPGPPPGGGGGGBB###&&#&Y.::^^:^^~~~~~~~~^.....:^::^~~~~~~
::..:......      .BBBGPPPPPPPPPPGGGGGBB####&&##^.:::.?Y!^^~~^^:.. ...::^:^^~~~~~
.......:::.     .GBBGGPPPP5555PPPGGGGBBB###&&&&P .::::B#G~:^^:.   ..:::::^^^^^^^
....~JPG?:.     5BBGGGGGGPPPPPPPPPPGGBB###&&&###:..::.PBB#~::.   ..:::::::^^^^^:
  !PB#G:.....  7BBBGGPJ~^^~75BBGGGY::^!7YG#&&&&&7 ...!BGP#5..   .......:::::::::
 JGPB#^ ..... :BBG~~P.     ..!BB#B5....   .^?G#&P.:!YP55B&!    .................
.G5PG#P.      GBJ. ~^   .......:?#J..:::::..  :?GGGGBBB#B7    .....  ...........
 YG5PGBBJ!^:.?#! :.!:. .....:: ..7!:^^^^::::.....~PB5Y7^.     ..        ........
  ?GGPPPGBBBB#! :..!!........~^~^~JB&&&&##JJJ~^::..^~                           
   .~YPGB##B#Y ^..:!#!........::~B&@@@@@&G77J5#?~~^::!.                         
        ... !:::..7&&#P7~^::::~5&&@&&&BPJ~~~!P#?~7!!^^7                         
            !.^..^G&&&GP555J5#&&&&&&@G  PG!~7JB!^^~?!:~~                        
            ~^^..?7P&&G??JJ .G###&&&@&##&&55PJ~^^::^J^.!                        
            .7:..?~^G&#J~!?J5GB##&&&##B5?7~^^^:::...7!^~                        
             ~~.:~~:^7?YJ77?????5J7~~:  ^7^:::::...~G7PGY^                      
           .^!5~::!:.::::::~^.. .. . .^~::^^^::::^^YPYYJPPY7:                   
...:::..:~7JJ?5BJ^^!~^^^^^^:  ..::~:^!?^      .......~J?7J55Y7^..               
:.......:~YY5GG5J^^^!!~~.    ..JG5GYYPGP:....          :?7:...::^~^:            
 .........~5?~.     ...   ...  !Y?!!?5P~.    .::        ~ .........^!.          
..........^!           .:.. .^~~^...:~~~!~.    .^.     :: ...........7:         
.........^!         ..::..~Y5YJJJJJYJ??YYGYYY!.  :!:   .~ ..  ........?         
......:^~:       ..:. .:!~~5?7?!7~!Y?!JPPGBBY::^~^..^.  ^:      ......^~        
...:^^:.     .::... .:^~: .?77J!7?JJ7YYYP##~    ^~.  .^: ^^     ......:!        
^7~^.    .....    .:^^.    !JYPJ?JJJPPPB##~       !~::.~~ .!7:   ...~.^!        
J~:...::.....:::::..        75PPYYYPGGB##?       .!^:.~!.   7PJ^. .?G~!:        
:^7?^: .^^::..              ^5PJ7??YPPGB#!      :!:.:!^      JP5J:?GBP7         
::^J?.:~.                 .7P5P?777JP5PGBB7.   ^~..:!.       ^G5PPGBB5                    
░█████╗░░██████╗██╗███╗░░██╗████████╗░░░░░░░██╗░░░░░░░██╗██╗████████╗░█████╗░██╗░░██╗
██╔══██╗██╔════╝██║████╗░██║╚══██╔══╝░░░░░░░██║░░██╗░░██║██║╚══██╔══╝██╔══██╗██║░░██║
██║░░██║╚█████╗░██║██╔██╗██║░░░██║░░░█████╗░╚██╗████╗██╔╝██║░░░██║░░░██║░░╚═╝███████║
██║░░██║░╚═══██╗██║██║╚████║░░░██║░░░╚════╝░░████╔═████║░██║░░░██║░░░██║░░██╗██╔══██║
╚█████╔╝██████╔╝██║██║░╚███║░░░██║░░░░░░░░░░░╚██╔╝░╚██╔╝░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░░░░░░░░░░╚═╝░░░╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝

""")
interesting = []
searchtodo = input('Type company or person to search: ')
searchtodo = searchtodo.lower()
lookfor = ['names', 'email','passwords','usernames','address', 'breaches', 'credentials', 'admin',
 'database','@gmail.com','@outlook.com','@'+searchtodo+'.com', searchtodo+'@', 'location', 'contact', 'social media', 'linkedin', 'facebook', 'twitter','leaks','site:gov','site:archive.org']

queries = []


def ifexist(arg):
	if arg == None:
		return " "
	else:
		return arg
def searches(query):
	try:
		gossip = search(query, num=4, stop=4, pause=1)
		page = ''
		for i in gossip:
		    page = get_html(i).lower()
		      
		    for look in lookfor:
		    	if(queries.count(i)==0):
			    	if (page.count(look) >= 1 or str(i).count(look) > 0):
			    		queries.append(i)
		    
	except:
		print('too many requests, try later')
    		

searches(searchtodo)
countl = 0
print("Looking for interesting information...")
for look in lookfor:
	searches(searchtodo + ' ' + look)
	countl = countl + 1
	print(str(int(countl / len(lookfor) * 100)) + '%', end="\r")
print("")

for i in range(0,len(queries)):
	print(str(i)+" "+queries[i])

commonsubs = []
dirdepth = get_html('https://raw.githubusercontent.com/rbsec/dnscan/master/subdomains-100.txt')
dirdepth = dirdepth.split()
for dirs in dirdepth:
	commonsubs.append(dirs)
foundlocations = []
foundnames = []
stay  = 0
while(stay == 0):
	whattodo = int(input("""What you want to do now? 
1-Look for emails
2-Fuzz directories of a selected website
3-Look for names
4-Look for locations
5-Look for past data breaches information
6-Look for names and locations and create a wordlist txt file
0-Exit
"""))
	if(whattodo == 1):
		print("Looking for emails...")
		for website in queries:
			page = get_html(website)
			pagetext = page.split()
			for text in pagetext:
				if(text.count('@') > 0 and (text.count('.com') > 0 or  text.count('.net') > 0 or  text.count('.edu') > 0)):
					print("Email found: " + text)
					print("Source: " + website)
					print("")
					
	if(whattodo == 2):
		searchindepth = int(input('Which of the above websites would you like to look in depth? (type number) '))
		webpage = queries[searchindepth]
		webpage = webpage[1:-1]
		print('Fuzzing through directories..')
		count = 0
		for subs in commonsubs:
			page = get_html(webpage+"/"+subs)
			if(page != "Failed connection" or page.count("404") < 1):
				for look in lookfor:
					if page.count(look) >= 2:
						print('Interesting info(mention of word '+look+') found in: ' + webpage+"/"+subs)
					
	names = get_html("https://raw.githubusercontent.com/dominictarr/random-name/master/first-names.txt")
	lastnames = get_html("https://raw.githubusercontent.com/dominictarr/random-name/master/places.txt")
	cities =  get_html("https://raw.githubusercontent.com/danielmiessler/SecLists/master/Miscellaneous/us-cities.txt") 
	locations= ['Afghanistan','Albania','Algeria','American Samoa','Andorra','Angola','Anguilla','Antarctica','Antigua And Barbuda','Argentina','Armenia','Aruba','Australia','Austria','Azerbaijan','Bahamas','Bahrain','Bangladesh','Barbados','Belarus','Belgium','Belize','Benin','Bermuda','Bhutan','Bolivia','Bosnia And Herzegovina','Botswana','Bouvet Island','Brazil','British Indian Ocean Territory','Brunei Darussalam','Bulgaria','Burkina Faso','Burundi','Cambodia','Cameroon','Canada','Cape Verde','Cayman Islands','Central African Republic','Chad','Chile','China','Christmas Island','Cocos (keeling) Islands','Colombia','Comoros','Congo','Congo,TheDemocratic Republic Of The','Cook Islands','Costa Rica','Cote Divoire','Croatia','Cuba','Cyprus','Czech Republic','Denmark','Djibouti','Dominica','Dominican Republic','East Timor','Ecuador','Egypt','El Salvador','Equatorial Guinea','Eritrea','Estonia','Ethiopia','Falkland Islands (malvinas)','Faroe Islands','Fiji','Finland','France','French Guiana','French Polynesia','French Southern Territories','Gabon','Gambia','Georgia','Germany','Ghana','Gibraltar','Greece','Greenland','Grenada','Guadeloupe','Guam','Guatemala','Guinea','Guinea-bissau','Guyana','Haiti','Heard Island And Mcdonald Islands','Holy See (vatican City State)','Honduras','Hong Kong','Hungary','Iceland','India','Indonesia','Iran','Islamic Republic Of','Iraq','Ireland','Israel','Italy','Jamaica','Japan','Jordan','Kazakstan','Kenya','Kiribati','Korea','Democratic People Republic Of Korea','Republic Of','Kosovo','Kuwait','Kyrgyzstan','Lao People Democratic Republic','Latvia','Lebanon','Lesotho','Liberia','Libyan Arab Jamahiriya','Liechtenstein','Lithuania','Luxembourg','Macau','Macedonia','The Former Yugoslav Republic Of', 'Madagascar','Malawi','Malaysia','Maldives','Mali','Malta','Marshall Islands','Martinique','Mauritania','Mauritius','Mayotte','Mexico','Micronesia','Federated States Of','Moldova,Republic Of','Monaco','Mongolia','Montserrat','Montenegro','Morocco','Mozambique','Myanmar,Namibia','Nauru','Nepal','Netherlands', 'Netherlands Antilles','New Caledonia','New Zealand','Nicaragua','Niger','Nigeria','Niue','Norfolk Island','Northern Mariana Islands','Norway','Oman','Pakistan','Palau','Palestinian Territory','Panama','Papua New Guinea','Paraguay','Peru','Philippines','Pitcairn','Poland','Portugal','Puerto Rico','Qatar', 'Reunion','Romania','Russian Federation','Rwanda','Saint Helena','Saint Kitts And Nevis','Saint Lucia','Saint Pierre And Miquelon','Saint Vincent And The Grenadines','Samoa','San Marino','Sao Tome And Principe','Saudi Arabia','Senegal','Serbia','Seychelles','Sierra Leone,Singapore,Slovakia','Slovenia','Solomon Islands','Somalia','South Africa','South Georgia And The South Sandwich Islands','Spain','Sri Lanka','Sudan,Suriname','Svalbard And Jan Mayen','Swaziland', 'Sweden','Switzerland','Syrian Arab Republic','Taiwan','Province Of China','Tajikistan','Tanzania','United Republic Of','Thailand','Togo','Tokelau,Tonga', 'Trinidad And Tobago','Tunisia','Turkey','Turkmenistan','Turks And Caicos Islands','Tuvalu','Uganda','Ukraine','United Arab Emirates','United Kingdom','United States','United States Minor Outlying Islands','Uruguay','Uzbekistan','Vanuatu','Venezuela','Viet Nam','Virgin Islands','British','Virgin Islands','U.s.', 'Wallis And Futuna','Western Sahara','Yemen','Zambia','Zimbabwe']
	lastnames = lastnames.replace(',',' ')
	cities = cities.split("\n",-1)
	nonnames = get_html("https://raw.githubusercontent.com/first20hours/google-10000-english/master/google-10000-english.txt") + " All " + " Will " + " Brand " + "And" + "One" + "-"
	if(whattodo == 3 or whattodo == 6):
		print("Looking for names...")
		for website in queries:
			page = get_html(website)
			pagetext = page.split()
			for i in range(0,len(pagetext)):
				if nonnames.count(pagetext[i].capitalize()) == 0 and nonnames.count(pagetext[i]) == 0 and len(pagetext[i]) > 2 and foundnames.count(pagetext[i]) < 1:
					pagetext[i] = pagetext[i].capitalize()
					if(names.count(pagetext[i]+"") > 3 and page.count(" "+pagetext[i]+" ") > 0 and lastnames.count(pagetext[i]+"") > 3 and page.count(" "+pagetext[i]+" ") > 0) :
						print("Possible name found in line:" )
						print(pagetext[i-1]+" "+pagetext[i]+" "+ifexist(pagetext[i+1]))
						print("On website: " + website)
						print(" ")
						foundnames.append(pagetext[i])
		if(len(foundnames) == 0):
			print("No names where found try different searches")
	if(whattodo == 4 or whattodo == 6):
		print("Looking for locations...")
		for website in queries:
			pagetext = get_html(website)
			for i in range(0,len(locations)):
				if(foundlocations.count(locations[i]) < 2):
					if(pagetext.count(locations[i].capitalize()) > 1 and len(locations[i]) > 3):
						print("Possible country found:" )
						print(locations[i])
						print("On website: " + website)
						print(" ")
						foundlocations.append(locations[i])
						for city in range(0,len(cities)):
							if(foundlocations.count(cities[city]) < 1 and nonnames.count(cities[city]) == 0):
								if(pagetext.count(cities[city].capitalize()) > 3 and len(cities[city]) > 3):
									print("Possible city found:" )
									print(cities[city])
									print("On website: " + website)
									print(" ")
									foundlocations.append(cities[city])
		if(len(foundlocations) == 0):
			print("No locations where found try different searches")
	if(whattodo == 5):
		print("Looking for past breaches information...")
		for website in queries:
			pagetext = get_html(website).lower()	
			breaches = ['breach','breaches','breached','leaks','hacked','passwords']
			for breach in breaches:
				if(pagetext.count(breach) > 3 or website.count(breach) == 1):
					print("Info about past breaches found in:")
					print(website)
					print("")
	if(whattodo == 6):
		with open("witchwordlist.txt","w") as file:
			for names in foundnames:
				file.write(names+"\n")
				file.write(names.lower()+"\n")
			for location in foundlocations:
				location = location.replace(" ","")
				file.write(location+"\n")
				file.write(location.lower()+"\n")
			print("witchwordlist.txt was created")
	
	if(whattodo == 0):
		stay = 1
