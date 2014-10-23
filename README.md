# Warehouse Order Tracking System

## Overview
I used to sell a lot on eBay (10 000+ orders a month!), and occasionally we would receive an email stating that the wrong item or quantity had been sent. This occurs naturally in the course of business and is easily rectified. However, I was sitting at my desk reading my emails when one customer claimed to have been sent the wrong item - I knew this was false as the day before it was I who sorted the order. So I made this system, originally in Bash on Linux, to record each item being packed, visually, and store it in a database, so that should a claim coming in that looks untrue I could simply check on the system. It got used for each order and was successful. This all ran on Raspberry Pis, so was pretty economical.

The system then got extended to include picking and packing information (eg. who picked/packed the order and at what time), tracking information (for Yodel and Royal Mail), and an alarm which goes off should a duplicate order be attempted to be picked/packed (this was because of an error in eBay's own system resulting in dispatched orders going back on to my 'Awaiting Dispatch' page - something of a nightmare that was!).

I've not added any of the main server-side stuff here, but basically aside from each of the files on here there was a small cheap MySQL database server (running Debian I believe..). Should anyone want the SQL structure for this, let me know and I'll fire up the old server and grab it off there.

## Requirements
These scripts were run on Raspberry Pis running Raspbian (the RPi Debian Fork), howeevr they should run on any GNU/Linux system as far as I'm aware, as long as Python3 is installed (it should be available in the repos for the main distributions).

## Licence
The entire contents of this repository is licenced under the GNU General Public License v3 unless otherwise specified. Basically you can use this for whatever purposes you would like to as long as you credit the work to me (generally a little note somewhere readable referencing `Elliot J. Reed, www.cyanidesystems.com` will do). Should you make any changes you must publish these in a prominent place such as GitHub, Sourceforge, etc. It would also be nice, though not required, if you were to let me know of any changes, as I may have missed something and could use the changes / edits myself.

```
Copyright (C) 2014  Elliot J. Reed

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see [<http://www.gnu.org/licenses/>](http://www.gnu.org/licenses/).
```
