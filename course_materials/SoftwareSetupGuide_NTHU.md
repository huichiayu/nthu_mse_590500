# MSE 590500

## Software Setup Guide

As this is a course in computational modeling and data science, you will be completing your assignments using your computer! However, in order to do so there are a number of things you need to set up before the course starts. If you run into issues during this setup process make sure to document the error you encountered and send an email to your Professor to let him know that you ran into a problem.

**We assume we will use Jupyter notebook for Python programming.** 


---
## Table of Contents

### Setting up important software 

* [Installing Python](#python)
    * [Updating a previous installation](#update-anaconda)
    * [Checking that Python is available in your command line path](#check-path)
    * [If you don't have a fully functioning, up-to-date version](#install-anaconda)
        * [Installing Anaconda for Windows](#anaconda-windows)
        * [Installing Anaconda for Mac](#anaconda-mac)
		* [Installing the Atom text editor](#atom)

---
<a id="software"></a>
## Setting up important software <br> (if you want to run your code locally)
---
<a id="python"></a>
### Installing Python for this course
If you choose to use a local Python installation for this course (you're absolutely welcome to!), you need to have an **Anaconda** Python installation that is both **functioning** and **current**. If you have a past installation, you are expected to make sure it is up-to-date. You can update your current Anaconda install by following [these directions](#update-anaconda).

In addition to making sure your installation is updated, you should also ensure that the Anaconda installation is in your default path. You can check that this is true by following [these directions](#check-path)

If you don't already have Anaconda installed or if you already had Anaconda, but you couldn't get the update to work or ensure that Anaconda is in your path, you should install a fresh version of Anaconda following [these directions](#install-anaconda).

<a id="update-anaconda"></a>
#### Updating a previous installation

<a id="update-windows"></a>
##### Updating on Windows ([jump to Mac directions](#update-mac))
1. Make sure you are connected to the internet

2. Find your Anaconda prompt and update Anaconda.

	<img src="./images/prompt.PNG" width="500">

    On keyboard press <kbd> Windows-key </kbd> or simply use the search bar on the taskbar if it is visible. Search `Anaconda Prompt` and right-click on the search result and select "Run as administrator".  

	<img src="./images/update01.PNG" width="500">
	
    Type in the command `conda update --all` and press `Enter`. This command will update anaconda.  

	<img src="./images/update02.PNG" width="500">

    To continue type `y` and press enter.  

	<img src="./images/update03.PNG" width="500">

    If all goes well you should be all updated. To close out of the terminal type `exit` and press enter.

Now double-check that Python is [available in your commandline path](#check-path).

<a id="update-mac"></a>
##### Updating on a Mac [(jump to Windows directions](#update-windows))
1. Make sure you are connected to the internet  
2. Find your terminal and update Anaconda.

	<img src="./images_mac/cmd_update.png" width="500">

    Using Spotlight by pressing <kbd> command </kbd> + <kbd> space-bar </kbd> or simply use the search bar in the top right corner search `terminal` and press `Enter`. Then type in the command `conda update --all` and press `Enter`. This command will update anaconda.  

	<img src="./images_mac/update_y.png" width="500">


    To continue type `y` and press enter.  

	<img src="./images_mac/update_done.png" width="500">

    If all goes well you should be all updated.

<a id="check-path"></a>
#### Checking that Python is available in your command line path

<a id="check-path-windows"></a>
##### Checking your path on Windows ([jump to Mac directions](#check-path-mac))
1. Make sure Anaconda is already installed on your system.

2. Open up any terminal besides anaconda prompt and run Jupyter Notebook.

	<img src="./images/run.PNG" width="500">

    On keyboard press <kbd> Windows-key </kbd> + <kbd> r </kbd> or simply use the search bar on the taskbar if it is visible. Enter `cmd` and press enter. This will open up the Windows Command terminal.  

	<img src="./images/cmd_jupyter.PNG" width="500">

    Type in `jupyter notebook` and press `Enter`. This should launch a jupyter notebook tab on a web browser.

	<img src="./images/exit01.PNG" width="500">

	<img src="./images/exit02.PNG" width="500">

    To exit jupyter notebook close the tab on the web browser, and go to the terminal window and type <kbd> Ctrl </kbd> + <kbd> c </kbd> twice in a row.  

<a id="check-path-mac"></a>
##### Checking your path on a Mac ([jump to Windows directions](#check-path-windows))
1. Make sure Anaconda is already installed on your system.

2. Open up the terminal and run Jupyter Notebook.

	<img src="./images_mac/cmd_jupyter_mac.png" width="500">

    Using Spotlight by pressing <kbd> command </kbd> + <kbd> space-bar </kbd> or simply use the search bar in the top right corner search `terminal` and press `Enter`. Then type in `jupyter notebook` and press `Enter`.

	<img src="./images_mac/jup.png" width="500">

    This should launch a jupyter notebook tab on a web browser and the terminal should look like this.

	<img src="./images_mac/jup_close.png" width="500">

    To exit jupyter notebook close the tab on the web browser, and go to the terminal window and type <kbd> control </kbd> + <kbd> c </kbd> twice in a row.

<a id="install-anaconda"></a>
#### If you don't having a fully functioning up-to-date installation of Anaconda Python

If you have a Windows computer, jump to [this section](#anaconda-windows) and follow the instructions.

If you have a Mac, jump to [this section](#anaconda-mac) and follow the instructions.

If you have a Linux computer and aren't sure how to go about installing Anaconda, contact you instructor.

<a id="anaconda-windows"></a>
##### Installing Anaconda for Windows
Instructions for downloading and installing Anaconda (Python 3):

1. Go to the [Anaconda Download webpage:](https://www.anaconda.com/download/)

2. Use the `download` button (or scroll until you see `Anaconda Installers`)

	<img src="./images/anaconda_download.PNG" width="500">

3. Download the current version of Python 3, you'll notice there is a 32-bit and 64-bit version. If you are unsure which you should download, you'll most likely want the 64-bit version, but if you want to be sure, follow the instructions below.

    a. On keyboard press <kbd> Windows-key </kbd> or simply use the search bar on the taskbar if it is visible.  

    b. Search `System Information` and click on the search result.  

	<img src="./images/system.PNG" width="500">

    c. Look for the line called `System Type`

       * If it reads `x64-based PC` you have a 64-bit system and you should download 64-bit Anaconda.

       * If it reads `x86-based PC` you have a 32-bit system and you should download 32-bit Anaconda.

	<img src="./images/sys.PNG" width="500"> 

4. After downloading, run the Anaconda Installer Executable. Say `yes` to any warnings.

	<img src="./images/01.PNG" width="500">
  
	<img src="./images/02.PNG" width="500">
   
	<img src="./images/03.PNG" width="500">

    Any option here is ok, change to `All Users` if you want to install to all accounts on your PC.

	<img src="./images/04.PNG" width="500">

    *Change the Destination folder at your own risk* If troubles creep up later in class with using Anaconda, this might make the issues harder to fix. If you do change location, make sure it remains on the drive your windows installation is on.  

	<img src="./images/05.PNG" width="500">

    **Make sure to enable this option** This is required for software this class uses.  

	<img src="./images/06.PNG" width="500">

    Installation may take awhile, it may stay at this screen for awhile. Be patient.  

	<img src="./images/07.PNG" width="500">
  
	<img src="./images/08.PNG" width="500">
 
	<img src="./images/09a.PNG" width="500">
	
    Any option here is okay, if you want to get a feel for the things Anaconda can do, feel free to keep those checkboxes selected.  

5. Open the command line program on your computer.

	a. On keyboard press <kbd> Windows-key </kbd> + <kbd> r </kbd> or simply use the search bar on the taskbar if it is visible.

   b. Enter `cmd` and press enter.

   ![run](./images/run.PNG)

6. Type `jupyter notebook` in the command line and hit enter.

	<img src="./images/cmd_jupyter.PNG" width="500">

    If everything goes correctly, a browser window should open up with the Jupyter interface running. If things don’t work, don’t worry, we will help you get started.

	<img src="./images/exit01.PNG" width="500">

    To exit jupyter notebook close the tab on the web browser, and go to the cmd window and type <kbd> Ctrl </kbd> + <kbd> c </kbd> twice in a row.

	<img src="./images/exit02.PNG" width="500">

    To close out of the terminal type `exit` and press enter.

*If for any reason you still don't have Anaconda functioning on your computer and you'd like to get it working, contact you instructor!*

<a id="anaconda-mac"></a>
##### Installing Anaconda for Mac
Instructions for downloading Anaconda (Python 3):

1. Go to the [Anaconda Download webpage:](https://www.anaconda.com/download/)

2. Use the `download` button  (or scroll until you see `Anaconda Installers`)

	<img src="./images_mac/anaconda_download_mac.png" width="500">

3. Download the current version of Python 3, you'll notice there is a "Graphical" and "Command Line" installer. This guide covers the Graphical, but feel free to use the Command Line if you wish.

4. After downloading, run the `Anaconda3` installer that popped into the dock (or you can open it from the `Downloads` folder as well).

	<img src="./images_mac/agree.png" width="500">

    Press the `Continue` button  

	<img src="./images_mac/welcome.png" width="500">

    Press the `Continue` button.   

	<img src="./images_mac/read.png" width="500">

    Press the `Continue` button.   

	<img src="./images_mac/license.png" width="500">
	
    Press the `Continue` button.

	<img src="./images_mac/license_agree.png" width="500">
	
    Press the `Agree` button.

	<img src="./images_mac/destination.png" width="500">
	
    You may notice that there is an error if you are running macOS Catalina or higher. We will want to change the destination for both the sake of macOS Catalina users, and those that are running macOS Mojave or sooner in case if you ever do update to macOS Catalina. Click on `Install on a specific disk...`
	
	<img src="./images_mac/drive.png" width="500">
    Make sure to click and select your main harddrive (You may only have one if no other storage device is connected to the compiter). Then click the `Choose Folder...` button.

	<img src="./images_mac/home.png" width="500">
    Then click on the `Users` -> `[YOUR_USERNAME]`. The `[YOUR_USERNAME]` should be the username of the account you are logged into. In my case this is `brandonmcintyre`. Then click in the bottom left hand corner on the `New Folder` button.

	<img src="./images_mac/new.png" width="500">
    You can enter any name you want for the folder as long as it does not have a space in it. For this tutorial we will use `me`. Then click `Create`.

	<img src="./images_mac/choose.png" width="500">
    If all went well the folder should be created and should be automatically selected. Now click the `Choose` button.

	<img src="./images_mac/cont.png" width="500">
	
    Press the `Continue` button.
<!--
    ```{image} ./images_mac/install.png
    :alt: install
    :width: 500
    ```
    Press the `Install` button.

    ```{image} ./images_mac/password.png
    :alt: password
    :width: 500
    ```
    Enter your password then click `Install Software`.  

    ```{image} ./images_mac/during.png
    :alt: during
    :width: 500
    ```
    This may take a moment to install.

    ```{image} ./images_mac/allow.png
    :alt: allow
    :width: 500
    ```
    Press `OK` button to allow.  

    ```{image} ./images_mac/pycharm.png
    :alt: pycharm
    :width: 500
    ```
    Press the `Continue` button.

    ```{image} ./images_mac/finished.png
    :alt: finished
    :width: 500
    ```
    Then press the `Close` button. Then to finish, press `Move to Trash` to delete the installer.  

5.  Open terminal on your computer by using Spotlight by pressing <kbd> command </kbd> + <kbd> space-bar </kbd> or simply use the search bar in the top right corner search `terminal` and press `Enter`. Then type `jupyter notebook` in the command line and hit enter.

    ```{image} ./images_mac/cmd_jupyter_mac.png
    :alt: cmd_jupyter_mac
    :width: 500
    ```   

    ```{image} ./images_mac/jup.png
    :alt: jup
    :width: 750
    ```
    This should launch a jupyter notebook tab on a web browser and the terminal should look like this.  

    ```{image} ./images_mac/jup_close.png
    :alt: jup_close
    :width: 500
    ```
    To exit jupyter notebook close the tab on the web browser, and go to the terminal window and type <kbd> control </kbd> + <kbd> c </kbd> twice in a row. Now you can close the terminal.   

*If for any reason you still don't have Anaconda functioning on your computer and you'd like to get it working, contact you instructor!*



---
## That's it! We look forward to seeing you in class!
-->