## fm3chanic Color Schemes

This repo is a collection of HTML files containing color schemes for text editors / terminal applications made by me. The HTML files work as visual reference sheets as well as data source to automatically built themes based on a template. Therefore format and base information is fix.<br>
Color schemes which have been created during my project of color theming Vtubers will be in the directory called "vtuber_project". Color schemes which were created outside this project will be in the directory "other".

**[Vtuber Project | Information & Galery](https://github.com/fm3chanic/vtuber_project)**<br>
**[Galery of Non-Project Themes](/doc/galery.md)**<br>
**[Supported Applications](/doc/applications.md)**

### Tools & Workflow (HTML files)

If you want to create your own themes with the tools in the repositories, your are welcome to do so (but it makes me happy if my name is mentioned somewhere of course).<br>
Just note that the tools are not very well documented (check the comments in the python scripts) and the scripts have no error handling at all. I would not touch them, if you don't know at least a bit about python.<br><br>

**How does it work?**<br><br>
You fill in the colors in the color_scheme_template.html and name the theme file as well as change the header in the file. After doing so I recommend running the test_load_colors.py (it targets the color_test_template.html) and ensure readability and look.<br>

The color_adjustment.py contains some base values (saturation & brightness, based on hls) for each of the different color types, which work for light or dark themes, so if you just want
your colors in a working theme, run this (it targets every html in a directory, changes the values and wants to write it in a subdirectory "reworked").<br>

### Contribution

The themes are based on the mapped templates in the **/tools** directory of the application repos.<br>
The python script (_\[...\]\_load_colors.py_) reads the colors from a html file from this repo and uses replace to fill in the colors.<br>

If you want to work on colors it makes the most sense to change the colors in the html file in this repository so the changes can be applied to all applications using the theme.<br>
If you want to work on the mapping of the colors it might make sense to change the base template in the application repository, so changes can be applied to all themes of an application.<br>

The only exception of this is the gruber-darker theme, which does not follow this standard for text editors only for terminals.<br><br>
Neverless, **I also welcome contribution not following this standard** in the application repositories. The standard was made to keep it maintainable for one person, not to block community ideas.<br>