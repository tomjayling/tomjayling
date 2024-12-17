
import numpy as np
import matplotlib.pyplot as plt

class Frame:
    #class that can hold a 4-momenta 
    
    def __init__(self, fourmomenta):
        self.fm = fourmomenta
        self.E = fourmomenta[0]
        self.px = fourmomenta[1]
        self.py = fourmomenta[2]
        self.pz = fourmomenta[3]
    
class Boost:
    #class can transform a 4-momentum from one Lorentz frame to another
    
    def __init__(self, frame):
        #constructor takes a frame as an argument that defines the boost of the transform method
        
        self.f = frame
    
    def transform(self, frame):
        #method that uses lorentz boost equation to transform the input frame to the boost frame and returns the tranformed frame
        
        c = 3*(10**8)
        bx = self.f.px/c - frame.px/c
        by = self.f.py/c - frame.py/c
        bz = self.f.pz/c - frame.pz/c

        b = np.sqrt(bx**2+by**2+bz**2)
        g = 1/np.sqrt(1-b**2)
        a = g**2/(1+g)
        M = [[g,-g*bx, -g*by,-g*bz],[-g*bx, 1+a*bx**2, a*bx*by, a*bx*bz],[-g*by, a*bx*by, 1+a*by**2, a*by*bz],[-g*bz, a*bx*bz, a*by*bz, 1+a*bz**2]]
        E = M[0][0]*frame.E + M[0][1]*frame.px + M[0][2]*frame.py + M[0][3]*frame.pz
        expected_E = g*(frame.E - b*frame.pz)

        px = M[1][0]*frame.E + M[1][1]*frame.px + M[1][2]*frame.py + M[1][3]*frame.pz
        py = M[2][0]*frame.E + M[2][1]*frame.px + M[2][2]*frame.py + M[2][3]*frame.pz
        pz = M[3][0]*frame.E + M[3][1]*frame.px + M[3][2]*frame.py + M[3][3]*frame.pz
        tfourmomenta = [E,px,py,pz]
        tframe = Frame(tfourmomenta)
        
        return tframe
    
    
class Database:
    
    def __init__(self, address):
        #constructor takes a file address as an argument which is used to read data from
        
        self.file = open(r""+address+"","r")
        self.lines = self.file.readlines()
        self.events = list()
        lastbreak = True
        event = []
        
        #break up data into events that are separated by blank lines in the Pythia 8 data
        for line in self.lines:
            # check if line empty
            line = line.strip()
            if line == "":
                if len(event) > 0:
                    self.events.append(event)
                    event = []
                lastbreak = True
                continue
            if len(line) > 0 and line[0] == '#':
                continue
            # line not empty -- add to events
            lastbreak = False

            event.append(line)
        if not lastbreak:
            self.events.append(event)
            
    def read_next_event(self, n):
        #lets a specific event be read in defined by the index n in the events list, not very useful as events can be publicly accessed?
        
        return self.events[n]
    
    
def getCombinations(event):
    #evaluates particles in each event and stores pairs of particles that could be combined to make a deuteron or anti-deuteron
    
    particles = []
    combs = []
    
    #checks each line, which corresponds to an individual particle in the event
    for line in event:
        n=0
        m=0
        particle = []
        
        #splits the data in each line into the ID, E, px, py, pz, and m
        for c in line:
            if (c == ' '):
                if (m-n) > 1:
                    particle.append(line[n:m])    
                n = m
            m += 1
        particle.append(line[n:m]) 
        [pid, E, px, py, pz, m] = particle
        
        #stores the variables in a dictionary with the ID as the key
        value = [E, px, py, pz, m]
        key = pid
        
        #if z component of momenta is much larger than x and y components then disregard
        if (float(px) + float(py))/float(pz) > 0.01:
            particles.append((key,value))
        
    i = 0
    l = len(event)    
    
    #compares each ID to ones after it to find matches that correspond to a p-n or ap-an combination
    for (key1, value1) in particles:
        i += 1
        if i < l:
            for (key2, value2) in particles[i:l]:
                if not key1 == key2 and ((key1 in key2) or (key2 in key1)):
                    if '-' in key1:
                        key3 = 'antideuteron'
                    else:
                        key3 = 'deuteron'
                    combs.append(key3,(value1, value2))
    return combs  


def find_k(boosted_A,boosted_B):
    # calculates the distance between two particles, that have been boosted to the COM frame, in momentum space
    
    k = np.sqrt((boosted_A.px-boosted_B.px)**2 + (boosted_A.py - boosted_B.py)**2 + (boosted_A.pz - boosted_B.pz)**2)
    return k


def two_body_decay(vector, m1, m2):
    #decays a two body final state into two decay products
    
    product1 = []
    product2 = []
    
#   randomly splits momentum into two so that momentum is conserved
    p = np.sqrt(vector[1]**2 + vector[2]**2 + vector[3]**2)
    r = np.random.random()*p
    
    #calculate energy using E**2 = p**2 + m**2
    E1 = np.sqrt(r**2 + m1**2)
    E2 = np.sqrt((p-r)**2 + m2**2)
    product1.append(E1)
    product2.append(E2)
    
    #preserve ratio of components of momenta to the total momentum, for each particle
    product1.append(vector[1]*r/p)
    product1.append(vector[2]*r/p)
    product1.append(vector[3]*r/p)
    product2.append(vector[1]*(p-r)/p)
    product2.append(vector[2]*(p-r)/p)
    product2.append(vector[3]*(p-r)/p)
    
    
