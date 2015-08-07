#!/bin/bash

create_page() {
	if [ -f "$1.html" ]
	then
		rm "$1.html"
	fi
	
	cat head.html >> "$1.html"
	
	echo "<nav>" >> "$1.html"
	markdown "$1_nav.md" >> "$1.html"
	echo "</nav>" >> "$1.html"
	
	echo "<div id='section-wrap'>" >> "$1.html"
	
	echo "<aside>" >> "$1.html"
	markdown aside.md >> "$1.html"
	echo "</aside>" >> "$1.html"
	
	echo "<section>" >> "$1.html"
	markdown "$1_section.md" >> "$1.html"
	echo "</section>" >> "$1.html"
	
	#end section-wrap
	echo "</div>" >> "$1.html"
	
	cat foot.html >> "$1.html"
}

create_page index
create_page research
