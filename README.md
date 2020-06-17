# smartpad-tester

## preface
*DISCLAIMER: use info here at your own risk, it might open a black hole or worse. Unfinished work. And i don't know Python :)*

*RECOMMEND TO UPDATE TO v0.15 firmware:* http://www.midiplus.com.tw/MIDIPLUS-Download.files/Firmware%20update/SmartPAD%20Firmware%20Update%20V0.15%2020171103.zip
V0.15 fixes multicolor leds over midi!

Alternative firmwares:
* https://github.com/DerFetzer/open-cleverpad
* https://github.com/TheKikGen/kikpad

## Intro
This repo collects information about the MidiPLUS Smartpad Midicontroller as eg available at Amazon:
https://www.amazon.com/midiplus-Smartpad-USB-MIDI-Controller/dp/B00WU6FDNG

Not much info is available for this device. So i decided to try to reverse-engineer and collect findings here.

* which MIDI data can it send by pushing buttons, turning the encoders.
* which MIDI data can it receive to color the LEDS.
* software used to reverse-engineer the above.


OPEN QUESTIONS:
* whatis the difference between the 2(?) firmware versions?
   * how hackable is the firmware?
   * translated: https://translate.google.nl/translate?sl=auto&tl=en&js=y&prev=_t&hl=en&ie=UTF-8&u=https%3A%2F%2Fwww.nightclubber.com.ar%2Fforo%2F162%2Fhardware-djs-and-productores%2F356629%2Fmidiplus-smartpad.html&edit-text=
* do the left- and bottom button rows really never send midi?
   * eg the cursorkeys don't seem to do anything (with this firmware?)
   * see https://github.com/s0len0id/smartpad-tester/blob/master/notes/amazon-review.txt for Ableton-mode sysex
* is there a special mode by holding a button pressed while powering-up?
* does it respond to eg controlchange, other midi?
