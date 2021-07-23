# SterenceqStranded
A small Point &amp; Click adventure project during the quarantimes.

--------------------
    Playing the Game
--------------------
User will ned pygame and PIL libraries.

Once installed, simply run:
>python3 main.py


--------------------
    Backgrounds
--------------------
All backgrounds should be kept in the ./background directory, and follow this naming convention:
   > lvl#
Background files should be stored in their cooresponding level. Files should be .png, and the left-most file should be named '0', and increment by 1.

--------------------
    Level Assets
--------------------
All level assets are organized, by level, in the ./level_asset directory. the follow this naming convention:
    >lvl#
Each lvl directoy is broken down into map# subdirectories.
These subdirectories contain the image files for each interactable object in a specific map.
map correlates to the background png files in the ./background directory. So map0 contains the assets for the 0.png backgorund file.

As of now, these assets are read by the main.py runner.  In order to display these assets, a dictionary must be created in main.py

This dictionary should follow this naming convention:
    >level_#{
}
where # refers to the level number.  ALL assets in the ./level_asset/map# directorys MUST HAVE an entry in this dictionary, or else the function that loads in the models will crash.
All assests must be present in the level_Asset directory and in this dictionary.

Dictionary entires should follow this convention:
> 'name_of_asset.png':(x,y)'
where x and y are the coordinates for the asset to be drawn on screen.

