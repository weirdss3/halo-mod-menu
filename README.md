Do not skid without perms!
halo.lol.py → This is your main Python script. (The name is a little funky with the double dots, but it should still run.)

halo_lol.pyproj & halo_lol.sln → Visual Studio project files

.gitignore, LICENSE, README.md → Not needed to run the code

✅ Option 1: Run It Using Visual Studio (Recommended if you're using Windows)
Open Visual Studio

Go to:
File > Open > Project/Solution

Choose halo_lol.sln

Let it load the project

Press F5 or click the green Start button to run it

🔧 If Visual Studio asks you to install the Python workload, let it do that — it's necessary for running Python projects in VS.

✅ Option 2: Run It From the Command Line / Terminal
Make sure Python is installed
Check by running:

bash
Copy
Edit
python --version
or

bash
Copy
Edit
python3 --version
Navigate to your project directory:

bash
Copy
Edit
cd path/to/project-folder
Run the script: Because of the filename halo.lol.py, use quotes:

bash
Copy
Edit
python "halo.lol.py"
or if you're on macOS/Linux or using python3:

bash
Copy
Edit
python3 "halo.lol.py"
⚠️ Quick Tip:
If the script uses any external libraries like pygame, tkinter, or anything else, you might need to install them first with:

bash
Copy
Edit
pip install <library-name>
