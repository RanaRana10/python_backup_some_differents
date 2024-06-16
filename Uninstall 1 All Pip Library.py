import subprocess

#ist of installed packages in Your PC By RanaUniverse https://t.me/RanaUniverse
pip_list = subprocess.check_output(['pip', 'list']).decode('utf-8')

# Split the list into individual package names
package_names = [line.split(' ')[0] for line in pip_list.split('\n')[2:-1]]

# Confirmation for Uninstall
confirmation = input("Are you sure you want to uninstall all pip packages? (yes/no): ")

if confirmation.lower() == 'yes':
    # Uninstall each package
    for package in package_names:
        subprocess.call(['pip', 'uninstall', '-y', package])

    print("All pip packages have been uninstalled.\nThanks Rana Universe🍌🍌🍌")
else:
    print("No packages were uninstalled.")
