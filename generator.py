import wikipedia as wiki
from bs4 import BeautifulSoup
import requests
import re
import random
import os



def wikiGrab():
	game_page = wiki.page("List of video game genres")
	lovgg_url = game_page.url

	game_content = game_page.content
	sections = game_content.split("\n\n\n")

	game_types = {}
	for s in sections:

		descr = re.split(r'[=][\n][\n]*', s)

		genreMatch = re.match(r'[=]+ (.*) [=]+', s)
		if(genreMatch and (len(descr) > 1)):
			game_types[genreMatch.group(1)] = descr[1]

	for a in game_types.keys():
		if(game_types[a] == None):
			game_types[a] = game_page.section(a)

	return game_types


def themeGrab():
	tgs = open("game_themes.txt", "r")
	themes = tgs.readlines()
	return themes


def litGenreGrab():
	lg = open("lit_genres.txt", "r")
	lit_genres = lg.readlines()
	return lit_genres


def artGrab():
	al = open("art_styles.txt", "r")
	arts = al.readlines()
	return arts




def randomGenre(g_types):
	keys = []
	for k in g_types.keys(): keys.append(k)
	x = random.randint(0,len(g_types)-1)
	genre = keys[x]
	print(genre)
	print("")
	print(g_types[genre])


def randomThing(list):
	print(list[random.randint(0, len(list)-1)])



def main():
	game_genres = wikiGrab()
	game_themes = themeGrab()
	lit_themes = litGenreGrab()
	art_styles = artGrab()
	user = "yes"
	while((user != "no") and (user != "n")):
		os.system('clear')
		print("***GAME GENRE***")
		randomGenre(game_genres)
		print("\n")
		print("***THEME***")
		randomThing(game_themes)
		print("\n")
		print("***ART STYLE***")
		randomThing(art_styles)
		print("\n")
		print("***STORY GENRE***")
		randomThing(lit_themes)
		user = input("\n\n\nNew game? ")



if __name__ == "__main__":
	main()