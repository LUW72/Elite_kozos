from time import sleep
import screen
from travel_logic import Planet_travel
import os

def location_calc(location):
    if location == 0:
        return "In Space"
    if location == 1:
        return "Thorodin"
    if location == 2:
        return "Ydalir  "
    if location == 3:
        return "Vidar   "
    if location == 4:
        return "Folkvang"

def header(location:str):
    print(f"""
┌────────────────────────────────────────────┬────────────────────────────────────┐
│ Your ship's location                       │                          {location}  │   
└────────────────────────────────────────────┴────────────────────────────────────┘""")




def alapkepernyo():
    sleep(1)
    ascii_art = r"""
                        . ___
                        __,' __`.                _..----....____
            __...--.'``;.   ,.   ;``--..__     .'    ,-._    _.-'
      _..-''-------'   `'   `'   `'     O ``-''._   (,;') _,'
    ,'________________                          \`-._`-',' 
     `._              ```````````------...___   '-.._'-: 
        ```--.._      ,.                     ````--...__\-. 
                `.--. `-`                       ____    |  |` 
                  `. `.                       ,'`````.  ;  ;` 
                    `._`.        __________   `.      \'__/` 
                       `-:._____/______/___/____`.     \  ` 
                                   |       `._    `.    \ 
                                   `._________`-.   `.   `.___ 
                                                 SSt  `------'`
    """
    print(ascii_art)

def ydalir():
    sleep(1)
    ascii_art = r"""    o               .        ___---___                    .                   
       .              .--\        --.     .     .         .
                    ./.;_.\     __/~ \.     
                   /;  / `-'  __\    . \                            
 .        .       / ,--'     / .   .;   \        |
                 | .|       /       __   |      -O-       .
                |__/    __ |  . ;   \ | . |      |
                |      /  \\_    . ;| \___|    
   .    o       |      \  .~\\___,--'     |           .
                 |     | . ; ~~~~\_    __|
    |             \    \   .  .  ; \  /_/   .
   -O-        .    \   /         . |  ~/                  .
    |    .          ~\ \   .      /  /~          o
  .                   ~--___ ; ___--~       
                 .          ---         .              -JT"""
    print(ascii_art)

def vidar():
    sleep(1)
    ascii_art = r"""                .                                            .
     *   .                  .              .        .   *          .
  .         .                     .       .           .      .        .
        o                             .                   .
         .              .                  .           .
          0     .
                 .          .                 ,                ,    ,
 .          \          .                         .
      .      \   ,
   .          o     .                 .                   .            .
     .         \                 ,             .                .
               #\##\#      .                              .        .
             #  #O##\###                .                        .
   .        #*#  #\##\###                       .                     ,
        .   ##*#  #\##\##               .                     .
      .      ##*#  #o##\#         .                             ,       .
          .     *#  #\#     .                    .             .          ,
                      \          .                         .
____^/\___^--____/\____O______________/\/\---/\___________---______________
   /\^   ^  ^    ^                  ^^ ^  '\ ^          ^       ---
         --           -            --  -      -         ---  __       ^
   --  __                      ___--  ^  ^                         --  __
"""

    print(ascii_art)

def thorodin():
    sleep(1)
    ascii_art = r"""              __...----...__
           .-' -=;::;::`;:::`-.
        .-'"; `-;:"";`-;   ,;;'`-.
      .''";;:     ,..   `.;;. .';;'.
     /  ,;;::,     `--'  ,.;: ::  .;:\
    ..- .; ;:,;,,.,   ,  ;;: ::;;:..;:.
   ;   ;    .;::,    ;:.;:::::::::;., ;
   |;. :      ;:;       `-;:::::-'""  |
   | ;,'  ,;::     ;.     `-;::  `;:::|
   ;`-;.   ,;:  ,;; `.  ."";,     ;;, ;
   '. ."".,        "".    ,;:;  '.,;::.
    `.                              .'
      `.                          .'
        `-.                    .-'
           ""--...______...--"""""

    print(ascii_art)

def folkvang():
    sleep(1)
    ascii_art = r"""             _______
          .-' _____ '-.
        .' .-'.  ':'-. '.
       / .''::: .:    '. \
      / /   :::::'      \ \
     | ;.    ':' `       ; |
     | |       '..       | |
     | ; '      ::::.    ; |
      \ \       '::::   / /
       \ '.      :::  .' /
        '. '-.___'_.-' .'
          '-._______.-"""

    print(ascii_art)

def kepernyo_calc(location):
    if location == 0:
        alapkepernyo()
    if location == 1:
        thorodin()
    if location == 2:
        ydalir()
    if location == 3:
        vidar()
    if location == 4:
        folkvang()