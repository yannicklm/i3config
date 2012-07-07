i3 configuration
=================

i3 configuration for the `i3 window manager <http://i3wm.org/>`_

Setup
-----

Requirements:

  - Python
  - i3-py : https://github.com/ziberna/i3-py
  - dmenu

::

  $ git clone ..../i3config.git ~/src/i3config
  $ ln -s ~/src/i3config .i3

Usage
-----

* Mod+t: go to or create a new named workspace
* Mod+Shit+t: move current window to named workspace, creating
  it if necessary

* Mod+<num>: go to workspace number <num>

Note there are no way to create non-named workspaces.

A few hooks try to keep the workspace list sorted.
