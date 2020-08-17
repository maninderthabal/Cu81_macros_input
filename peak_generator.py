import fileinput
import subprocess
import numpy as np

#states =[l, Ef, FixRtiotoState, Intensity, IfFixElambda, Sigma]

 #States for Ga83 singles histogram
#state1 =  [1, 0, -1, 300.6503,  7968.624, 0, 0.0]
#state2 =  [1, 0, -1, 800.3706,  6770.465, 0, 0.0]
#state3 =  [1, 0, -1, 2000.999,  5948.142, 0, 0.0]
#state4 =  [0, 0, -1, 2500.573,  5431.712, 0, 0.0]
#state17=  [1, 0, -1, 2000.3706, 5100.465, 0, 0.0]
#state5 =  [1, 0, -1, 5000.531,  4911.268, 0, 0.0]
#state6 =  [1, 0, -1, 5032.867,  4611.981, 0, 0.0]
#state7 =  [1, 0, -1, 3195.804,  4373.504, 0, 0.0]
#state8 =  [1, 0, -1, 3377.623,  4198.086, 0, 0.0]
#state9 =  [1, 0, -1, 3518.881,  4085.953, 0, 0.0]
#state10 = [1, 0, -1, 3086.013,  3991.210, 0, 0.0]
#state11 = [1, 0, -1, 2500.6503, 3924.682, 0, 0.0]
#state12 = [1, 0, -1, 2000.0839, 3863.519, 0, 0.0]
#state13 = [1, 0, -1, 1500.1538, 3819.758, 0, 0.0]
#state14 = [1, 0, -1, 1100.1538, 3777.657, 0, 0.0]
#state15 = [1, 0, -1, 700.7832,  3770.116, 0, 0.0]
#state16 = [1, 0, -1, 500.34965, 3745.117, 0, 0.0]

#Cu79 states generator#

#state1 =  [1, 0, -1, 140,  9504.253 , 0, 0.0]
#state2 =  [1, 0, -1, 1400,  6151.71 , 0, 0.0]
#state3 =  [1, 0, -1, 1400,  5694.831 , 0, 0.0]
#state4 =  [1, 0, -1, 2200,  5249.881 , 0, 0.0]
#state5 =  [0, 0, -1, 2200,  5035.983 , 0, 0.0]
#state6 =  [1, 0, -1, 2400,  4773.769 , 0, 0.0]
#state7 =  [1, 0, -1, 2250,  4661.060 , 0, 0.0]
#state8 =  [1, 0, -1, 1200,  4534.066 , 0, 0.0]
#state9 =  [1, 0, -1, 800,  4500.047 , 0, 0.0]
#state10 =  [1, 0, -1, 2200,  4419.506 , 0, 0.0]
#state11 =  [1, 0, -1, 700, 4389.739 , 0, 0.0]
#state12 = [1, 0, -1, 600,  4349.613 , 0, 0.0]
#state13 = [1, 0, -1, 650,  4309.143 , 0, 0.0]
#state14 = [1, 0, -1, 580,  4272.125 , 0, 0.0]
#state15 = [1, 0, -1, 500,  4208.411 , 0, 0.0]
#state16 = [1, 0, -1, 300,  4181.139 , 0, 0.0]
#state17 = [1, 0, -1, 230, 4150.523 , 0, 0.0]
#state18 = [1, 0, -1, 200,  4139.077 , 0, 0.0]
#state19 = [1, 0, -1, 250, 4121.110 , 0, 0.0]
#state20 = [1, 0, -1, 230, 4106.260 , 0, 0.0]
#state21 = [1, 0, -1, 200,  4095.525 , 0, 0.0]

