# Overtherainbow
OverTheRainbow is a set of python scripts to interact with Nessus &amp; Metasploit API

# Development
Project is currently under creation

# Dependencies
To run the scripts you need to install previously the Nessus scanner package from https://support-tenable.com/support-center/
Linux dependencies are:
-python-requests

# How to use
Begin by creating a Nessus API key, a target folder and a policy
Then configure getNessusFolders.py and getNessusPolicies.py with the API keys to obtain the Nessus folders and policies ids.

Once you have all the ids, update the createNessusScan.py with the requested settings and launch ./createNessusScan.py <IP_file>
