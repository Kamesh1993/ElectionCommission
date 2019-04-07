$(document).ready(function () {
document.getElementById("state1").options.length=0;
    var list = ["--Select State--", "Chattisgarh", "MadhyaPradesh", "Mizoram", "Rajasthan", "Telangana"];
    for(var i=0;i<list.length;i++)
    {
      var select = document.getElementById("state1");
      select.options[select.options.length] = new Option(list[i],list[i]);
    }
});

function checkState()
{
var list=document.getElementById("state1");
if(list.value==="--Select State--")
{
alert("select State");
return false;
}
return true;
}

function checkConstituency()
{
var list=document.getElementById("constituency1");
if(list.value==="--Select Constituency--")
{
alert("select Constituency");
return false;
}
return true;

}

function update()
{
 
            var list1 = document.getElementById('state1');
            document.getElementById("constituency1").options.length=0;
            if(list1.value==='Chattisgarh')
            {
		var list =["--Select Constituency--","Abhanpur","Ahiwara","Akaltara","Arang","Basna","Bastar","Bijapur","Beltara","Bilha","Durg City"]
                
                for(var i=0;i<list.length;i++)
                {
                 var select = document.getElementById("constituency1");
                 select.options[select.options.length] = new Option(list[i],list[i]);
                }
            }
            else if (list1.value==='Telangana')
            {
                var list =["--Select Constituency--","Aliar","Armur","Boath","Chennur","Chevella","Dubbak","Gadwal","Jagtial","Jukkal","Mulug"]
                for(var i=0;i<list.length;i++)
                {
                 var select = document.getElementById("constituency1");
                 select.options[select.options.length] = new Option(list[i],list[i]);
                }
            }
			else if (list1.value==='Mizoram')
            {
                var list =["--Select Constituency--","Aizawl North-i","Aizawl North-ii","Aizawl North-iii","Aizawl East-i","Aizawl East-ii","Aizawl South-i","Aizawl South-ii","Aizawl South-iii","Aizawl West-i","Aizawl West-ii","Aizawl West-iii"]
                for(var i=0;i<list.length;i++)
                {
                 var select = document.getElementById("constituency1");
                 select.options[select.options.length] = new Option(list[i],list[i]);
                }
            }
			else if (list1.value==='Rajasthan')
            {
                var list =["--Select Constituency--","Ahore","Amber","Anta","Asind","Bali","Bagru","Bansur","Bari","Bassi","Bhim"]
                for(var i=0;i<list.length;i++)
                {
                 var select = document.getElementById("constituency1");
                 select.options[select.options.length] = new Option(list[i],list[i]);
                }
            }
			else if (list1.value==='MadhyaPradesh')
            {
                var list =["--Select Constituency--","AGAR","ALOTE","AMLA","ASHTA","ATER","BAGLI","BAIHAR","BANDA","BARGI","BETUL"]
                for(var i=0;i<list.length;i++)
                {
                 var select = document.getElementById("constituency1");
                 select.options[select.options.length] = new Option(list[i],list[i]);
                }
               
            }
}

function updatetrend(){
 
            var list1 = document.getElementById('state1');
            document.getElementById("constituency1").options.length=0;
            if(list1.value==='Chattisgarh')
            {
		var list =["--Select Constituency--","Ahiwara","Akaltara","Arang","Beltara","Bilaigarh","Bilha","Bindranawagarh","Chitrakot","Durg Gramin","Gunderdehi","Jaijaipur","Janjgirchampa","Jashpur","Kanker"]
                
                for(var i=0;i<list.length;i++)
                {
                 var select = document.getElementById("constituency1");
                 select.options[select.options.length] = new Option(list[i],list[i]);
                }
            }
            else if (list1.value==='Telangana')
            {
                var list =["--Select Constituency--","Achampet","Adilabad","Alair","Alampur","Amberpet","Andole","Armur","Asifabad","Aswaraopeta","Bahadurpura","Balkonda","Banswada","Bellampalli","Bhadrachalam","Bhongir"]
                for(var i=0;i<list.length;i++)
                {
                 var select = document.getElementById("constituency1");
                 select.options[select.options.length] = new Option(list[i],list[i]);
                }
            }
			else if (list1.value=='Mizoram')
            {
                var list =["--Select Constituency--","Aizawl South-iii","Champhai South","Hachhek","Hrangturzo","Lawngtlai East","Lawngtlai West","Lengteng","Lunglei South","Palak","Serlui","Tawi","Thorang"]
                for(var i=0;i<list.length;i++)
                {
                 var select = document.getElementById("constituency1");
                 select.options[select.options.length] = new Option(list[i],list[i]);
                }
            }
			else if (list1.value=='Rajasthan')
            {
                var list =["--Select Constituency--","Alwar Rural","Alwar Urban","Anupgarh","Asind","Aspur","Bagru","Bali","Banswara","Baran-atru","Bari sadri","Baseri","Bayana","Baytu","Beawar"]
                for(var i=0;i<list.length;i++)
                {
                 var select = document.getElementById("constituency1");
                 select.options[select.options.length] = new Option(list[i],list[i]);
                }
            }
			else if (list1.value=='MadhyaPradesh')
            {
                var list =["--Select Constituency--","AGAR","ALIRAJPUR","ALOTE","AMLA","ASHOK NAGAR","ATER","BADNAGAR","BADNAWAR","BAGLI","BAHORIBAND","BAIHAR","BAMORI","BANDA","BANDHAVGARH","BARGHAT","BASODA","BHAINSDEHI"]
                for(var i=0;i<list.length;i++)
                {
                 var select = document.getElementById("constituency1");
                 select.options[select.options.length] = new Option(list[i],list[i]);
                }
               
            }
}