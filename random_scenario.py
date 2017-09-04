while True:
	
		

	
	

		###------------RANDOM_SCENARIO_GENERATOR---------------####
		#an unending matrix of possible solutions, scenarios, outcomes for the past, present, and future.
		#based on an idea that we may ourselves be living in a matrix or advanced computer simulation.
		print('\n')
		print("##############################################################################")
		print("#                                                                            #")
		print("#-----------------RANDOM_SCENARIO_GENERATOR----------------------------------#".title())
		print("#                                                                            #")
		print("# An unending matrix of possible solutions, scenarios                        #")
		print("# and outcomes for the past, present, and future....                         #")
		print("#                                                                            #")
		print("# Based on a theoretical idea that we may ourselves                          #") 
		print("# be living in a matrix or advanced computer simulation....                  #")
		print("#                                                                            #")
		print("#--(current program is based on the scenarios of domestic crime and disputes,#")
		print("# war, Politics and powers, weather and astronomical events)--               #")
		print("#                                                                            #")
		print("##############################################################################")
		print('\n')
		RSG = input ("              Would you like to start RANDOM_SCENARIO_GENERATOR?")
		if RSG.startswith('y') or RSG.startswith('Y'):
			print('\n\n')
			#scenarios related to domestic crime and disputes
			Race = ['White', 'Black', 'Asian', 'Indian', 'Mexican', 'Cuban', 'Italian', 'Spanish', 'Russian', 'Australian', 'British', 'Canadian',
				'Korean', 'African', 'American', 'German']
			Emotion = ['depressed', 'angered', 'apathetic', 'amused', 'negligent', 'irresponsible']
			Gender =['male','female']
			Crime =['shoots', 'stabs','rapes','asults','murders','drowns','robs','fights','frames']
			Motive =['Money', 'Sex', 'Cheating', 'Relationship', 'Drama', 'Attitude', 'Child Custody',
				'insurance', 'obsession', 'Racism']
				
											

											
			#scenarios related to war
			Country= ['North America', 'South America', 'Brazil', 'Italy', 'Spain', 'United Kingdom', 'China', 'North Korea', 'South Korea',
			'Syria', 'Russia', 'Australia', 'Africa', 'Egypt', 'Afghanistan', 'pakistan', 'Vietnam', 'Greenland', 'Iceland', 'Sweden',
			'Finland', 'Poland', 'Germany']
			Precursor= ['discusses', 'bans', 'threatens', 'engages', 'taunts', 'deligates', 'avoids', 'ignores', 'exchanges']
			Act =['Peace-talks', 'Chemical warfare', 'nuclear war', 'missle strikes', 'terrorism', 'global warming', 'weapons',
			'War', 'human rights', 'civil war', 'nuclear weapons']
			Side=['With', 'against', 'for']
			Motive_2 =['Money', 'Power', 'domination', 'humanity', 'refugees', 'peace', 'weapons', 'science', 'avoiding war', 'imminent war']

											

			#Scenarios related to government
			Country_2 = ['North America', 'South America', 'Brazil', 'Italy', 'Spain', 'United Kingdom', 'China', 'North Korea', 'South Korea',
			'Syria', 'Russia', 'Australia', 'Africa', 'Egypt', 'Afghanistan', 'pakistan', 'Vietnam', 'Greenland', 'Iceland', 'Sweden',
			'Finland', 'Poland', 'Germany']
			Precursor_2 = ['Legalizes', 'Criminalises', 'Bans', 'Supports', 'Opposes', 'Gives funding to', 'takes funding away from']
			Topic = ['Guns', 'high powered weapons', 'Smoking in public', 'Marijuana', 'Marijuana Reseach', 'Medical marijuana', 'Recreational Marijuana',
			'Tobacco', 'protesting', 'Space exploration', 'medical research', 'Scientific research', 'psychiatry', 'NASA', 'Abortion', 
			'Stem cell research', 'Global research', 'Racism']
			Side_2 = ['In support of', 'in opposition of', 'to advance', 'to further study', 'to focus on', 'related to']
			Outcome = ['Increasing Death', 'Decreasing Death', 'new diseases', 'Global warming', 'New Scientific advances', 'a new world',
			'Humanity', 'new Medical advances', 'resources', 'atmospheric conditions', 'accidental death', 'the human mind']		
						


					
			#scenarios related to weather and astronomical events
			Storm_Size = ['minor', 'Mid-level', 'Major', 'Astronomical']
			Event = ['Storm', 'Lightning Storm', 'rain events', 'Asteroid', 'Solar Flares', 'Drought', 'Tornados', 'Sunamis', 'hurricanes', 'typhoons',
			'volcanic eruptions', 'earthquakes', 'winds']
			Effects = ['Wild fires', 'Wide spread flooding', 'Flash flooding', 'damage', 'destruction', 'loss of life']
			Effects_2 = ['people homeless', 'people in fear', 'devastation', 'total loss', ]
			Deaths = ['0 deaths', 'under 10', 'under 100', 'under 1,000', 'under 10,000', 'under 100,000', 'over 100,000', 
			'over 1,000,000', 'over 1,000,000,000', 'Humanity is destroyed']
				
			import random
			
			print ("#############################################################")
			print ("#                                                           #")
			print ("#------programs generates 5 Scenarios at a time------       #")
			print ("#--Scenarios are based on DOMESTIC CRIME and DISPUTES--     #")
			print ("#                                                           #")
			print ("#############################################################")
			print ('\n')


			while True:
					count = 0
					while count < 5:
						count = count +1


						CRIME = print(random.choice(" "),("----"), end= " ")
						CRIME = print(random.choice(Emotion), end= " ")
						CRIME = print(random.choice(Race), end= " ")
						CRIME =print(random.choice(Gender), end= " ")
						CRIME= print(random.choice(Crime), end= " ")
						CRIME =print(random.choice(Race), end=  " ")
						CRIME =print(random.choice(Gender), end=  " " "related to" " ")
						CRIME =print(random.choice(Motive), end=  " " '\n')
						print('\n')
						
					print("        !????????????????????????????????????????????????!")
					print("        !?                                              ?!")
					CRIME = input("        !? Would you like to RUN Crime Scenarios AGAIN? ?!   ")
					print("        !?                                              ?!")
					print("        !????????????????????????????????????????????????!")
					print('\n')
					
					if CRIME.startswith('y') or CRIME.startswith('Y'):
						continue
					else: 
						break
					
			print('\n\n\n\n')
			print ("#############################################################")
			print ("#                                                           #")
			print ("#    ------programs generate 5 SCENARIOS at a time------    #")
			print ("#            --Scenarios are based on WAR--                 #")
			print ("#                                                           #")
			print ("#############################################################")
			print ('\n')
					
			while True:
					count = 0
					while count < 5:
						count = count +1

						WAR = print(random.choice(" "),("----"), end= " ")
						print(random.choice(Country), end= " ")
						print(random.choice(Precursor), end= " ")
						print(random.choice(Act), end= " ")
						print(random.choice(Side), end= " ")
						print(random.choice(Country), end=  " " "related to" " ")
						print(random.choice(Motive_2), end=  " " '\n')
						print('\n')
					
					print("        !????????????????????????????????????????????????!")
					print("        !?                                              ?!")
					WAR = input("        !? Would you like to run WAR Scenarios AGAIN?   ?!   ")
					print("        !?                                              ?!")
					print("        !????????????????????????????????????????????????!")
					print('\n')
					
					if WAR.startswith('y') or WAR.startswith('Y'):
						continue
					else: 
						break
					count = count +1

						
					
					
			print('\n\n\n\n')
			print ("#############################################################")
			print ("#                                                           #")
			print ("#   ------programs generate 5 SCENARIOS at a time------     #")
			print ("#      --Scenarios are based on POLITICS and POWER--        #")
			print ("#                                                           #")
			print ("#############################################################")
			print ('\n')



			while True:
					count = 0
					while count < 5:
						count = count +1


						GOVERNMENT = print(random.choice(" "),("----"), end= " ")
						print(random.choice(Country_2), end= " ")
						print(random.choice(Precursor_2), end= " ")
						print(random.choice(Topic), end= " ")
						print(random.choice(Side_2), end= " ")
						print(random.choice(Outcome), end=  " " '\n')
						print('\n')
					
					print("        !???????????????????????????????????????????????????!")
					print("        !?                                                 ?!")
					GOVERNMENT = input("        !? Would you like to run POLIICAL Scenarios AGAIN? ?!   ")
					print("        !?                                                 ?!")
					print("        !???????????????????????????????????????????????????!")
					print('\n')
					if GOVERNMENT.startswith('y') or GOVERNMENT.startswith('Y'):
						continue
					else: 
						break		
					count = count +1
						
						
						
						


				#Weather_events = 4


			print('\n\n\n\n')
			print ("#############################################################")
			print ("#                                                           #")
			print ("#   ------programs generate 5 Scenarios at a time------     #")
			print ("#--Scenarios are based on WEATHER and ASTRONOMICAL EVENTS-- #")
			print ("#                                                           #")
			print ("#############################################################")
			print ('\n')


			while True:
					count = 0
					while count < 5:
						count = count +1

						WEATHER = print(random.choice(" "),("----"), end= " ")
						print(random.choice(Storm_Size), end= " ")
						print(random.choice(Event), end= " " "causes" " ")
						print(random.choice(Effects), end= " " "and" " ")
						print(random.choice(Effects_2), end= " " '\n' "---Deaths estimated: " " ")
						print(random.choice(Deaths), end=  " ")
						print('\n')
				
					print("        !??????????????????????????????????????????????????!")
					print("        !?                                                ?!")
					WEATHER = input("        !? Would you like to run WEATHER Scenarios AGAIN? ?!   ")
					print("        !?                                                ?!")
					print("        !??????????????????????????????????????????????????!")
					print('\n')
					if WEATHER.startswith('y') or WEATHER.startswith('Y'):
						continue
					else: 
						break
					
			
		
		