#Cu80 states 
#state2 =  [1, 0, -1, 30, 9362.647, 0, 0.0]
#state1 =  [1, 0, -1, 20, 11920.623, 0, 0.0]
#state3 =  [1, 0, -1, 40, 8013.367, 0, 0.0]
#state4 =  [1, 0, -1, 70, 7479.797, 0, 0.0]
#state5 =  [1, 0, -1, 50, 7735.500, 0, 0.0]
#state6 =  [1, 0, -1, 50, 7376.995, 0, 0.0]
#state7 =  [1, 0, -1, 80,  9466.200, 0, 0.0]
#state8 =  [1, 0, -1, 260, 8025.726, 0, 0.0]
#state9 =  [1, 0, -1, 120, 7144.971, 0, 0.0]
#state10 =  [1, 0, -1, 480, 6862.535, 0, 0.0]
#state11 =  [1, 0, -1, 50,  6613.022, 0, 0.0]
#state12 =  [1, 0, -1, 340, 6896.844, 0, 0.0]
#state13 =  [1, 0, -1, 240, 6805.756, 0, 0.0]











#Cu81 States Generator#
#state1 = [1, 0, -1, 90, 4371.749, 0, 0.0]
#state2 = [1, 0, -1, 20, 3947.231, 0, 0.0]
#state3 = [1, 0, -1, 50, 3719.847, 0, 0.0]
#state4 = [1, 0, -1, 120, 3484.565, 0, 0.0]
#state5 = [1, 0, -1, 100, 3247.084, 0, 0.0]
#state6 = [1, 0, -1, 20, 3064.584, 0, 0.0] 
#state7 = [1, 0, -1, 100, 6142.020, 0, 0.0] 
#state8 = [1, 0, -1, 20, 6958.716, 0, 0.0] 

state1 =  [1, 0, -1, 20, 9200.003 , 0, 0.0]
state2 =  [1, 0, -1, 10,  8055.808 , 0, 0.0]
state3 =  [1, 0, -1, 50,  5551.850 , 0, 0.0]
state4 =  [0, 0, -1, 60,  4744.020 , 0, 0.0]
state5 =  [1, 0, -1, 90, 4371.749 , 0, 0.0]
state6 =  [1, 0, -1, 50, 3947.231 , 0, 0.0]
state7 =  [1, 0, -1, 80, 3719.847 , 0, 0.0]
state8 =  [1, 0, -1, 200,  3484.565 , 0, 0.0]
state9 =  [1, 0, -1, 80,  3247.084 , 0, 0.0]
state10 = [1, 0, -1,  40, 3064.584 , 0, 0.0]





#states = np.array([state1, state2,state3, state4, state5, state6, state7, state8, state9, state10, state11, state12, state13,state14, state15, state17, state18, state19, state20, state21])


#states = np.array([state1, state2, state3, state4, state5, state6, state7, state8, state9, state10, state11, state12, state13]) 

states = np.array([state1, state2, state3, state4, state5, state6, state7, state8, state9, state10])

for x in states:
  L = x[0] 
  Eff = x[1]
  FixState = x[2]
  Intensity = x[3]
  Energy= x[4] 
  FixElambda = x[5]
  Sigma= x[6]
  print(Energy)
  print('Angular Momentum of the state:',  L)
  print('Energy of the state:', Energy)
  s= str(Energy)
  ss = s.split(".")

  filename = 'Zn81_' + str(ss[0])+'_'+str(ss[1]) + '.input'
  fin = open("Ge83_xxxx.input", "rt")
  fout = open(filename, "wt")
  for line in fin:
      newline = line.replace('Lorb 1', 'Lorb ' + str(x[0]))
      newline = newline.replace('Ef 0', 'Ef '+ str(x[1]) )
      newline = newline.replace('FixRatioToState -1', 'FixRatioToState '+ str(x[2]))
      newline = newline.replace('Int 13378.76', 'Int '+str(x[3]))
      newline = newline.replace('Elambda 5000.00', 'Elambda '+ str(x[4]))
      newline = newline.replace('IfFixElambda 0', 'IfFixElambda '+str(x[5]))
      newline = newline.replace('AddSigma 5.0', 'AddSigma '+ str(x[6]))
      fout.write(newline)
fout.close()
fin.close()