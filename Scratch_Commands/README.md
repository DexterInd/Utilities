To create or adjust this image:

1. run Scratch on the Pi and arrange your block sequence, one sequence at a time. Right click and *save picture of script*
2. put all individuals images into the appropriate robot folder.
3. manually edit scratch_commands.json for that particular robot. You are in charge of choosing what goes into which column. You can change the number of columns if you want.
4. since json is not meant to be edited by humans, it ended up being a poor choice but it does work. Run your newly edited json through http://jsonlint.com/
5. run generateScratchCommands.py <robot>  (ie. generateScratchCommands.py gopigo) to generate the SVG for that robot
6. visualize the svg in a browser, and do a screencap to get a jpg or a png as you wish.

Cheap and dirty way of not having to deal with block alignment and allowing future changes
