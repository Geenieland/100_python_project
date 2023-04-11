import turtle as turtle_module                                                                                        
import random                                                                                                         
                                                                                                                      
                                                                                                                      
turtle_module.colormode(255)                                                                                          
tim = turtle_module.Turtle()                                                                                          
color_list = [(194, 163, 120), (137, 83, 57), (67, 101, 125), (219, 201, 140), (164, 150, 54),                        
              (137, 161, 177), (70, 36, 27), (125, 37, 25), (60, 113, 87), (147, 176, 156), (194, 99, 79),            
              (117, 80, 88), (230, 175, 165), (29, 53, 71), (171, 148, 158), (60, 39, 42), (24, 90, 65), (97, 146, 117
              (116, 34, 40), (189, 92, 97), (23, 66, 50), (99, 138, 150), (25, 81, 89), (46, 62, 87), (178, 201, 182),
              (220, 176, 181)]                                                                                        
tim.penup()                                                                                                           
tim.hideturtle()                                                                                                      
tim.speed("fastest")                                                                                                  
tim.setheading(225)                                                                                                   
tim.forward(300)                                                                                                      
tim.setheading(0)                                                                                                     
num_of_dots = 100                                                                                                     
                                                                                                                      
                                                                                                                      
for dot_count in range(1, num_of_dots + 1 ):                                                                          
    tim.dot(20, random.choice(color_list))                                                                            
    tim.forward(50)                                                                                                   
                                                                                                                      
    if dot_count % 10 == 0:                                                                                           
                                                                                                                      
        tim.setheading(90)                                                                                            
        tim.forward(50)                                                                                               
        tim.setheading(180)                                                                                           
        tim.forward(500)                                                                                              
        tim.setheading(0)                                                                                             
                                                                                                                      
                                                                                                                      
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    
                                                                                                                      
screen = turtle_module.Screen()                                                                                       
screen.exitonclick()                                                                                                  
                                                                                                                      