#     #alternative method
#     E1 = (vector[0]**2 + m1**2-m2**2)/2*vector[0]
#     E2 = (vector[0]**2 + m2**2-m1**2)/2*vector[0]
#     p1 = np.sqrt(E1**2 - m1**2)
#     p2 = np.sqrt(E2**2 - m2**2)
#     x = p1**2 + p2**2
#     rnums = np.ones(3)
#     for i in index:
#         y = np.random()*x 
#         i = y
#     rnums = rnums.sort()
#     p1x = np.sqrt(rnums[0]/2)
#     p2x = -p1x
#     p2y = np.sqrt((rnums[1]-rnums[2])/2)
#     p1y = -p2y
#     p1z = np.sqrt((rnums[2]-rnums[1])/2)
#     p2z = -p1z
    
#     product1 = [E1, p1x, p1y, p1z]
#     product2 = [E2, p2x, p2y, p2z]
    return product1, product2

#not isotropic


def coalescence_model(db):
    #implements the coalescence model using the tools that have been defined above. Returns a list of transverse momenta
    
    #cutoff chosen to be 150keV expressed in MeV as 0.15
    cutoff = 0.15
    deuterons = []
    antideuterons = []
    
    # 1. Create all pn and  ̄p ̄n combinations in an event.
    for event in db.events:
        combs = getCombinations(event)

    # 2. Randomly select a combination, boost into its centre-of-mass frame and calculate the magnitude of the
    # three three-momentum difference, k.

        for c in combs:
            A = c[1]
            B = c[2]
            E_A = float(A[0])
            E_B = float(B[0])
            px_A = float(A[1])
            py_A = float(A[2])
            pz_A = float(A[3])
            px_B = float(B[1])
            py_B = float(B[2])
            pz_B = float(B[3])
            m_A = float(A[4])
            m_B = float(B[4])

            frame_A = Frame((E_A, px_A, py_A, pz_A))
            frame_B = Frame((E_B, px_B, py_B, pz_B))
            
            #define boosts to COM and back to lab
            frame_COM = Frame((E_A + E_B, 0, 0, 0))
            boost_to_COM = Boost(frame_COM)
            boost_to_lab = Boost(frame_A)
            
            #transform A and B to COM and calculate k
            frame_A = boost_to_COM.transform(frame_A)
            frame_B = boost_to_COM.transform(frame_B)
            k = find_k(frame_A,frame_B)


            # 3. If k is below some cut-off, combine the proton and neutron, or the anti-proton and anti-neutron. Otherwise,
            # return to Step 2 and select a new combination.
            if k > cutoff:
                #return to step 2
                continue
            #combine A and B
            frame_C = Frame(np.add(frame_A.fm, frame_B.fm))

            # 4. Isotropically decay this combined momentum four-vector into a two-body final state, a deuteron and
            # photon or an anti-deuteron and a photon, given the initial state.

            deut, photon = two_body_decay(frame_C.fm, m_A + m_B, 0)
            deut = Frame(deut)
            photon = Frame(photon)
            
            # 5. Boost these decay products back into the lab frame and return to Step 2 until all combinations have been
            # checked.
            deut = boost_to_lab.transform(deut)
            photon = boost_to_lab.transform(photon)
            
            #find transverse momentum from deuteron (or anti-deuteron) x and y components, since beam is along z direction
            pT = np.sqrt(deut.px**2 + deut.py**2)
            if c[0] == 'deuteron':
                deuterons.append(pT)
            if c[1] == 'antideuteron':
                antideuterons.append(pT)
            
            #no way of removing combinations with the same particle
            #transverse momentum is wrong
            
    return deuterons, antideuterons


#Main Code

#create a database using the pythia 8 file
deuteron = Database("pythia.crdownload ")

#perform the coalescence model on the database to get the deuteron and anti-deuteron transverse momentum 
deuts, antideuts = coalescence_model(deuteron)

#plot the cross section from the coalescence model as a funtion of the deuteron and anti-deuteron transverse momentum

#create histogram data
(counts1, bins1) = np.histogram(deuts, bins= 50)
(counts2, bins2) = np.histogram(antideuts, bins= 50)

#scale for the cross section and plot
N = len(deuteron.events)

#use equation for cross section which is number of deuterons (counts) divided by the number of events processed (N) times
#the inelastic cross section (100000microB)
factor = (1/N)*(100/0.3894)
fig1 = plt.figure()
ax1 = fig1.add_subplot(1,1,1)
ax2 = fig1.add_subplot(1,1,1)
ax1.hist(bins1[:-1], bins1, weights = factor*counts1)
ax1.title('Cross section from coalescence model as a function of deuteron transverse momentum')
ax1.xlabel('Deuteron Transverse Momenta (GeV)')
ax1.yscale('log')
ax1.ylabel('Cross section (GeV**2)')
ax1.legend(['distribution'])

ax2.hist(bins2[:-1], bins2, weights = factor*counts2)
ax2.title('Cross section from coalescence model as a function of anti-deuteron transverse momentum')
ax2.xlabel('Anti-Deuteron Transverse Momenta (GeV)')
ax2.yscale('log')
ax2.ylabel('Cross section (GeV**2)')
ax2.legend(['distribution'])
plt.show
