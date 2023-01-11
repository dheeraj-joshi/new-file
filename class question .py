"""4. Create a list of 7 cars with car data for, Milage, Name, Doors, Tires, Sunroof
(true or false), 0to60, brand. Now access the "0to60" 
value of 5th index. Now add two more cars to the list
 and print brand of car with index 7."""

carList = [{"name": "swift", "0_60": "12sec","doors":"4","tyres":"4","sunroof":"true","brand":"maruti suzuki"}, 
{"name": "toyato", "0_60": "3sec","doors":"4","tyres":"4","sunroof":"false","brand":""}, 
{"name": "mahindra", "0_60": "1sec","doors":"4","tyres":"4","sunroof":"true","brand":"thar"},
{"name": "swift desire", "0_60": "15sec","doors":"4","tyres":"4","sunroof":"true","brand":" suzuki"},
{"name": "xuv 700", "0_60": "9sec","doors":"4","tyres":"4","sunroof":"true","brand":"mahindra"},
{"name": "altroz", "0_60": "0.32sec","doors":"4","tyres":"4","sunroof":"true","brand":"tata"},
{"name": "pollo", "0_60": "2sec","doors":"4","tyres":"4","sunroof":"true","brand":"tata"}
]
print("index of 5th mileage:",carList[5]["0_60"])
carList.append({"name": "safari", "0_60": "2sec","doors":"4","tyres":"4","sunroof":"true","brand":"tata"})
carList.append({"name": "x7", "0_60": "2sec","doors":"4","tyres":"4","sunroof":"true","brand":"bmw"})

print("the brand of car:",carList[6]['brand'])
print(carList[0])


                                    
