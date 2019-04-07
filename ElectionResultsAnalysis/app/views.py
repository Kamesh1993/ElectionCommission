from django.shortcuts import render, render_to_response
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
import requests
from bs4 import BeautifulSoup
import csv
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
import os
from app.forms import StateForm, state_const_form

dict = {"Abhanpur": "53", "Ahiwara": "67", "Akaltara": "33", "Arang": "52", "Basna": "40", "Bastar": "85",
        "Beltara": "31", "Bijapur": "89", "Bilha": "29", "Durg City": "64", "AGAR": "166", "ALOTE": "223",
        "AMLA": "130", "ASHTA": "157", "ATER": "9", "BAGLI": "174", "BAIHAR": "108", "BANDA": "42", "BARGI": "96",
        "BETUL": "131", "Aizawl North-i": "10", "Aizawl North-ii": "11", "Aizawl North-iii": "12",
        "Aizawl East-i": "13", "Aizawl East-ii": "14", "Aizawl South-i": "18", "Aizawl South-ii": "19",
        "Aizawl South-iii": "20", "Aizawl West-i": "15", "Aizawl West-ii": "16", "Aizawl West-iii": "17",
        "Ahore": "141", "Amber": "47", "Anta": "193", "Asind": "177", "Bali": "120", "Bagru": "56", "Bansur": "63",
        "Bari": "78", "Bassi": "57", "Bhim": "173", "Alair": "97", "Armur": "11", "Boath": "8", "Chennur": "2",
        "Chevella": "53", "Dubbak": "41", "Gadwal": "79", "Jagtial": "21", "Jukkal": "13", "Mulug": "109"}

dict1={"Alwar Rural":"65" ,"Alwar Urban": "66" ,"Anupgarh": "6" ,"Asind": "177",
       "Aspur": "159" ,"Bagru": "120","Bali": "120","Banswara": "164","Baran-atru": "195","Bari sadri": "171",
       "Baseri":"77","Bayana":"76","Baytu":"136","Beawar":"168",
       "Ahiwara": "67", "Akaltara": "33", "Arang": "52", "Beltara": "31","Bilaigarh":"43","Bilha":"29",
       "Bindranawagarh":"55","Chitrakot":"87","Durg Gramin":"63","Gunderdehi":"61","Jaijaipur":"37",
       "Janjgirchampa":"34","Jashpur":"12","Kanker":"81","Kasdo":"l44",
       "Achampet":"82","Adilabad":"7","Alair":"97","Alampur":"80","Amberpet":"59","Andole":"36",
       "Armur":"11","Asifabad":"5","Aswaraopeta":"118","Bahadurpura":"69","Balkonda":"19","Banswada":"14",
       "Bellampalli": "3", "Bhadrachalam": "119", "Bhongir": "94",
        "AGAR":"166", "ALIRAJPUR": "191", "ALOTE": "223", "AMLA": "130", "ASHOK NAGAR": "32",
        "ATER": "9", "BADNAGAR": "218", "BADNAWAR": "202", "BAGLI": "174", "BAHORIBAND": "94", "BAIHAR": "108",
        "BAMORI": "28", "BANDA": "42", "BANDHAVGARH": "89", "BARGHAT": "114", "BASODA": "145", "BHAINSDEHI": "133",
       "Aizawl South-iii": "20", "Champhai South": "24", "Hachhek": "1", "Hrangturzo": "28","Lawngtlai East": "38",
       "Lawngtlai West": "37", "Lengteng": "21","Lunglei South": "33", "Palak": "40", "Serlui": "6", "Tawi": "9",
       "Thorang": "34"}

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def partywise(request):
    states={'s26':'Chattisgarh','s29':'Telangana','s12':'MadhyaPradesh','s16':'Mizoram','s20':'Rajasthan'}
    if request.method=="POST":
        form = StateForm(request.POST)
        state = form['dropdown']
        Name = states[state.data]
        ruby="C:/Users/admin/source/repos/ElectionResultsAnalysis/ElectionResultsAnalysis/app/static/scrape_data/"+Name+".csv"
        df = pd.read_csv(ruby,skiprows=2)
        df.plot(kind='bar',x='Party',y='Won',color='blue')
        plt.savefig('C:/Users/admin/source/repos/FlaskElectionDADV/FlaskElectionDADV/FlaskElectionDADV/static/plots/'+Name+".png")
        if(state.data=='s26'):
            return render(request,'app/chattisgarh.html')
        elif(state.data=='s12'):
            return render(request,'app/madhyapradesh.html')
        elif(state.data=='s20'):
            return render(request,'app/rajasthan.html')
        elif(state.data=='s29'):
            return render(request,'app/telangana.html')
        elif(state.data=='s16'):
            return render(request, 'app/mizoram.html')
        else:
            return render(request,'app/party.html')
    else:
        return render(request,'app/party.html')

