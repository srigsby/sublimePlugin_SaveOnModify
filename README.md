move into the ~/.config/sublime-text-3/Packages/User directory

cd /home/$USER/.config/sublime-text-3/Packages/User


make a link to the plugins in this folder

ln -s /path/to/sublimePlugin_SaveOnModify/saveOnModify.py saveOnModify.py


thanks to [skuroda](https://stackoverflow.com/users/1852931/skuroda) and [this answer here](http://stackoverflow.com/a/15279948/2055586) for the basis of this here plugin.
