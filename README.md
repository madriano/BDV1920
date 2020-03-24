
VISUALIZATION FOR BIG DATA
2019-20
Adriano Lopes

*****************************************************************************************
IMPORTANT
*****************************************************************************************

Before continuing to read this README file, check the labs slides about visualization 
in a web application

*****************************************************************************************
Setting up the application
*****************************************************************************************

1. Create a directory and put there the given application structure. Let us say the base directory of this application is BDVapp

2. Open a Terminal window and move to the directory BDVapp -> web

3. Initialize a virtual environment e.g. named env. Administrator privileges are required
to install virtualenv

$ pip3 install virtualenv

$ virtualenv –p python3 env

$ source env/bin/activate

If you are using Microsoft Windows, the activation command is:

$ env\Scripts\activate

First, a subdirectory env has been created inside airbnbApp and all files associated 
with the virtual environment will be inside it. Then the virtual environment is activated. 

When a virtual environment is activated, the location of its Python interpreter is added to the PATH environment variable in your current command session, which determines where to look for executable files. Notice that the activation command modifies your command prompt to include the name of the environment as:

(env) $

After a virtual environment is activated, typing commands will invoke the interpreter from 
the virtual environment instead of the system-wide interpreter. Having more than one Terminal window implies that we should activate the virtual environment in each of them.

To restore the PATH environment variable for the Terminal session and the command prompt to their original states, we should invoke:

(env) $ deactivate

4. Install the dependencies

If a requirements file exists e.g. requirements.txt we can install all the dependencies it relates to:

$ pip3 install –r requirements.txt

But if not, we have to install one by one, as follows:

(env) $ pip3 install flask
(env) $ pip3 install ....

You can check what packages are installed in the virtual environment at any time using the pip3 freeze command. Hence we can create the requirements file like:

(env) $ pip3 freeze > requirements.txt

*****************************************************************************************
Purpose and working of this web application
*****************************************************************************************

This application is an online data model web service using Spark and Flask

The structure is as follows:

TODO



*****************************************************************************************
FAQ
*****************************************************************************************

What problem does a virtual environment solve? 

The more Python projects you have, the more likely it is that you need to work with different versions of Python libraries, or even Python itself. Newer versions of libraries for one project can break compatibility in another project. Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages.

Why using a requirements file?

It is a good practice for applications to include a requirements file that records all the package dependencies, with the exact version numbers. This is important in case the virtual environment needs to be regenerated on a different machine, such as the machine on which the application will be deployed for production use. 

