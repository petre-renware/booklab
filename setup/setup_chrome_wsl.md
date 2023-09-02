# Setup Chrome WSL



## Installing Chrome

```
sudo apt-get update

sudo apt-get install -y curl unzip xvfb libxi6 libgconf-2-4 libatk-bridge2.0-0

sudo apt install libnss3-dev libatk1.0-0 libatk-bridge2.0-0 libcups2 libgbm1 libpangocairo-1.0-0 libgtk-3-0



wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb

```

-#FIXME here to clean all created files and dir(s) or work directly on tmp/ directory

Check:

`google-chrome --version`


## Installing ChromeDriver

Find the URL of the ChromeDriver version that matches your Chrome version on the ChromeDriver website. It should be a zip file; in my case it’s

`wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chrome-linux64.zip`

Download, unzip, and put it in your bin directory:

```
wget https://edgedl.me.gvt1.com/edgedl/chrome/chrome-for-testing/116.0.5845.96/linux64/chrome-linux64.zip
unzip chrome-linux64.zip
cd  chrome-linux64/
sudo cp chrome /usr/bin/chromedriver
sudo chown root:root /usr/bin/chromedriver
sudo chmod +x /usr/bin/chromedriver
```

Double check it worked:

`chromedriver --version`

If was previously installed drivers, check version

`which chromedriver`












