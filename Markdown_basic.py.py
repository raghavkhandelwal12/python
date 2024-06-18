#!/usr/bin/env python
# coding: utf-8

# # Heading level1
# i really like using markdown.to add the new line we space the one blank line 
# 
# i think i'll use it to format all of my document from now on

# <h1>Heading level 1</h1>

# # heading

# ## to create the heading level 2

# 

# ### createt he heading level 3

# #### create the heading level 4

# ##### create th heading level 5

# ###### create the heading level 6

#  alternate syntax this is for the heading 1
#  =================================
#  
#  alternatively on the line below the text add any number of == character for heading level 1
#  
#  
#  
#  

# alternate syntax for the heading 2
# ----------------------------------
# alternatively ,on the line below the text add any number of  -----character for heading level 2

# # heading best practices
# markdown application don't agree on how to handle missing space between sign(#) and the heading name.For compatiablility always put a space between the numbers signs and the heading name
# 

# # here's a heading
# provide the space when we add the heading

# In[32]:


# Don't allow
#in markdown not allow the without space for the heading


# # we should also put blank lines before and after a heading for compatiability

# 
# Try to put a blank line before...
# 
# # heading
# 
# ...and after a heading

# try to put blank line before
# 
# # heading
# 
# after a heading

# # Paragraphs
# to create paragraphs,use a blank line  to separate one or more lines of text

# 
# 
# i really like using markdown
# 
# i think i'll use it to format all of my document from now on

# # Html using 
# <p>I really like using markdown.</p>
# 
# <p>I think I'll use it to format all of documents from now on.</p>

# # paragraph best practice
# unless the paragraph in a list dont't indent paragraph withs spaces or tabs

# # we can do this
# Don't put tabs or spaces in front  of you paragaph
# 
# keep lines left-aligned like this
# 

# # we Don't do this
#     this can result in unexpected formatting problem
#     
#     don't add tabs or spaces in front end of the paragraphs

# # Line breaks
# to create a line break or new line(<br>),end a line with two or more spaces,and then type return

# # html using
# 
# <p>this is the first line.<br>and this is the second line.</p>

# # line break best practice
# 

# # We can do this
# first line with two spaces after.
# and the next line
# 
# first line with the html tage after.<br>
# and the next line

# # we don't do this
# first line with a backslash after. \
# this is nice for the human.\
# And the next line
# 
# first line with nothing after.
# and the next line

# # Emphasis 
# you can add emphasis  by making text or italic

# # bold
# to bold text,add two asterisks or underscores before and after a word and a phrase.\
# to bold the middle of the word for emphasis,add two asterisk without spaces around the letters

# i just love **bold text**

# i just love __bold text__

# Love **is** bold

# # Html using bold
# 

# i just love <strong> and the text </strong>
# 
# i just love <strong>bold text </strong>

# # Bold best practice
# love**is**bold
# 
# 

# # we dont do this
# love__is__bold

# # italic
# to itaclize text,add one aterisk or underscore before and after a word or phrase.To italicize the middle of a word for emphasis ,add one astersik without spaces around letters
# 

# # to italic this we use the following in the markdown
# 
# Italicized text is the *cat's meow*
# 
# Italicized text is the _cat's meow_'
# 
# A*cat*meow

# # USING THE HTML ITALIC
# 
# Italicized text is the <em>cat's meow>/em>
#     
# a<em>cat</em>meow

# # ITALIC BEST PRACTICE
# A*cat*meow
# 
# 

# # we cant do this
# a_cat_meow

# # Bold and italic
# to emphasize text with bold and italic at the same itme,add three asterisk or underscores before and after the word or phrase.To bold and itaclize the middle of word for emphasis,add three astersik without spaces around the letters
# 

# # Markdown
# this test is ***really important***
# 
# this text is ___really important___
# 
# this text is __*really important*__
# 
# this text is **_really important_**
# 
# this is
# really***very***important text
# 

# # HTML USING THE BOLD AND ITALIC
# this text is <em><strong>really important </strong></em>

# # bold and italic best practice
# this is  rally***very***important 
# text

# # we don't do this bold and italic
# 
# this is
# really___very___important
# text

