# OctoPrint-Helloworld

**TODO:** Describe what your plugin does.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)
or manually using this URL:

    https://github.com/tomekd85/OctoPrint-Helloworld/archive/master.zip

**TODO:** Describe how to install your plugin, if more needs to be done than just installing it via pip or through
the plugin manager.

## Configuration

**TODO:** Describe your plugin's configuration options (if any).

Fire Alarm Module -> Listener activated when alarm is raised ->

- Sent signal notification
- Create event in OctoPrint - how to do this ?
  - from octoprint.events import eventManager
  - eventManager().fire(event, payload)
- Handle event in octoPrint with [octoprint.events.register_custom_events hook](https://docs.octoprint.org/en/master/plugins/hooks.html#sec-plugins-hook-events-register-custom-events)
- Try to connect this new event handling to OctoApp
- Sent notification to Signal App

Check if OptoEverywhere works fine !!!
Other
