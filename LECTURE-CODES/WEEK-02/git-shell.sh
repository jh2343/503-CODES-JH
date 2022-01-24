DATE=$(date +"%Y-%m-%d" ) #$(date +"%Y-%m-%d")
message="SYNC-"$DATE; #echo $message; exit
git add ./;
git commit -m $message;
git push
