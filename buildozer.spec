[app]

# (str) Title of your application
title = Aplicatia Mea

# (str) Package name
package.name = aplicatiamea

# (str) Package domain (needed for android packaging)
package.domain = org.test

# (str) Source directory where the application files are located
source.dir = .

# (str) Application version
version = 0.1

# (str) Android target API, should be as high as possible.
android.api = 33

# (str) Minimum API your APK will support.
android.minapi = 21

# (bool) Indicate if the application should accept Android SDK license agreement
android.accept_sdk_license = True

# (list) Source files to include (let it include python files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
requirements = python3,kivy

# (str) Supported orientations (landscape, portrait or all)
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

[buildozer]

# (int) Log level (0 = error, 1 = info, 2 = debug (with command output))
log_level = 2
