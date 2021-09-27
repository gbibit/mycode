#!/usr/bin/env python3
""" GBibit Lab""" 

# import additional code to complete task
import shutil
import os

# move to working directory
 os.chdir("/home/student/mycode/")

 # backing up 5G Research file
 shutil.copy("5g_research/sdn_network.txt", "5g_research/sdn_network.txt.copy")

 # backing uo 5G Research director
 shutil.copytree("5g_research/", "5g_research_backup/")

# The following line will create the directory if it does not exist already

