import os
l = "automate callback chooser timer commands essential importers markups prayertime replyer"
l = l.split()
text = ''

for x in l:
    text += f'{x}/__pycache__/\* '
if os.path.isfile('bot.zip'):
    os.remove('bot.zip')
os.system(f'zip -r bot.zip timer automate callback chooser commands essential importers markups prayertime replyer bot.py __init__.py main.py zipper.py هام_جدا_README.TXT -x {text}')
print('bot.zip is done')

if os.path.isfile('all.zip'):
    os.remove('all.zip')

os.system(f'zip -r all.zip * .env -x {text} bot.zip')
print('all.zip is done')