def trend(request):
    if request.method=="POST":
        form = state_const_form(request.POST)
        Name = form['dropdown'].data
        Name4 = form['dropdown1'].data
        Name1 = dict1[Name4]
        id=Name1
        kamesh = str(Name+ ".csv")
        Name2 = (Name + Name1 + "")
        Name3 = Name2 + ".png"
        kk = str("C:/Users/admin/source/repos/ElectionResultsAnalysis/ElectionResultsAnalysis/app/static/data/"+Name+"/"+Name2+".csv")
        with open(kk, 'r') as f:
            var = []
            var = csv.reader(f, delimiter=",");
            left=[1]
            tick_label = []
            margin=[]
            for i in var:
                if len(i) is not 0:
                    if(id.__eq__(i[1])):
                        tick_label.append(i[2])
                        margin.append(int(i[3]))
                        if(len(i)!=4):
                            tick_label.append(i[4])
                            margin.append(int(i[5]))
                            left.append(2)
            fig = plt.figure()
            plt.bar(left, margin, tick_label=tick_label,width=0.5 ,color=['red', 'green'])
            plt.xlabel('Leading party');
            plt.ylabel('Margin');
            plt.title('Constituency- wise Trends')
            #plt.show()
            plt.savefig('C:/Users/admin/source/repos/ElectionResultsAnalysis/ElectionResultsAnalysis/app/static/scrape_data/graph.png');
            plt.clf()
            return render(request,'app/trend.html')
    else:
        return render(request,'app/trend.html')

def const(request):
    if request.method=="POST":
        dict={"Abhanpur":"53","Ahiwara":"67","Akaltara":"33","Arang":"52","Basna":"40","Bastar":"85","Beltara":"31","Bijapur":"89","Bilha":"29","Durg City":"64","AGAR":"166","ALOTE":"223","AMLA":"130","ASHTA":"157","ATER":"9","BAGLI":"174","BAIHAR":"108","BANDA":"42","BARGI":"96","BETUL":"131","Aizawl North-i":"10","Aizawl North-ii":"11","Aizawl North-iii":"12","Aizawl East-i":"13","Aizawl East-ii":"14","Aizawl South-i":"18","Aizawl South-ii":"19","Aizawl South-iii":"20","Aizawl West-i":"15","Aizawl West-ii":"16","Aizawl West-iii":"17","Ahore":"141","Amber":"47","Anta":"193","Asind":"177","Bali":"120","Bagru":"56","Bansur":"63","Bari":"78","Bassi":"57","Bhim":"173","Alair":"97","Armur":"11","Boath":"8","Chennur":"2","Chevella":"53","Dubbak":"41","Gadwal":"79","Jagtial":"21","Jukkal":"13","Mulug":"109"}
        form = state_const_form(request.POST)
        Name = form['dropdown'].data
        Name4 = form['dropdown1'].data
        Name1 = dict[Name4]
        Gadzou=str(Name+Name1+".csv")
        Name2=(Name+Name1+"")
        Name3=Name2+".png"
        Gadzou1=str("C:/Users/admin/source/repos/Election_Commission/Election_Commission/app/static/app/data/"+Name+"/"+Gadzou)
        with open(Gadzou1, 'r') as f:
            var = []
            c_name = []
            p_name = []
            votes = []
            left=[]
            j=0
            tick_label = []
            var = csv.reader(f, delimiter=",");
            for i in var:
                if len(i) is not 0:
                    c_name.append(i[0]);
                    p_name.append(i[1]);
                    votes.append(int(i[2]));
            fig = plt.figure()
            index = np.arange(len(c_name))
            plt.bar(c_name, votes,color=['red', 'yellow', 'blue', 'green', 'black']);
            plt.xlabel('Candidate_name');
            plt.ylabel('Votes polled per canditate');
            plt.xticks(index,c_name, fontsize=5, rotation=70)
            plt.title('Constituency- wise results')
            #plt.show()
            plt.savefig('C:/Users/admin/source/repos/ElectionResultsAnalysis/ElectionResultsAnalysis/app/static/plots/graph.png')
            plt.clf()
            return render(request,'app/constituency.html')
    else:
        return render(request,'app/const.html')