# # Blockquotes
# 
# to create a blockquotes ,add a >in front of a paragraph
# 
# 

# > Dorothy followed her through many of the beautiful rooms in his castle.

# # Blockquotes with multiple paragraphs
# Bloackquotes can contain multiple paragraphs,add a > on the blank line between the paragraph

# > Doorthy followed her through many beautiful rooms in his castle
# >
# > the witch bade his clean the pots and kattles and sweep the floor and keep the fire fed with wood

# # Nested blockquotes
# 
# Blockquotes can be nested add a >> in front of the paragraph you want to nest

# >Dorothy followd her through many of the beautiful room in his castle
# >
# >>the witch bade her clean the pots and kattles and sweep the floor and keep the fite fed with food

# # Blockquotes with other elements
# Blockquotes can contain other markdown formatted element.Not all element can be used-you'll need to experiment to see which means work

# > ### the quartely result look great
# >
# > - Revenue was off the cart/
# > -profits were higher than ever.
# >
# > *Everything is going to according to **plan**
# >
# - hi my name is raghav
# 
# 

# # Blockquotes best practices
# for compatiabiltiy ,put blank lines before and after blockquotes
# 
# 

# # do this
# try to put a blank line
# before...
# 
# > this is a blockquotes
# 
# ...and after a blockquotes

# # don't do this
# without blank lines, this might not look right
# >this is a blockquotes
# don't do this
# >
# is very beautiful

# # list
# we can oragnize items into ordered and unordered lists.
# 

# # Markdown
# 1. first item
# 2. second item
# 3. third item
# 4. fouth item

# 1. first item
# 1. second item
# 1. third item
# 1. fourth item

# 1. first item
# 8. second item
# 10. third item
# 11. fourth item

# 1. first item
# 2. second item
# 3. third item
#     1. 
#     indented items
#     2.
#     indented item
# 4. fourth item

# # using the html
# <ol>
#     <li>first item</li>
#     <li>second
#     item</li>
#     <li>third item</li>
#     <li>fourth</li>
# </ol>

# <ol>
#     <li>first item</li>
#     <li>second item</li>
#     <li>third item</li>
# </ol>

# <ol>
#     <li>first item</li>
#     <li>second item</li>
#     <li>third item
#         <ol>
#             <li>indented item</li>
#             <li>indented item</li>
#         </ol>
#     </li>
#     <li>fourth item</li>
# </ol>
#         

# # ordered list best practice
# # do this
# 1. first item
# 2. second item

# 

# 1) first item
# 2) second item

# # unordered list
# to create an unordered list,add dashes(-),asterisk(*) or plus signs(+) in front of line items.Indent one or more items to created a nested list

# # markdown
# - first item
# - second item
# - third item
# - fourth item
# 

# * first item
# * second item
# * third item
# * fourth item

# + first item
# + second item
# + third item
# + fourth item

# - first item
# - second item
# - third item
#     -
#  indented item
#     -
#  
#  
#  
#  indented item
# - fourth item

# # using html to create the unordered list
# 
# <ul>
#     <li>first item</li>
#     <li>second item</li>
#     <li>third item</li>
#     <li>fourth item</li>
# </ul>

# <ul>
#     <li>first item</li>
#     <li>second item</li>
#     <li>third item</li>
#         <ul>
#             <li>indented item</li>
#             <li>indented item</li>
#         </ul>
#     <li>fourth item</li>
# </ul>

# # starting unordered list items with numbers
# if we need to start an unordered list item with a number followed by a period we can use the backslash(/) escape period
# 

# - 1968\.a great year
# - i think 1969 was second best

# # Adding element in this list
# to add another element in a list while preserving the continuity of the list,indent the elements four spaces or one tab 

# * this is the first list item.
# * here's the second list items
#      
#      I need to add another paragraph below the second list item
#      
# *and here's the third list item

# # using blockquotes to add the list
# 
# * this is the first list items
# * here's the second list items
#     
#     >a blcoquotes would look great below the second list items
#     
# * and here's the third list items

# # code blocks 
# code blocks are normally indented four spaces or one tab. when they're in list,indent them eight spaces or two tabs
# 

