from random import random
from tkinter import INSIDE
from django.shortcuts import render , redirect ,HttpResponse
from time import gmtime, strftime
import random

def index(request):

    #1st session
   if not(request.session.get("yourGold")):
    yourGold=0
    activity=[{'color' :'c1','text' : ''}]
    request.session["yourGold"]=yourGold
    request.session["activity"]=activity
    request.session["yourlocation"]=''

# the locations that going to render.
    goldLocations = ["farm","cave","house","quest"]

# the info going to render
    context = {
        'gold': request.session['yourGold'],
        'activity' : request.session['activity'],
        'goldLocations' :goldLocations
    }
    return render(request,'index1.html',context)




def process_money (request):

    # to make sure the request is POST
    if request.method != 'POST':
        return redirect('/') #if not we are going to not process anything

    # processing if the request is POST
    currentLocation = request.POST['location']
    request.session['currentLocation'] = currentLocation


    #update yourGold
    if (currentLocation == 'quest'):
        #to randomly specify subtraction or addition.
        if random.randint(0,1): 
            gold = random.randint(1, 50)
        else:
            gold = random.randint(1, 50) * -1
    else:
        #for the other locations its random addition
        gold = random.randint(10, 20)

    request.session['yourGold'] += gold
    color = 'c1'

    #addin activity.
    if (gold < 0): #means its quest with subtraction
        text = f'You failed a Quest and lost {gold} Ouch '
        color = "c2"
    else: #means its addition
        text = f'You entered a {currentLocation} and earned {gold} '
        

    #specifying current time.
    time = strftime("%m %d %Y %H : %M %p", gmtime())
    text += f"( {time} )"
    activity = {'color' :color,
                'text' : text }
        
    #pushing a new activity to thee screen
    request.session["activity"].append(activity)
    request.session.save()
    
    return redirect('/')