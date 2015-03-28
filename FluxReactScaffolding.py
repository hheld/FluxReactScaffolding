import os
import tarfile
import fileinput


# options ##############################################################################################################
appName = 'My test app'
appPath = '.'
appAuthor = 'Harald Held'
webTitle = 'Testing'
appDescription = 'Testing my template generator'
appKeyword = 'Scaffolding'
appLicense = 'ISC'
########################################################################################################################

# extract template archive to specified output folder, i.e. appPath/appName ############################################
template = 'FluxReactProjectTemplate.tgz'
outputPath = os.path.join(appPath, appName.replace(' ', '_'))

def files(members):
    for tarinfo in members:
        tarinfo.name = tarinfo.name.replace('FluxReactProjectTemplate/', '')
        yield tarinfo

tar = tarfile.open(template, 'r')
tar.extractall(path=outputPath, members=files(tar))

# substitute template values in index.html #############################################################################
for line in fileinput.input(os.path.join(outputPath, 'index.html'), inplace=True):
    print(line.replace('%TITLE%', webTitle), end='')
########################################################################################################################

# substitute template values in package.json ###########################################################################
for line in fileinput.input(os.path.join(outputPath, 'package.json'), inplace=True):
    print(line.replace('%APPNAME%', appName.replace(' ', '_'))
              .replace('%DESCRIPTION%', appDescription)
              .replace('%KEYWORD%', appKeyword)
              .replace('%AUTHOR%', appAuthor)
              .replace('%LICENSE%', appLicense), end='')
########################################################################################################################
