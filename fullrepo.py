from github import Github
import os,requests,shutil
token = "TOKEN" # Personal token WITH REPO PERMISSIONS
g = Github(token) # creating pygithub object
if not os.path.exists("releases"):
    os.mkdir("releases")
    pass
for repo in g.get_user().get_repos():# for each repo
    releases = repo.get_releases()  # getting releases
    reporeleasesfoldername = "releases/"+repo.name+"-releases" # generating folder name for releases of repo X
    if not os.path.exists(reporeleasesfoldername): # if not exists, creating
        os.mkdir(reporeleasesfoldername)
        pass
    for release in releases: # for each release
        releasefoldername = reporeleasesfoldername+"\\"+str(release.title)+" - "+release.tag_name # folder name for assets of release X
        if not os.path.exists(releasefoldername): # if not exists, creating
            os.mkdir(releasefoldername)
        pass        
        print("Downloading release ZIP file(Source Code)..")
        try: # try / except for preventing script crash 
            r = requests.get(release.zipball_url, headers={"Authorization":"token "+token,"Accept":"application/json"}) # downloading asset
            if r.status_code < 250:# is status code in "OK" range?
                open(releasefoldername+"\\"+("SourceCode.zip"), 'wb').write(r.content) # downloading
                print("Success") # all done, sending log message
            else: # status code invalid
                print("Failed to download source code, got non-standart respose code!") # log message
        except Exception as e: # exception
            print("Unable to download source, got exception") # log message
            print(e) # exception        
        for asset in release.get_assets(): # for each asset
            try: # try / except for preventing script crash 
                print("Downloading asset "+asset.name) # sending log message                
                r = requests.get(asset.url, headers={"Authorization":"token "+token,"Accept":"application/octet-stream"}) # downloading asset
                if r.status_code < 250:# is status code in "OK" range?
                    open(releasefoldername+"\\"+(asset.name.replace("\\","").replace("/","").replace("\\","").replace(":","").replace("?","").replace("\"","").replace("*","").replace("|","").replace("<","").replace(">","")), 'wb').write(r.content) # downloading
                    print("Success") # all done, sending log message
                else: # status code invalid
                    print("Failed to download asset "+asset.name+", got non-standart respose code!") # log message
            except Exception as e: # exception
                print("Unable to download asset, got exception") # log message
                print(e) # exception
            pass
        pass