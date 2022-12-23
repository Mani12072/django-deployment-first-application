from django.shortcuts import render
from django.http import HttpResponse;

# Create your views here.
def display(request): #view-function
	ss = "<center><h2 style='color:Blue;'>Hello User, Welcome to Django First-Project First-App</h2><hr /></center>";
	return HttpResponse(ss);

def show(request):
    ss= '''      
           
           <!--
	HTML Webpage to display "Welcome-Message" with different Headings 
	(F:\python3\HTML\Welcome.html)
-->
<html>
    <head>
	   
	   <title>****WELCOME-TO-ANIMALS-PICTURE****</title>
        <style/> 
		h1{
		   color:red; 
		}
		h2{
		   color:green; 
		}
		h3{
		   color:gray; }
		h4{
		   color:orange; 
		}
		h5{
		   color:purple;
		}
		h6{ 
		   color:ash; 
		}
		h1,h3,h5{ 
		   background-color:yellow;
		} 
		h2,h4,h6{
		   background-color:skyblue; 
		} 
		</style>
	</head>
	    <body>
			    <center>
			     <h1> WELCOME TO ANIMALS PICTURES </h1>
				 <hr color="orange" />
				 </center>
				 <img src="animal.jpg",alt="animal",height ="180" width="230" />
				 <center>
				 <h2> WELCOME TO ANIMALS PICTURES </h2>
				 <hr color="brown" />
				 </center>
				 <img src="animal1.jpg",alt="animal1",height ="180" width="230" />
				 <center>
				 <h3> WELCOME TO ANIMALS PICTURES </h3>
				 <hr color="light-green" />
				 </center>
				 <img src="animal2.jpg",alt="animal2",height ="180" width="230" />
				 <center>
				 <h4> WELCOME TO ANIMALS PICTURES </h4>
				 <hr color="pink" />
				 </center>
				 <img src="animal3.jpg",alt="animal3",height ="180" width="230" />
				 <center>
				 <h5> WELCOME TO ANIMALS PICTURES </h5>
				 <hr color="blue" />
				 </center>
				 <img src="animal4.jpg",alt="animal4 ",height ="180" width="230" />
				 <center>
				 <h6> WELCOME TO ANIMALS PICTURES </h6>
			    <hr color="red" />
			    </center>	
			    <img src="animal5.jpg",alt="animal5 ",height ="180" width="230" />
		</body>
    </head>
</html>	
            
             
        ''';
        
    return HttpResponse(ss);