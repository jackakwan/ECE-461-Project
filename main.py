""" Name: Matthew Nale, Eric Chen 
    Date of Last Edit: 2/5/2023
    
    Purpose: Used for testing individual functions and function calls, without having to setup Rust-Python integration

    Details: Individual calls can be made below, such as for Licensing.py and repo_clone.py, in order to ensure compatability with all files
"""

import sys
import subprocess                                                               #Used for calling executables (Compiled Rust files) with arguements
import os

from NetScoreCalculation.MetricCalculation.licensing import calculateLicenseScore
from Submodules.repo_clone import clone_repo
import Submodules.readme as rm
import Submodules.issues as issues
import Submodules.pull_requests as pulls
from Submodules.npm_handler import npm2git
import Submodules.file_information as files

url_in = sys.argv[1] 
   
if"npmjs" in url_in:                                                            #Converts npm to github if necessary 
    url = npm2git(url_in)  
else: 
    url = url_in                                                                #Obtains the URL link from argv[1]. Will later be modified to take a .txt file instead
repo = clone_repo(url)                                                          #Clones the repository from the given URL, and a GitPython Repo object is stored in repo
license_score = calculateLicenseScore(repo)                                     #license_score is determined by the evaluate_readme function in Licensing.py

readmeLength = rm.checkRMLength(repo)                                           #Example usage of the checkRMLength function in readme.py, which returns the lines of the README
print(f'Number of lines in the README: {readmeLength}')
repoSize = files.getDirectorySize(url)                                          #Example usage of the getDirectorySize function, which returns the size of the directory
print(f"Size of the directory: {repoSize}")

numIssues = issues.getIssuesByType(url, 'open')                                 #Example usage of the getIssuesByTypes function, which obtains the number of open issues
print(f'Number of open issues: {numIssues}')
numDownloads = issues.getUsers(url)                                             #Example usage of the getUsers function, which obtains the number of downloads of the repo
print(f'Estimated number of users: {numDownloads}')

recentPull = pulls.getMostRecentPull(url, 'closed')                             #Example usage of the getMostRecentPull function, which obtaines the most recent closed pull request
print(f'The most recent pull request was: {recentPull} time ago')
#pullDates = pulls.getAllPullDates(url, 'closed')                               #Example usage of the getAllPullDates function, which obtains a list of all Pull Request dates
#print(pullDates)

creationDate = pulls.getCreationDate(url)
print(f'The creation date of the repository was: {creationDate}')

executable = os.path.dirname(__file__) + "/NetScoreCalculation/net_score.exe "
#Arguements for NetScore file. Add more as needed
args = f"{license_score} {numIssues} {numDownloads} {readmeLength} 100"                         
subprocess.run(executable + args, cwd=None, shell=False)
