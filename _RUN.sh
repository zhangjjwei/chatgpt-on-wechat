date
sudo ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
sudo dpkg-reconfigure -f noninteractive tzdata
date

nohup python3 app.py > output.log 2>&1 &
disown
