╔╦╗┬┌─┐┌┬┐┬─┐┬┌┐ ┬ ┬┌┬┐┌─┐┌┬┐  ╔╦╗┌─┐┌┐┌┬┌─┐┬    ┌─┐┌─┐  ╔═╗┌─┐┬─┐┬  ┬┬┌─┐┌─┐
 ║║│└─┐ │ ├┬┘│├┴┐│ │ │ ├┤  ││   ║║├┤ ││││├─┤│    │ │├┤   ╚═╗├┤ ├┬┘└┐┌┘││  ├┤ 
═╩╝┴└─┘ ┴ ┴└─┴└─┘└─┘ ┴ └─┘─┴┘  ═╩╝└─┘┘└┘┴┴ ┴┴─┘  └─┘└    ╚═╝└─┘┴└─ └┘ ┴└─┘└─┘




## Command and Control:
	
	So, i use arch linux, so..
	[# pacman -S] -> install packages
	
	# pacman -Sy nmap
	# pacman -Sy ssh
				
						                                                            
## Bots:
	
	ssh enabled hosts, present in the same network
	Host must be that system’s administrator 



## Imprementations:
   
	### 1. TCP SYN flooding attack ###
		
		# python2 botSearcher.py
		
			This code will look for IP addresses in the local network using nmap tool. To change the network address, edit line 4 of this program.
			This tool will save the results in "nmapOP.xml" file. 
			"botSearcher.py" will then parse this xml file and looks for systems which are up and whose ports are unfiltered and store the IP address of those systems in "IPList.txt" file.
		
		
		$ gcc -pthread botMaker.c
			
			$./a.out
					
				"botMaker.c" will take the username and password of the bots and will also take the input as name of the python code for implementing this attack. In this case filename is "TCPSyn.py". This attack will be for 60 seconds. This time value can be changed by changing the value on line 104 in TCPSyn.py file.


### Output ###
	
	On terminal, login screen of connected hosts will appear. Error messages from unsuccessful connection to hosts will also appear. After the attack, "success" message will be displayed from the all the hosts.
	Can also run wireshark on the victim system to see the packets.


		# 2. TCP PSH+ACK flooding attack:        
		    $ sudo python2 botSearch.py

		    	This code will look for IP addresses in the local network using nmap tool.
		    
		    $ gcc -pthread botMaker.c
		    
		    $./a.out
		    	
		    	"botMaker.c" will take the username and password of the bots and will also take the input as name of the python code for implementing this attack. In this case filename is "TCPpsh+ack.py". This attack will be for 60 seconds. This time value can be changed by changing the value on line 104 in TCPpsh+ack.py file.



## Bandwidth Depletion attack:

	UDP flooding attack:

		$ sudo python2 botSearch.py

		    This code will look for IP addresses in the local network using nmap tool.
		    

		    $gcc -pthread botMaker.c
		    
		    $./a.out

			
			### Output ###
			
				* On terminal, login screen of connected hosts will appear. Error messages from unsuccessful connection to hosts will also appear. After the attack, 
				"success" message will be displayed from the all the hosts.
				* Can also run wireshark on the victim system to see the packets.

