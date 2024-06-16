import subprocess

# Get the list of installed packages
pip_list = subprocess.check_output(['pip', 'list']).decode('utf-8')

# Display the list of packages and versions
print("List of installed packages and their versions:\n")
print(pip_list)

# Split the list into individual package names
package_names = [line.split(' ')[0] for line in pip_list.split('\n')[2:-1]]

# Confirmation for Uninstall
confirmation = input("\033[91mAre you sure you want to uninstall all pip packages?(yes/no):\033[0m ")

if confirmation.lower() == 'yes':
    # Uninstall each package
    for package in package_names:
        subprocess.call(['pip', 'uninstall', '-y', package])

    print("All pip packages have been uninstalled.\nThanks Rana Universe🍌🍌🍌")
else:
    print("No packages were uninstalled.\nRanaUniverse")
