#!/bin/sh
# Copyright (C) 2000 Idan Shoham <idan@m-tech.ab.ca> 
#               2002 Sebastian Zagrodzki <s.zagrodzki@net.icm.edu.pl>
#  
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2 of the License, or
# (at your option) any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software 
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

# get bounding box (only works because we know there is only 1 such comment)
read llx lly urx ury << EOF
`awk '$1=="%%BoundingBox:"{print $2,$3,$4,$5}' < "$1.eps"`
EOF

height="$(( $ury - $lly ))"
width="$(( $urx - $llx ))"

epsffit 0 0 $width $height "$1.eps" "$1.epstemp"

gs -q -dNOPAUSE -sDEVICE=pgm -sOutputFile="$1.pgm" -g"${width}x${height}" \
 "$1.epstemp" quit.ps
rm -f "$1.epstemp"

pnmtopng -interlace "$1.pgm" > "$1.png" 2>/dev/null
rm -f "$1.pgm"
