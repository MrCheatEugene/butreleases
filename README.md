# butreleases
You clone the repo, but.. Releases. Where are they? They are not cloned. This little script clones the releases, including ALL THEIR BINARIES, and SOURCE CODE!
# What it does
It goes trough all of your repos(including private ones) and gets all of their releases.<br> Releases and their binaries are saved by path `./releases/reponame-releases/releasetitle - releasetag`.<br> In the same path you will find SourceCode.zip. <b>That's "Source code" of release.</b>
<br>If you are considering moving your project from Github for some reason, this is the perfect solution. 
# How to use?
0. Get your peronal token with repo permisssions
1. Edit fullrepo.py and set "token" variable value to your token.
2. Install all requirements from requirements.txt(`pip install -r requirements.txt`)
3. Run python3 ./fullrepo.py
4. Script will do it's job and then exit.

# Support me
If you liked the project, consider donating <a href="https://donationalerts.com/r/mrcheatt">here</a>. Thanks!