# 1. open the file
# 2. find the following code block on line 21:
# 
#         <html>
#             <head>
#                 <title>test</title>
#             </head>
#     
#     
# 3. update the title to match the name of your website

# # images

# 1. open the file containing the linux mascot
# 2. Marvel at its beauty
# 
#     ![Tux, the Linux mascot](/assets/images/C:\Users\pc\Downloads\tux.avif)
# 
# 3. close the file

# # lists
# we can nest an unordered list in an ordered list or vice versa
# 

# 1. first item
# 2. second item
# 3. third item
# 
#     - indented item
#     
#     - indented item
#     
# 4. fourth item
# 

# # code 
# to denote a word or phrase a code , enclose it in bacticks()
# 

# # Markdown
# at the command
# promt, type
# 'nano' .

# # html
# At the command promt,
# type <code>nano</code>

# # Escaping Backticks
# if the word or phrase we wan t to denote as code includes one or more backticks, we can escape it by enclosing the word or phrase in double backticks('')
# 

# ``Use `code` in
# your markdown
# file.``
# 

# # html
# <code>use `code` in 
#  your markdown file.
# </code>

# # CODE Blocks
# to create code blocks,indent every line of the block by at least four spaces or one tab
# 

#         <html>
#             <head>
#             </head>
#         </html>

# # horizontal rules
# to create a horizontal rules,use three or more asterisk(***),dashes(---), or underscore(___) or a line by  themselves
# 
# 

# ***
# 
# ---

# # horizontal rules best practice
# 
# try to put a blank line
# before...
# 
# ***
# 
# and this is very nice
# 
# ---
# 
# ...and after a horizontal rule

# # links
# to create a link,enclose the link text in brackets(e.g[Duck Duck Go])and then follow it immediately with the url in parenthesis 
# 
# 

# my favoriate search engine is [Duck Duck Go](https://duckduckgo.com)

# # Adding titles
# To add a title ,enclose it in quotation marks after  the url
# 

# my favoriate search engine is [Duck Duck Go](https:duckduckgo.com "The best search engine for privacyy")

# # url and email address
# to quickly turn a url or email address into a link,enclose it in single brackets
# 

# <https://www.google.com>
# 
# <ram456@gmail.com>

# # images
# to add an image add an exclamation mark(!) followed by alt text in brackets

# ![The San Juan Mountains are beautiful!](![Tux Image](C:/Users/pc/Downloads/tux.png)
#  "San Juan Mountains")

# # linking image
# to add a link to an image ,enclose the markdown for the image in brackets
# 

# In[82]:


[![An old rock in the desert](/assets/images/shiprock.jpg "Shiprock, New Mexico by Beau Rogers")](https://www.flickr.com/photos/beaurogers/31833779864/in/photolist-Qv3rFw-34mt9F-a9Cmfy-5Ha3Zi-9msKdv-o3hgjr-hWpUte-4WMsJ1-KUQ8N-deshUb-vssBD-6CQci6-8AFCiD-zsJWT-nNfsgB-dPDwZJ-bn9JGn-5HtSXY-6CUhAL-a4UTXB-ugPum-KUPSo-fBLNm-6CUmpy-4WMsc9-8a7D3T-83KJev-6CQ2bK-nNusHJ-a78rQH-nw3NvT-7aq2qf-8wwBso-3nNceh-ugSKP-4mh4kh-bbeeqH-a7biME-q3PtTf-brFpgb-cg38zw-bXMZc-nJPELD-f58Lmo-bXMYG-bz8AAi-bxNtNT-bXMYi-bXMY6-bXMYv)


# 

# # escaping character
# to display a literal character that would otherwise be used to format text in markdown document
# add a backslash  in front of the character
# 
# \* without the backslash,thar would be bullet in unordered list
# 
# \[] without the backslash,thar would be bullet in unordered list
# 
# \() without the backslash,thar would be bullet in unordered list
# 
# \. without the backslash,thar would be bullet in unordered list
# 
# \| without the backslash,thar would be bullet in unordered list
# 
# \<> without the backslash,thar would be bullet in unordered list

# In[ ]:




