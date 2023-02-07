This is a collection of schema files for all of the primary Data\ categories, excluding the directories with no xml files. This data was gathered by using a PowerShell script to load each of the xml files, blank out the values and then add any new unique nodes or attribues in the file to the root element "gameData". That root element is mine, not Proxy Studios' and has no reflection of the actual namespace used in Gladius.

These schema files can be loaded in an xml editor that supports tree view to get a collapsible view of all the nodes and attributes used in Gladius. The free version of Visual Studio or Notepad++ with the XML treeview plugin, can do this. With some effort it may be possible to get your xml editor to use these files to validate the xml in modded xml files. I haven't attempted to do so, not sure how cumbersome it might be. Additionally, in standard editor view mode some elements will have additional xml properties listed. For example many attributes list whether they are optional or required.

If anyone has any suggestions for improved formatting let me know and I'll consider it. If anyone would like the PowerShell script I'd be happy to share it, but it does require you have PowerShell and the .Net SDK installed (both free).

If you have any recommendations for improved or alterante formatting, let me know.

-Kurziel (discord: Kurziel#7212)