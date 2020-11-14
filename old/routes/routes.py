from flask import Flask, redirect

def main_page(): 
    return redirect("https://github.com/danmanners/non-disclosure-agreement", code=302)
