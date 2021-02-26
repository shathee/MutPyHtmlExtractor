import os, glob, sys, re, fileinput, argparse

from bs4 import BeautifulSoup
import csv

def collect_files_from_directory(pathToDirectory):
    return glob.glob(pathToDirectory +r"/**/*.html", recursive=True)

