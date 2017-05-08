# smartpad-tester

*DISCLAIMER: use info here at your own risk, it might open a black hole or worse. Unfinished work. And i don't know Python :)*

This repo collects information about the Smartpad Midicontroller as eg available at Amazon:
https://www.amazon.com/midiplus-Smartpad-USB-MIDI-Controller/dp/B00WU6FDNG

Not much info is available for this device. So i decided to try to reverse-engineer and collect findings here.

* which MIDI data can it send by pushing buttons, turning the encoders.
* which MIDI data can it receive to color the LEDS.
* software used to reverse-engineer the above.

OPEN QUESTIONS:
* leds can't be turned off via midi?
* the purple-pad color, is it a bug?
* whatis the difference between the 2(?) firmware versions?
   * how hackable is the firmware?
   * translated: https://translate.google.nl/translate?sl=auto&tl=en&js=y&prev=_t&hl=en&ie=UTF-8&u=https%3A%2F%2Fwww.nightclubber.com.ar%2Fforo%2F162%2Fhardware-djs-and-productores%2F356629%2Fmidiplus-smartpad.html&edit-text=
* do the left- and bottom button rows really never send midi?
* is there a special mode by holding a button pressed while powering-up?
