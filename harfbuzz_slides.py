#!/usr/bin/python
# -*- coding:utf8 -*-

if __name__ == "__main__":
	import slippy
	import sys
	import harfbuzz_theme
	slippy.main (__file__, harfbuzz_theme, sys.argv[1:])
	sys.exit (0)

# Copyright 2007,2009 Behdad Esfahbod <besfahbo@redhat.com>

# A slides file should populate the variable slides with
# a list of tuples.  Each tuple should have:
#
#	- Slide content
#	- User data
#	- Canvas width
#	- Canvas height
#
# Slide content can be a string, a list of strings,
# a function returning one of those, or a generator
# yielding strings.  The user data should be a dictionary or
# None, and is both used to communicate options to the
# renderer and to pass extra options to the theme functions.
#
# A function-based slide content will be passed a renderer object.
# Renderer is an object similar to a cairo.Context and
# pangocairo.CairoContext but has its own methods too.
# The more useful of them here are put_text, put_image, and
# set_allocation.  See their pydocs.

slides = []
def slide_add(f, data=None, width=800, height=600):
	#slides[:0] = [(f, data, width, height)]
	slides.append ((f, data, width, height))
	return f

import pango, pangocairo, cairo, os, signal

# We use slide data to tell the theme who's speaking.
# That is, which side the bubble should point to.
behdad = -1
whois = None
def who(name):
	global whois
	whois = name
# And convenience functions to add a slide.  Can be
# used as a function decorator, or called directly.
def slide_who(f, who, data=None):
	if data:
		data = dict (data)
	else:
		data = {}
	data['who'] = who
	return slide_add (f, data)
def slide(f, data=None):
	return slide_who (f, whois, data=data)
def slide_noone(f, data=None):
	return slide_who (f, None, data=data)
def slide_behdad(f, data=None):
	return slide_who (f, behdad, data=data)
def slide_image (f, height=650, data=None):
	@slide_noone
	def image_func (r):
		r.move_to (400, 300)
		r.put_image (f, height=height)
		#r.set_allocation (000, 0, 800, 600)
		yield ""

#
# Slides start here
#

@slide_noone
def title_slide (r):
	r.move_to (800, 30)
	r.put_text (
"""<b>HarfBuzz</b>\nthe Free and Open\nShaping Engine""",
width=800, height=500, valign=1, halign=-1)

	r.move_to (0, 570)
	r.put_text ("""Behdad Esfahbod\n<span font_desc="monospace">behdad@redhat.com\nhttp://behdad.org/\nhttp://freedesktop.org/wiki/Software/HarfBuzz</span>""", height=130, halign=1, valign=-1)


who (behdad)

def list_slide (l, data=None):
	def s (r):
		return '\n'.join (l)
		#yield l[0]
		#for i in l[1:]:
		#	yield '\n'+i
	s.__name__ = l[0]
	slide (s, data)

list_slide ([
		"<b>Agenda</b>",
		"??? Introduction",
		"??? History",
		"??? Old HarfBuzz",
		"??? New HarfBuzz",
		"??? Scope",
		"??? Design",
		"??? Status",
		"??? Roadmap",
	    ], data={'align': pango.ALIGN_LEFT})

slide_noone("<b>Intro</b>")
slide("<span font_desc=\"IranNastaliq\">	?????? ??????	</span>")
slide("Free and Open\nUnicode\nShaping Engine")

slide_noone("<b>History</b>")
slide("FreeType\nOpenType\nLayout")
slide("GNOME\nKDE")
slide("Pango\nQt")

slide_noone("<b>Old\nHarfBuzz</b>")
slide("2006")
slide("Qt\nShapers")
list_slide([	"<b>Problems</b>",
		"??? Inefficient",
		"??? Fragile",
		"??? Ugly",
	   ], data={'align': pango.ALIGN_LEFT})

slide_noone("<b>New\nHarfBuzz</b>")
slide("Baking")

slide_noone("<b>Scope</b>")
list_slide([	"<b>Generic Shaper</b>",
		"??? OpenType",
		"??? ATT",
		"??? Graphite",
		"??? Fallback",
		"??? ...",
	   ], data={'align': pango.ALIGN_LEFT})
list_slide([	"<b>Just Shaper</b>",
		"??? No Itemizer",
		"??? No Bidi",
		"??? No Line Breaking",
		"??? No Rasterization",
	   ], data={'align': pango.ALIGN_LEFT})
list_slide([	"<b>Goals</b>",
		"??? Beautiful",
		"??? Robust",
		"??? Flexible",
		"??? Efficient",
		"??? Portable",
	   ], data={'align': pango.ALIGN_LEFT})
list_slide ([	"<b>Consumers</b>",
		"??? GUI Toolkits",
		"??? Web Browsers",
		"??? Word Processors",
		"??? Designer Tools",
		"??? Font Design Tools",
		"??? Terminal Emulators",
		"??? Batch Doc Processors",
		"??? TeX Engines",
	    ], data={'align': pango.ALIGN_LEFT})

slide_noone("<b>Design</b>")
slide("<b>For Humans</b>\n<small>hb_face_t\nhb_font_t\nhb_buffer_t</small>")
slide("Unicode\nCallbacks")
slide("Font\nCallbacks")
slide("SFNT-\nBased")
slide("Garbage-In\nGlyphs-Out")
slide("Fallbacks")
slide("In-Place")
slide("Error\nHandling")
slide("Backend-\nIndependent")
slide("Backend\nAPI")
slide("Thread-\nSafe")
slide("No\nDependencies")
slide("Well\nSome C++")
slide("MIT-\nLicensed")
list_slide ([	"<b>OpenType 1.6</b>",
		"??? Mark filtering sets",
		"??? cmap type 14",
		"??? Mirroring",
	    ], data={'align': pango.ALIGN_LEFT})

slide_noone("<b>Status</b>")
slide("OpenType\nLayout")
slide("API\nReview")
slide("Shapers")
slide("Test\nSuite")


"""
list_slide ([	"<b></b>",
		"??? ",
		"??? ",
		"??? ",
		"??? ",
		"??? ",
		"??? ",
	    ], data={'align': pango.ALIGN_LEFT})
"""

@slide
def where_is_my_vote (r):
	r.move_to (400, 300)
	r.put_image ("IgreenNY.jpg", height=1024)
	return ""

slide_noone("Q?")
